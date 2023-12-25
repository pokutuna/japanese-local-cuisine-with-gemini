import signal
from _typeshed import Incomplete
from types import FrameType
from typing import Any, Callable, Dict, Optional, Union

SignalHandlerT = Union[Callable[[int, Optional[FrameType]], Any], int, signal.Handlers, None]
signal_names: Dict[int, str]
signum: Incomplete

def install_shutdown_handlers(function: SignalHandlerT, override_sigint: bool = True) -> None: ...
