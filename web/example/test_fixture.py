import pytest


@pytest.fixture()
def ini():
    print("********Before fixture function*******")
    yield True, 100
    print("********After fixture function*******")


@pytest.fixture(scope="class")
def ini_class():
    print("********Before fixture class *******")
    yield
    print("********After fixture class *******")


@pytest.mark.usefixtures("ini")
def a_test_abc(ini):
    print("========function=========")
    print(ini)


@pytest.mark.usefixtures("ini", "ini_class")
class TestDay(object):

    # @pytest.mark.usefixtures("ini")
    def a_test_new1(self):
        print("------class method1-----")

    def a_test_new2(self):
        print("------class method2-----")

    def a_test_new3(self):
        print("------class method3-----")
