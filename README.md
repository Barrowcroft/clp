# clp
# A simple command line processor (clp)

The clp can be used to parse a string into a command and parameter list.
The command will then be invoked with the parameter list being passed to it.

Installation: 

`pip install git+https://github.com/barrowcroft/clp.git`


### Use:

Create the CLP object:

```
from clp.commandprocessor import CLP 
clp: CLP = CLP()
```

Add commands that will be recognised by the CLP using the add methd:

`clp.add()`


The 'add' method has a number of parameters:

    name (str):
        The name of the command.
    description (str):
        The description of the command.
    action (action_type):
        A reference to a function that will be executed to carry out the command.
    parameters (list[parameter_type]):
        A list of names of expected parameters.

NOTE: 

The 'action_type' is a callable representing the function or method that will execute the command.

`Callable[[dict[str, str]], None]`

The 'parameter_type' is a tuple representing the parameter name and description:

`tuple[str, str]`

There is also a 'command_type' of the form:

`tuple[str, action_type, list[parameter_type], bool] `

Once the commands have been added they can be listed using:

`clp.list()`

### Parsing

Once the clp has been set up and commands added, a string can be passed to clp and parsed, with the appropriate 'action' being invoked.

`clp.parse(buffer_to_parse)`

