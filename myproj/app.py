import logging.config
from myproj.common.loggerconf import LOGGING_CONFIG

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger('MyProj')

# this import has to be after the logger import . Can this be avoided?

from myproj.pkg1.mod1inpkg1 import dummyinmod1pkg1


def init():
    print("This is from the python run in app.py")
    logger.info("This is from the python run in app.py")
    dummyinmod1pkg1()


if __name__ == '__main__':
    print("In app.py")
    logger.info("In app.py")
    init()
