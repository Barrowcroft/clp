# pylint: skip-file

from dataclasses import dataclass
from typing import Callable, Dict, List, Optional, Tuple

@dataclass
class CommandDef:
    name: str
    description: str
    action: Optional[Callable[[Dict[str, str]], None]]
    parameters: Optional[List[Tuple[str, str]]]
    no_parse: bool

class CLP:
    _commands: Dict[str, CommandDef]

    def __init__(self) -> None: ...
    def add(self, command_def: CommandDef) -> None: ...
    def list(self) -> None: ...
    def parse(self, buffer: str) -> None: ...
