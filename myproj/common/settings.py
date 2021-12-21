import os
import yaml
import logging

logger = logging.getLogger(__name__)


def set_gloal_config():
    """
    This module sets a global config dict which will be used across the project.
    the config.yml is read
    :return:
    """
    global cfg
    config_filepath = os.path.join(os.getcwd(), 'myproj/common/config.yml')
    # try catch with an exception - noconfig file found
    with open(config_filepath, 'r') as ymlfile:
        fullconfigdict = yaml.safe_load(ymlfile)

    # the key used below should be derived from an env variable
    # The variable can define it in the container
    # env = os.environ['env']
    env = 'dev'

    cfg = fullconfigdict[env]

    logger.info(cfg)
