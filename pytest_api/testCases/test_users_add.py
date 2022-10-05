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
import os
import pytest

from pytest_api.utils.api_handler import send_requests
from pytest_api.utils.config_handler import EnvData
from pytest_api.utils.excel_file_handler import HandleExcel
from pytest_api.utils.my_logger import logger
from pytest_api.utils.path_handler import data_dir
from pytest_api.utils.random_phone_number_generator import get_new_phone_number
from pytest_api.utils.random_string_generator import get_random_string, get_new_name
from pytest_api.utils.replace_test_data_values_handler import replace_case_with_regular
from pytest_api.utils.users_handler import get_admin_user

file_dir = os.path.join(data_dir, "api_test_cases_single.xlsx")
he = HandleExcel(file_dir, "users_add")
cases = he.read_all_data()
he.close_file()


# fixture for admin user login
@pytest.fixture(scope="class")
def class_admin_login():
    # get admin username/password
    user, password, phone = get_admin_user()
    # login
    req_data = {"username": user, "password": password}
    res = send_requests("POST", "/paymall_admin/authorizations/", req_data)
    # cls.token = res.json()["access"]
    setattr(EnvData, "token", res.json()["access"])


@pytest.mark.usefixtures("class_admin_login")
@pytest.mark.usefixtures("class_init_envdata")
class TestUsersAdd(object):

    @pytest.mark.parametrize("case", cases)
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
            assert response.json() == expected

            # if check_sql not None, check DB
            # if case["check_db_sql"]:
            #     logger.info("Need to check DB, with SQL: {}".format(case["check_db_sql"]))
            #     result = handle_db.get_count(case["check_db_sql"])
            #     self.assertTrue(result)
                # self.assertFalse(result)

        except AssertionError:
            logger.exception("Assertion error！")
            raise


