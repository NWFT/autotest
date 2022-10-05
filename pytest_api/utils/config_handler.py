from configparser import ConfigParser
import os

from pytest_api.utils.path_handler import conf_dir


class EnvData(object):
    """
    For Environment values during test cases running.
    eg.,
    setattr(EnvData, "token", "XXX")
    getattr(EnvData, "token")
    """
    pass


class HandleConfig(ConfigParser):

    def __init__(self, file_dir):
        super().__init__()
        self.read(file_dir, encoding="utf-8")


def clear_envdata():
    values = dict(EnvData.__dict__)
    for key in values.keys():
        if not key.startswith("__"):
            delattr(EnvData, key)


file_path = os.path.join(conf_dir, "conf.ini")
conf = HandleConfig(file_path)

if __name__ == '__main__':
    print(conf.get("log", "name"))
