'''
This is the config file of the program
set various static varibles
'''

import logging

OUTPUT_DIR = 'outputs/'
SRC_FILE = OUTPUT_DIR + 'fx.csv'
STRAT_OUT_FILE = OUTPUT_DIR + 'movingAverage.csv'

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)
# create formatter
LOG_DATEFMT = '%Y-%m-%d %H:%M:%S'
LOG_FORMAT = ('\n[%(levelname)s/%(name)s:%(lineno)d] %(asctime)s ' +
              '(%(processName)s/%(threadName)s)\n> %(message)s')
FORMATTER = logging.Formatter(LOG_FORMAT, datefmt=LOG_DATEFMT)
FH = logging.FileHandler('trade.log')  # create file handler
FH.setLevel(logging.DEBUG)  # set handler level to debug
FH.setFormatter(FORMATTER)  # add formatter to fh
LOGGER.addHandler(FH)  # add file handler to logger
