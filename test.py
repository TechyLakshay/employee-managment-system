import logging


logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(levelname)s: %(message)s',
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.INFO)
age = 22

logging.debug("The value of age is %d", age)