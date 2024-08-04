#  Barrowcroft, 2024

from typing import Callable

#  A simple command line processor (clp).

action_type = Callable[[dict[str, str]], None]
parameter_type = tuple[str, str]  #  Parameter name and description.
command_type = tuple[
    str, action_type, list[parameter_type]
]  #  Command description, action and parameters.

class CLP:
    def __init__(self) -> None: ...
    def add(
        self,
        name: str,
        description: str,
        action: action_type,
        parameters: list[parameter_type],
        noparse: bool = False,
    ) -> None: ...
    def list(self) -> None: ...
    def parse(self, buffer: str) -> None: ...
