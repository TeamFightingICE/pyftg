# pyftg

```
from pyftg.gateway import Gateway
gateway = Gateway(port=50051)
```

```
gateway.load_agent(["KickAI", "KickAI"])
gateway.start_ai()
gateway.close()
```

```
agent = KickAI()
gateway.register_ai("KickAI", agent)
gateway.run_game(["ZEN", "ZEN"], ["KickAI", "MctsAi65"], 1)
gateway.close()
```
