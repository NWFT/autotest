import os
import unittest

from api.utils.api_handler import send_requests
from api.utils.db_mysql_handler import handle_db
from api.utils.excel_file_handler import HandleExcel
from api.utils.myddt import ddt, data
from api.utils.path_handler import data_dir
from api.utils.my_logger import logger
from api.utils.replace_test_data_values_handler import replace_mark_with_value

file_dir = os.path.join(data_dir, "api_test_cases_single.xlsx")
he = HandleExcel(file_dir, "login")
cases = he.read_all_data()
he.close_file()


@ddt
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        logger.info("======  Login cases starting...  ========")

    @classmethod
    def tearDownClass(cls) -> None:
        logger.info("======  Login cases end.  ========")

    @data(*cases)
    def test_login(self, case):
        logger.info("*********   Case_{}：{}   *********".format(case["id"], case["title"]))
        # test steps, test data
        response = send_requests(case["method"], case["url"], case["request_data"])
        # Assert - code == 0 msg == ok

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
            self.assertEqual(response.json(), expected)

            # if check_sql not None, check DB
            if case["check_db_sql"]:
                print("SQL: ", case["check_db_sql"])
                result = handle_db.get_count(case["check_db_sql"])
                handle_db.close_connections()
                self.assertTrue(result)
                # self.assertFalse(result)

        except AssertionError:
            logger.exception("Assertion error！")
            raise


if __name__ == '__main__':
    unittest.main()