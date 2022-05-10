from serializer.serializers.factory_serializer import SerializerFactory


def gen(x):
    for i in x:
        yield i


class SuperClass:
    sup = 13


class ChildClass(SuperClass):
    child = 'hi'


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        return


def func(x, y):
    x = SuperClass().sup
    return x + y


import math
def f(x):
    return math.sin(x)


def hello(name, age):
    print("Hello, {}!I`m {}".format(name, age))


factory = SerializerFactory()
serializer = factory.get_serializer('json')
serializer.dump(f, 'test.json')
foo = serializer.load('test.json')
foo(math.pi/4)
print(foo)




