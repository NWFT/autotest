from configparser import ConfigParser
import os

from api.utils.path_handler import conf_dir


class HandleConfig(ConfigParser):

    def __init__(self, file_dir):
        super().__init__()
        self.read(file_dir, encoding="utf-8")


file_path = os.path.join(conf_dir, "conf.ini")
conf = HandleConfig(file_path)

if __name__ == '__main__':
    print(conf.get("log", "name"))
