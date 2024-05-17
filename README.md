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
