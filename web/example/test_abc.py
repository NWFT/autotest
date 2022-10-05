# content of test_sample.py
def inc(x):
    return x + 1


def test_answern():
    assert inc(3) != 5


class TestAbc():

    def setup(self):
        print("setup.....")

    def teardown(self):
        print("teardown....")

    def test_answer(self):
        assert inc(3) != 5

    def test_answer1(self):
        assert inc(3) == 5


