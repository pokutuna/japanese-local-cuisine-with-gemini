from scrapy.http import Response as Response

def gunzip(data: bytes) -> bytes: ...
def gzip_magic_number(response: Response) -> bool: ...
