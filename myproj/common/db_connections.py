import myproj.common.settings as settings
import logging

logger = logging.getLogger(__name__)


def get_connection():
    """
    use the config yaml to create a connection
    :return: connection object
    """
    dbname = settings.cfg['devdb']['dbname']
    logger.info(f"dbname  = {dbname}")
    print(dbname)

    # conn = database specific connection
    # return conn
