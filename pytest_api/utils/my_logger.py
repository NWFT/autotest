import logging
import os

from pytest_api.utils.config_handler import conf
from pytest_api.utils.path_handler import logs_dir


class MyLogger(logging.Logger):

    def __init__(self, file=None):
        # set LOG lever, output, formatter
        # super().__init__(name,level)
        super().__init__(conf.get("log", "name"), conf.get("log", "level"))

        # log formatter
        fmt = '%(asctime)s %(name)s %(levelname)s %(filename)s-%(lineno)d line：%(message)s'
        formatter = logging.Formatter(fmt)

        # output to console
        handle1 = logging.StreamHandler()
        handle1.setFormatter(formatter)
        self.addHandler(handle1)

        # output to file if any
        if file:
            # 文件渠道
            handle2 = logging.FileHandler(file, encoding="utf-8")
            handle2.setFormatter(formatter)
            self.addHandler(handle2)


# a setting in conf.ini, to control write to file or not
# -config/conf.ini
if conf.getboolean("log", "file_ok"):
    file_name = os.path.join(logs_dir, conf.get("log", "file_name"))
else:
    file_name = None

logger = MyLogger(file_name)


if __name__ == '__main__':
    logger.info(" Test in my_logger module.")