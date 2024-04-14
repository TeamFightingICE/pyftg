# pyftg

An interface for implementing python AI in DareFightingICE

**Note:** Version 2.0 is the latest version compatible with the legacy [FightingICE](https://github.com/TeamFightingICE/FightingICE). Version 2.1 and later will only support [DareFightingICE-Unity](https://github.com/TeamFightingICE/DareFightingICE-Unity).

First, install `pyftg` with pip.
```
pip install pyftg
```

Initiate `Gateway` for connecting to DareFightingICE platform.
```
from pyftg.utils.gateway import get_async_gateway
gateway = get_async_gateway(port=50051)
```

Construct an agent and register it to gateway and then run the game by using following code.
```
agent1 = KickAI()
agent2 = DisplayInfo()
gateway.register_ai("KickAI", agent1)
gateway.register_ai("DisplayInfo", agent2)
await gateway.run_game(["ZEN", "ZEN"], ["KickAI", "DisplayInfo"], game_num)
```

After all the process are done, please also close the gateway.
```
await gateway.close()
```

Please refer to the examples provided in the `examples` directory for more information.
