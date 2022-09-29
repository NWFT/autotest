import unittest

from api.utils.api_handler import send_requests
from api.utils.excel_file_handler import HandleExcel
from api.utils.myddt import ddt, data
from api.utils.path_handler import data_dir
from api.utils.my_logger import logger

he = HandleExcel(data_dir + "\\api_test_cases_single.xlsx", "register")
cases = he.read_all_data()
he.close_file()


@ddt
class TestRegister(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        logger.info("======  Register cases starting...  ========")

    @classmethod
    def tearDownClass(cls) -> None:
        logger.info("======  Register cases end.  ========")

    @data(*cases)
    def test_register(self, case):
        logger.info("*********   Case_{}：{}   *********".format(case["id"], case["title"]))
        expected = eval(case["expected"])
        # test steps, test data
        response = send_requests(case["method"], case["url"], case["request_data"])
        # Assert - code == 0 msg == ok
        logger.info("Expected result：{}".format(case["expected"]))
        try:
            # self.assertEqual(response.json()["code"], expected["code"])
            # self.assertEqual(response.json()["msg"], expected["msg"])
            self.assertEqual(response.json(), expected)
        except AssertionError:
            logger.exception("Assertion error！")


if __name__ == '__main__':
    unittest.main()