from conf import setting
import logging.config
def get_logger(name):
    logging.config.dictConfig(setting.LOGGING_DIC)
    my_logger= logging.getLogger(name)
    return my_logger