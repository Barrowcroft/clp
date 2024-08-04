#  Barrowcroft, 2024

from shlex import split
from typing import Callable

#  A simple command line processor (clp).

action_type = Callable[[dict[str, str]], None]
parameter_type = tuple[str, str]  #  Parameter name and description.
command_type = tuple[
    str, action_type, list[parameter_type], bool
]  #  Command description, action and parameters.


class CLP:
    def __init__(self) -> None:
        """__init__

        Initialises the clp.

        """
        self._commands: dict[str, command_type] = {}

    def add(
        self,
        name: str,
        description: str,
        action: action_type,
        parameters: list[parameter_type],
        noparse: bool = False,
    ) -> None:
        """add

        Adds a new command to the dictionary of recognisable commands.

        Args:
            name (str):
                The name of the command.
            description (str):
                The description of the command.
            action (action_type):
                A reference to a function that will be executed to carry out the command.
            parameters (list[parameter_type]):
                A list of names of expected parameters.
        """
        self._commands[name] = (description, action, parameters, noparse)

    def list(self) -> None:
        """list

        Lists the recognisable commands.

        """

        #  Loop over entries in the recognisable commands dictionary.

        for _command in sorted(self._commands):

            #  Print the command name and description.

            _command_description: str = self._commands[_command][0]
            print(f"{_command:<10}{_command_description}")

            #  Get the parameter list, and if its not empty
            #  loop over it printing parameter name and description.

            _command_parameters: list[parameter_type] = self._commands[_command][2]

            if _command_parameters != []:
                print(f"{' ':<10}(parameters)")

                for _param in _command_parameters:
                    print(f"{' ':<10}{_param[0]}, {_param[1]}")

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

        #  The command is recognised store a reference to the action and parameter list.

        _action: action_type = self._commands[_name][1]
        _parameters: list[parameter_type] = self._commands[_name][2]
        _noparse: bool = self._commands[_name][3]

        if _noparse is not True:

            #  Check the correct number of parameters is supplied.
            #  If not print error and return.

            if len(_parameters) != len(_parts[1:]):
                print(
                    f"Error - incorrect number of parameters for command '{_name}' - {len(_parameters)} expected, {len(_parts[1:])} supplied."
                )
                return

            #  The command is recognised and the correct number of parameters has been supplied.
            #  Create a parameter dictionary and invoke the appropriate action.

            _parms: dict[str, str] = {}

            for _index, _parm in enumerate(_parameters):
                _parms[_parm[0]] = _parts[_index + 1]

        else:

            #  Parameters need not be parsed so return a list of all given paramters without checking them.
            #  Assumption is that action function will parse as needed.

            _parms: dict[str, str] = {}

            for _index, _parm in enumerate(_parts[1:]):
                _parms[str(_index)] = _parts[_index + 1]

        _action(_parms)
