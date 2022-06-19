import logging

logging.basicConfig(filename='logFile/Weatherlog.log',
                    filemode='w',
                    level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s')


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
