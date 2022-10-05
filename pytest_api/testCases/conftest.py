
import pytest

from pytest_api.utils.config_handler import clear_envdata, conf
from pytest_api.utils.db_mysql_handler import HandleDB
from pytest_api.utils.my_logger import logger


# fixture for cases in classes
@pytest.fixture(scope="class")
def class_init_envdata():
    # log info to log-file and console
    logger.info("======  API cases starting...  ========")
    # clear EnvData variables before new test suite running
    clear_envdata()
    yield
    # log info to log-file and console
    logger.info("======  API cases ending.  ========")


# fixture for db connection and close
@pytest.fixture(scope="session", autouse=True)
def database():
    # open db
    handle_db = HandleDB(
        conf.get("mysql", "host"),
        int(conf.get("mysql", "port")),
        conf.get("mysql", "user"),
        conf.get("mysql", "password"),
        conf.get("mysql", "database")
    )
    yield handle_db
    # close connections
    handle_db.close_connections()


