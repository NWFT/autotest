import pytest


if __name__ == '__main__':
    pytest.main(["-s", "-v",
                 "--html=./output/report.html",
                 "--alluredir=./output/allure_dir"])

