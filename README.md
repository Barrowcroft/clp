# clp
# A simple command line processor (clp)

The clp can be used to parse a string into a command and parameter list.
The command will then be invoked with the parameter list being passed to it.

Installation: 

`pip install git+ssh://git@github.com/Barrowcroft/clp.git`

or

`uv add git+https://git@github.com/barrowcroft/clp.git`

### Use:

Create the CLP object:

```
from clp.commandprocessor import CLP 
clp: CLP = CLP()
```

### Configuration:
The commands are defined using the CommandDef data class as follows:

CommandDef data class fields:

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

Usage:
```
from clp.commandprocessor import CLP, CommandDef

my_clp:CLP = CLP()

my_command: CommandDef = CommandDef()
my_command.name = "command"
my_command.description = "command description."
my_command.action = my_command_action
my_command.parameters = [("parameter", "Paramater description.")]
my_command.no_parse = False

clp.add(my_command)
```

Once the commands have been added they can be listed using:

`clp.list()`

### Parsing

Once the clp has been set up and commands added, a string can be passed to clp and parsed, with the appropriate 'action' being invoked.

`clp.parse(buffer_to_parse)`

