
import pytest


if __name__ == '__main__':
    pytest.main(["-s", "-v",
                 # "-m", "",
                 "--html=./output/reports/report.html",
                 "--alluredir=./output/allure_dir"])
