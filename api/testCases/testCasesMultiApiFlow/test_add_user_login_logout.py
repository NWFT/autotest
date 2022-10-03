
"""
1. user add (no need to check DB)
    username/password
2. login
    new username/password
3. list users with new user
    send list users, with token after login
4. logout
"""
import json
import os
import unittest

from api.utils.api_handler import send_requests
from api.utils.config_handler import clear_envdata, EnvData
from api.utils.excel_file_handler import HandleExcel
from api.utils.my_logger import logger
from api.utils.myddt import ddt, data
from api.utils.path_handler import data_dir
from api.utils.random_phone_number_generator import get_new_phone_number
from api.utils.random_string_generator import get_new_name, get_random_string
from api.utils.replace_test_data_values_handler import replace_case_with_regular, replace_mark_with_value
from api.utils.users_handler import get_admin_user

file_dir = os.path.join(data_dir, "api_test_cases_multi_flow.xlsx")
he = HandleExcel(file_dir, "users")
cases = he.read_all_data()
he.close_file()


@ddt
class TestUserFlow(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # admin user login
        # save admin's token
        logger.info("======  Multi API user flow cases starting...  ========")
        # clear EnvData variables before new test suite running
        clear_envdata()

        # get admin username/password
        user, password, phone = get_admin_user()
        # login
        req_data = {"username": user, "password": password}
        res = send_requests("POST", "/paymall_admin/authorizations/", req_data)
        # cls.token = res.json()["access"]
        setattr(EnvData, "token_admin", res.json()["access"])

        """
        if json complex, use "jsonpath" to retrieve values
        import jsonpath
        cls.token = jsonpath.jsonpath(res.json(), "$.access")[0]
        cls.token = jsonpath.jsonpath(res.json(), "$..access")[0]
        """

        # new user's username, password, phone number
        setattr(EnvData, "username", get_new_name())
        setattr(EnvData, "phone", get_new_phone_number())
        setattr(EnvData, "password", get_random_string(8))

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @data(*cases)
    def test_user_flow(self, case):
        logger.info("*********   Case_{}：{}   *********".format(case["case_id"], case["title"]))
        # replace marks
        case = replace_case_with_regular(case)

        # use admin_token for the first request,
        # then, use new_user_token for the following operation
        if hasattr(EnvData, "token_admin"):
            get_token = getattr(EnvData, "token_admin")
            # add the new user, case_id is 1
            response = send_requests(case["method"], case["url"], case["request_data"], token=get_token)
            # get the response id, replace expected result
            if case["expected"].find("#id#") != -1:
                setattr(EnvData, "id", str(response.json()['id']))
                case = replace_case_with_regular(case)

            logger.info("Expected result：{}".format(case["expected"]))
            # change expected from str to json
            expected = json.loads(case["expected"])

            # check response with expected result, and check DB if sql exist
            try:
                self.assertEqual(response.json(), expected)
            except AssertionError:
                logger.exception("Assertion error！")
                raise

            # delete "token_admin", next steps will not use admin_token
            delattr(EnvData, "token_admin")

        else:
            # send requests
            if hasattr(EnvData, "token"):
                get_token = getattr(EnvData, "token")
                if case["request_data"]:
                    response = send_requests(case["method"], case["url"], case["request_data"], token=get_token)
                else:
                    response = send_requests(case["method"], case["url"], token=get_token)
            else:
                if case["request_data"]:
                    response = send_requests(case["method"], case["url"], case["request_data"])
                else:
                    response = send_requests(case["method"], case["url"])

            # compare result
            # replace the '"#refresh_token#' and '#access_token#', if needed
            if case["expected"].find("#refresh_token#") != -1:
                case = replace_mark_with_value(case, "#refresh_token#", response.json()["refresh"])
            if case["expected"].find("#access_token#") != -1:
                case = replace_mark_with_value(case, "#access_token#", response.json()["access"])
                setattr(EnvData, "token", response.json()["access"])

            if case["expected"].find("#count#") != -1:
                case = replace_mark_with_value(case, "#count#", str(response.json()["count"]))

            expected = eval(case["expected"])
            logger.info("Expected result：{}".format(case["expected"]))

            try:
                self.assertEqual(response.json(), expected)
            except AssertionError:
                logger.exception("Assertion error！")
                raise



