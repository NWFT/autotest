
class TestClass(object):
    pass


setattr(TestClass, "hello", "hello world")
setattr(TestClass, "name", "Alex")

print(dict(TestClass.__dict__))

values = dict(TestClass.__dict__)
for key in values.keys():
    if not key.startswith("__"):
        delattr(TestClass, key)

print(dict(TestClass.__dict__))
