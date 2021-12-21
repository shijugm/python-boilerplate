from myproj.common.settings import set_gloal_config
from myproj.common.db_connections import get_connection
import logging

logger = logging.getLogger(__name__)


def dummyinmod1pkg1():
    print("in dummyinmod1pkg1 ")
    logger.info("dummyinmod1pkg1")
    set_gloal_config()
    get_connection()
