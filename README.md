# pyftg

An interface for implementing python AI in DareFightingICE

First, install `pyftg` with pip.
```sh
pip install pyftg
```

Initiate `Gateway` for connecting to DareFightingICE platform.
```py
from pyftg.socket.aio.gateway import Gateway
gateway = Gateway(port=31415)
```

Construct an agent and register it to gateway and then run the game by using following code.
```py
agent1 = KickAI()
agent2 = DisplayInfo()
gateway.register_ai("KickAI", agent1)
gateway.register_ai("DisplayInfo", agent2)
await gateway.run_game(["ZEN", "ZEN"], ["KickAI", "DisplayInfo"], game_num)
```

After all the process are done, please also close the gateway.
```py
await gateway.close()
```

Please refer to the examples provided in the `examples` directory for more information.

# For developer only
Please refer to this [link](https://twine.readthedocs.io/en/stable/).

1. Increase version number in pyproject.toml

1. Build project
```sh
python -m build
```
if the above command doesn't work due to ```no module named build``` error, install ```build``` library then try again
```sh
pip install build
```
3. Push project to pypi
```sh
twine upload dist/*
```
