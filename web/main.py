import pytest


if __name__ == '__main__':
    pytest.main(["-s", "-v",
                 # "-m demo and test",
                 # "-m demo or test",
                 "--html=./output/report.html",
                 "--alluredir=./output/allure_dir",
                 "--rerun", "2", "--rerun-delay", "5"
                 ])

