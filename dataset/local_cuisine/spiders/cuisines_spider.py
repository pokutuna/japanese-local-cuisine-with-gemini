import re

import scrapy


class CuisinesSpider(scrapy.Spider):
    name = "cuisines"
    allowed_domains = ["www.maff.go.jp"]
    start_urls = ["https://www.maff.go.jp/j/keikaku/syokubunka/k_ryouri/index.html"]

    custom_settings = {
        "DOWNLOAD_DELAY": 0.5,
        "CONCURRENT_REQUESTS_PER_DOMAIN": 4,
    }

    def parse(self, response):
        """トップページから県ごとのページをたどる"""
        table = response.css("#main_content div.menu8_tab_pc")
        area_rows = table.css("dl")
        for area in area_rows:
            area_name = area.css("dt::text").get()
            for item in list(area.css("dd a")):
                pref_name = item.css("a::text").get()
                pref_url = response.urljoin(item.css("a::attr(href)").get())
                pref_id = pref_url.split("/")[-1].split(".")[0]
                pref = dict(
                    area_name=area_name,
                    pref_id=pref_id,
                    pref_name=pref_name,
                    pref_url=pref_url,
                )
                yield response.follow(pref_url, self.parse_pref, meta=dict(pref=pref))

    def parse_pref(self, response):
        """県ごとのページから料理ごとのページをたどる"""
        cuisine_items = response.css("#main_content .section ul:first-of-type li")
        for item in cuisine_items:
            url = response.urljoin(item.css("a::attr(href)").get())
            yield response.follow(url, self.parse_cuisine, meta=response.meta)

    def parse_cuisine(self, response):
        """料理ごとのページから情報を抽出する"""
        pref = response.meta["pref"]

        url = response.url
        cuisine_id = url.split("/")[-1].split(".")[0]

        # 名前
        nameline = response.css(
            "#main_content ul.menu_details:first-child h2 .name::text"
        ).get()
        (name, ruby) = self.decompose_name(nameline)

        # メイン画像 & 利用可否
        (image_url, can_download_image) = self.cuisine_image(response)

        # 説明
        try:
            details_container = response.css(
                "#main_content ul.menu_details li:nth-child(n+2)"
            )
            details = self.cuisine_details(details_container)
            details_text = self.format_details_text(details)
        except Exception:
            details = None
            details_text = None

        # レシピ
        # ないこともある
        # 例: https://www.maff.go.jp/j/keikaku/syokubunka/k_ryouri/search_menu/menu/37_22_toyama.html
        try:
            recipe_container = response.css("#main_content .jsPrintBtn")[0].xpath("..")
            recipe = self.cuisine_recipe(recipe_container)
            recipe_text = self.format_recipe_text(recipe)
        except Exception:
            recipe = None
            recipe_text = None

        yield dict(
            id=cuisine_id,
            url=url,
            name=name,
            ruby=ruby,
            image_url=image_url,
            image_can_download=can_download_image,
            details=details,
            details_text=details_text,
            recipe=recipe,
            recipe_text=recipe_text,
            **pref,
        )

    def format_lines(self, iter):
        return " ".join(
            map(lambda i: i.strip(), filter(lambda i: not i.isspace(), iter))
        )

    def decompose_name(self, nameline) -> tuple[str, str]:
        """名前と読みを分ける"""
        parts = re.split(r"[()（）]", nameline)
        if len(parts) == 3:
            return (parts[0], parts[1])
        else:
            return (parts[0], parts[0])

    def cuisine_image(self, response) -> tuple[str | None, bool]:
        """料理のメイン画像 URL と、ダウンロード可能かを返す"""
        url = response.urljoin(
            response.css("#main_content .menu_main h2 img::attr(src)").get()
        )
        filename = url.split("/")[-1]
        if filename.startswith("noimage"):
            return (None, True)

        thumbs = response.css(
            f'#main_content .menu_main .modalWrap img[src*="{filename}"]'
        )
        if len(thumbs) == 0:
            return (url, False)

        text_around_thumb = "".join(thumbs[0].xpath("../..//text()").getall())
        can_download = "画像をダウンロード" in text_around_thumb
        return (url, can_download)

    def cuisine_details(self, container) -> list[dict]:
        """料理の詳細情報を label, content の dict のリストで返す"""
        details = []
        for item in container:
            # h3(見出し) に 複数の p(コンテンツ) が続く
            label = self.format_lines(
                item.css("h3:first_of_type").css("*::text").getall()
            )
            label = label.split("（")[
                0
            ].strip()  # 末尾の注釈(=保存・継承の取組 の説明)を削除
            content = self.format_lines(item.css("p::text").getall())
            details.append(dict(label=label, content=content))
        return details

    def format_details_text(self, details) -> str:
        return "\n".join(map(lambda i: f"{i['label']}:\n{i['content']}\n", details))

    def cuisine_recipe(self, container) -> dict:
        """料理のレシピを返す"""
        heading = "".join(container.css("h2:first-of-type::text").getall())
        match = re.search(r"[(（]([^)）]+)", heading)
        servings = match.groups()[0] if match else ""  # n 人分

        ingredients = []
        for entry in container.css("ul.menu_material > li"):
            item = self.format_lines(entry.css("li:nth-child(1)::text").getall())
            amount = self.format_lines(entry.css("li:nth-child(2)::text").getall())
            if item != "" and amount != "":
                ingredients.append(dict(item=item, amount=amount))

        steps = []
        for entry in container.css("ul.recipe > li"):
            lines = entry.css("*::text").getall()
            lines = list(filter(lambda i: not i.isspace(), lines))
            if len(lines) > 0 and re.match(r"^\d+", lines[0]):
                lines[0] = lines[0] + "."
            steps.append(self.format_lines(lines))

        return dict(
            servings=servings,
            ingredients=ingredients,
            steps=steps,
        )

    def format_recipe_text(self, recipe) -> str:
        ingreding_part = "\n".join(
            map(
                lambda i: i["item"]
                if i["amount"] == ""
                else f'- {i['item']}: {i['amount']}',
                recipe["ingredients"],
            )
        )
        steps_part = "\n".join(map(lambda i: f"- {i}", recipe["steps"]))
        return "\n".join(
            [
                f"材料 ({recipe["servings"]})",
                ingreding_part,
                "",
                "作り方",
                steps_part,
            ]
        )
