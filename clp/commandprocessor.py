"""
A simple command line processor (clp).

The command line preocessor maintains a list of known commands,
and provides facilities to list
"""

from dataclasses import dataclass
from shlex import split
from typing import Callable, Optional


@dataclass
class CommandDef:
    """
    The CommandDef data class defines each command.

    name
        The name of the command.
    description
        The description of the command.
    action
        A reference to a function that will be executed to carry out the command.
    parameters
        A list of names of expected parameters.
    no_parse
        If true, indiactes that the paramater string should not be parsed.
    """

    name: str = ""
    description: str = ""
    action: Optional[Callable[[dict[str, str]], None]] = None
    parameters: Optional[list[tuple[str, str]]] = None
    no_parse: bool = False


class CLP:
    """
    CLP

    The command line processor class.
    """

    def __init__(self) -> None:
        """__init__

        Initialises the clp.

        """
        self._commands: dict[str, CommandDef] = {}

    def add(self, command_def: CommandDef) -> None:
        """
        add

        Adds a new command to the dictionary of recognisable commands.

        Args:
            command_def (CommandDef): _desThe command to add to the dictionary.
        """
        self._commands[command_def.name] = command_def

    def list(self) -> None:
        """list

        Lists the recognisable commands.

        """

        #  Loop over entries in the recognisable commands dictionary.

        for _name, _command_def in self._commands.items():

            #  Print the command name and description.

            print(f"{_name:<20}" f"{_command_def.description}")

            #  Get the parameter list, and if its not empty
            #  loop over it printing parameter name and description.

            if _command_def.parameters:
                print(" " * 19, "Parameters:")
                for _param_name, _param_desc in _command_def.parameters:
                    print(" " * 22, f"{_param_name}: {_param_desc}")
            else:
                print(" " * 22, "Parameters: None")

    def parse(self, buffer: str) -> None:
        """parse

        Parse the string in the given buffer extracting the command and any given parameters.
        If the string is successfully parsed then the command action is invoked with a
        dictionary containing the parameters.

        Args:
            buffer (str): String buffer to prase.
        """

        #  Split the buffer into individual strings.

        _parts: list[str] = split(buffer)

        #  The first string is the command name.
        #  Check if it is in the list of recognisable commands. If not print error and return.

        _name: str = _parts[0]

        if _name not in self._commands:
            print(f"Error - command '{_name}' not recognised.")
            return

        #  The command is recognised store a reference to the command definition.

        _command = self._commands[_name]

        if _command.no_parse is not True:

            #  If there are not supposed to be parameters
            #  check that none are supplied.
            #  If not print error and return.

            if not _command.parameters and len(_parts[1:]) > 0:
                print(
                    f"Error - incorrect number of parameters for command '{_name}'"
                    + f" - none expected, {len(_parts[1:])} supplied."
                )
                return

            #  If there are supposed to be parameters
            #  check the correct number of parameters is supplied.
            #  If not print error and return.

            if _command.parameters and len(_command.parameters) != len(_parts[1:]):
                print(
                    f"Error - incorrect number of parameters for command '{_name}'"
                    + f" - {len(_command.parameters)} expected, {len(_parts[1:])} supplied."
                )
                return

            #  The command is recognised and the correct number of parameters has been supplied.
            #  Create a parameter dictionary and invoke the appropriate action.

            _parms: dict[str, str] = {}
            if _command.parameters:
                for _index, _parm in enumerate(_parts[1:]):
                    _parms[_command.parameters[_index][0]] = _parm
        else:

            #  Parameters need not be parsed so return a list
            #  of all given paramters without checking them.
            #  Assumption is that action function will parse as needed.
            #  This is to allow for the posibility that we dont know how many
            #  parameters will be passed.

            _parms: dict[str, str] = {}

            for _index, _parm in enumerate(_parts[1:]):
                _parms[str(_index)] = _parm

        if _command.action:
            _command.action(_parms)
