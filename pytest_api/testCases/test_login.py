import os
import pytest

from pytest_api.utils.api_handler import send_requests
from pytest_api.utils.excel_file_handler import HandleExcel
from pytest_api.utils.path_handler import data_dir
from pytest_api.utils.my_logger import logger
from pytest_api.utils.replace_test_data_values_handler import replace_mark_with_value

file_dir = os.path.join(data_dir, "api_test_cases_single.xlsx")
he = HandleExcel(file_dir, "login")
cases = he.read_all_data()
he.close_file()


@pytest.mark.usefixtures("class_init_envdata")
class TestLogin(object):

    @pytest.mark.parametrize("case", cases)
    def test_login(self, case, database):
        logger.info("*********   Case_{}：{}   *********".format(case["id"], case["title"]))
        # test steps, test data
        response = send_requests(case["method"], case["url"], case["request_data"])

        # replace the '"#refresh_token#' and '#access_token#', if needed
        if case["expected"].find("#refresh_token#") != -1:
            case = replace_mark_with_value(case, "#refresh_token#", response.json()["refresh"])
        if case["expected"].find("#access_token#") != -1:
            case = replace_mark_with_value(case, "#access_token#", response.json()["access"])
        expected = eval(case["expected"])
        logger.info("Expected result：{}".format(case["expected"]))

        try:
            # self.assertEqual(response.json()["code"], expected["code"])
            # self.assertEqual(response.json()["msg"], expected["msg"])
            assert (response.json() == expected)

            # if check_sql not None, check DB
            if case["check_db_sql"]:
                print("SQL: ", case["check_db_sql"])
                result = database.get_count(case["check_db_sql"])
                database.close_connections()
                assert result
                # self.assertFalse(result)

        except AssertionError:
            logger.exception("Assertion error！")
            raise


if __name__ == '__main__':
    pytest.main()