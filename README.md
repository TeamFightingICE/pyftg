# pyftg

An interface for implementing python AI in DareFightingICE

**Note:** Version 2.0 is the latest version compatible with the legacy [FightingICE](https://github.com/TeamFightingICE/FightingICE). Future versions will only support [DareFightingICE-Unity](https://github.com/TeamFightingICE/DareFightingICE-Unity).

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
