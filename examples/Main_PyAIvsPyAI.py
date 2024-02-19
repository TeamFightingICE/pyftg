import argparse
import logging

from DisplayInfo import DisplayInfo
from KickAI import KickAI
from pyftg import Gateway


def start_game(port: int):
    gateway = Gateway(port=port)
    character = 'ZEN'
    game_num = 1
    agent1 = KickAI()
    agent2 = DisplayInfo()
    gateway.register_ai("KickAI", agent1)
    gateway.register_ai("DisplayInfo", agent2)
    gateway.run_game([character, character], ["KickAI", "DisplayInfo"], game_num)
    gateway.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=50051, type=int, help='Port used by DareFightingICE')
    args = parser.parse_args()
    logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', level=logging.DEBUG)
    start_game(args.port)
