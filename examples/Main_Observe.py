import logging
import argparse
from pyftg import ObserverGateway
from Collector import Collector

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=50051, type=int, help='Port used by DareFightingICE')
    args = parser.parse_args()
    logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', level=logging.DEBUG)
    collector = Collector()
    gateway = ObserverGateway(handler=collector, port=args.port)
    logging.info('Observer is started.')
    gateway.start()
    gateway.close()
