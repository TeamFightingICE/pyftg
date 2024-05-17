# Examples

## File Description
- ```DisplayInfo.py``` is an example AI that utilizes screen data as input.
- ```KickAI.py``` is an example AI that only executes a single command.
- ```OneSecondAI.py``` is an example AI that utilizes multi-threading to achieve a processing time of one second.
- ```Main_PyAIvsPyAI.py``` is the script to run two instances of the Python AI and set up the game. This is when both AI are implemented using Python
- ```Main_SinglePyAI.py``` is the script to run a single instance of the Python AI, e.g. when the opposing AI is not implemented using Python.

## Instruction
- First, install our interface on implementing python AI using `pip`. (Python version >= 3.10 required)
```
pip install -r requirements.txt
```

## Instruction on using Main_PyAIvsPyAI.py
- Boot DareFightingICE with option `--pyftg-mode`.
- If both of AI are implemented in Python, modify lines 16 to 20 of `Main_PyAIvsPyAI.py`.
- The following example shows how to use KickAI as player 1 and DisplayInfo as player 2.
```
agent1 = KickAI()
agent2 = DisplayInfo()
gateway.register_ai("KickAI", agent1)
gateway.register_ai("DisplayInfo", agent2)
await gateway.run_game([character, character], ["KickAI", "DisplayInfo"], game_num)
```
- Execute `Main_PyAIvsPyAI.py` to connect to the DareFightingICE platform where `port` is the exposed port of DareFightingICE (optional).
```
python Main_PyAIvsPyAI.py --port {port}
```

## Instruction on using Main_SinglePyAI.py
- Boot DareFightingICE.
- To run a single instance of the Python AI, refer to `Main_SinglePyAI.py`.
- Execute `Main_SinglePyAI.py`, the following example shows how to use KickAI as player 1 and not select anything for player 2.
```
python Main_SinglePyAI.py --a1 KickAI
```
