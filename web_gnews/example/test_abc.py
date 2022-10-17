# content of test_sample.py
def inc(x):
    return x + 1


def a_test_answern():
    assert inc(3) != 5


class TestAbc():

    def setup(self):
        print("setup.....")

    def teardown(self):
        print("teardown....")

    def a_test_answer(self):
        assert inc(3) != 5

    def a_test_answer1(self):
        assert inc(3) == 5


