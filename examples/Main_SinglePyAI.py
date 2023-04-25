import logging
import argparse
from pyftg import Gateway

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=50051, type=int, help='Port used by DareFightingICE')
    parser.add_argument('--a1', default=None, type=str, help='The AI name to use for player 1')
    parser.add_argument('--a2', default=None, type=str, help='The AI name to use for player 2')
    args = parser.parse_args()
    logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', level=logging.DEBUG)
    gateway = Gateway(port=args.port)
    gateway.load_agent([args.a1, args.a2])
    gateway.start_ai()
    gateway.close()
