"""
0. Prepare all test data in one file
1. Read test data from -testData excel-files
    (use 'excel_file_handler')
2. Define a TestClass
    eg.: class AddPosts(unitterst.TestCase)
3. Define the pre/after-conditions for this test
    pre-condition,
        user login, get access-token
    after-condition,
        user logout
4. Make test cases
    (following unittest rules, def test_XXX())
    4-1 Replace "#MARK#" with dynamic values
        (use 'replace_test_data_values_handler')
    4-2 Send requests
    4-3 Get response data
    4-4 Assert response with expected results
"""
import json
import unittest

from api.utils.api_handler import send_requests
from api.utils.config_handler import EnvData, clear_envdata
from api.utils.db_mysql_handler import handle_db
from api.utils.excel_file_handler import HandleExcel
from api.utils.my_logger import logger
from api.utils.myddt import ddt, data
from api.utils.path_handler import data_dir
from api.utils.random_phone_number_generator import get_new_phone_number
from api.utils.random_string_generator import get_random_string, get_new_name
from api.utils.replace_test_data_values_handler import replace_mark_with_value, replace_case_with_regular
from api.utils.users_handler import get_admin_user

he = HandleExcel(data_dir + "\\api_test_cases_single.xlsx", "users_add")
cases = he.read_all_data()
he.close_file()


@ddt
class TestUsersAdd(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        logger.info("======  Add-users cases starting...  ========")
        # clear EnvData variables before new test suite running
        clear_envdata()

        # get admin username/password
        user, password, phone = get_admin_user()
        # login
        req_data = {"username": user, "password": password}
        res = send_requests("POST", "/paymall_admin/authorizations/", req_data)
        # cls.token = res.json()["access"]
        setattr(EnvData, "token", res.json()["access"])

        """
        if json complex, use "jsonpath" to retrieve values
        import jsonpath
        cls.token = jsonpath.jsonpath(res.json(), "$.access")[0]
        cls.token = jsonpath.jsonpath(res.json(), "$..access")[0]
        """

    @classmethod
    def tearDownClass(cls) -> None:
        logger.info("======  Add-users cases end.  ========")
        # handle_db.close_connections()

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        delattr(EnvData, "username")
        delattr(EnvData, "phone")
        delattr(EnvData, "password")
        if hasattr(EnvData, "id"):
            delattr(EnvData, "id")

    @data(*cases)
    def test_users_add(self, case):
        logger.info("*********   Case_{}：{}   *********".format(case["case_id"], case["title"]))
        # replace #username# #password# #phone#
        setattr(EnvData, "username", get_new_name())
        setattr(EnvData, "phone", get_new_phone_number())
        setattr(EnvData, "password", get_random_string(8))
        if case["request_data"].find("#phone#") != -1 or case["request_data"].find("#username#") != -1 or case["request_data"].find("#password#") != -1:
            case = replace_case_with_regular(case)

        # send request, add user
        get_token = getattr(EnvData, "token")
        response = send_requests(case["method"], case["url"], case["request_data"], token=get_token)
        # logger.info("Response Data：{}".format(response.json()))
        # Assert - code == 0 msg == ok
        # if expected result '#id#' exist, replace the id with response result
        if case["expected"].find("#id#") != -1:
            setattr(EnvData, "id", str(response.json()['id']))
            # case = replace_mark_with_value(case, "#id#", str(response.json()['id']))
            case = replace_case_with_regular(case)
        logger.info("Expected result：{}".format(case["expected"]))

        # change expected from str to json
        expected = json.loads(case["expected"])

        # check response with expected result, and check DB if sql exist
        try:
            # self.assertEqual(response.json()["code"], expected["code"])
            # self.assertEqual(response.json()["msg"], expected["msg"])
            self.assertEqual(response.json(), expected)

            # if check_sql not None, check DB
            # if case["check_db_sql"]:
            #     logger.info("Need to check DB, with SQL: {}".format(case["check_db_sql"]))
            #     result = handle_db.get_count(case["check_db_sql"])
            #     self.assertTrue(result)
                # self.assertFalse(result)

        except AssertionError:
            logger.exception("Assertion error！")
            raise


if __name__ == '__main__':
    unittest.main()
