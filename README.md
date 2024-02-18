# pyftg

An interface for implementing python AI in DareFightingICE
**Note:** Version 2.0 or later is compatible with [DareFightingICE-Unity](https://github.com/TeamFightingICE/DareFightingICE-Unity). If you intend to use it with [FightingICE](https://github.com/TeamFightingICE/FightingICE), please use version 1.x instead which is also **deprecated**.

First, install `pyftg` with pip.
```
pip install pyftg
```

Initiate `Gateway` for connecting to DareFightingICE platform.
```
from pyftg.gateway import Gateway
gateway = Gateway(port=50051)
```

Construct an agent and register it to gateway and then run the game by using following code.
```
agent = KickAI()
gateway.register_ai("KickAI", agent)
gateway.run_game(["ZEN", "ZEN"], ["KickAI", "MctsAi23i"], 1)
```

After all the process are done, please also close the gateway.
```
gateway.close()
```
