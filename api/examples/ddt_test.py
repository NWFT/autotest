import unittest

from api.utils.myddt import ddt, data


@ddt
class TestSomething(unittest.TestCase):
    @data(1,2,3)
    def test_print_something(self, num):
        print(num, " ABCDEFG")


if __name__ == '__main__':
    unittest.main()