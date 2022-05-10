global_num = 13


class OtherClass:
    def __init__(self):
        self.string = 'string'


class SomeClass:
    def __init__(self):
        self.number = 123
        self.other = OtherClass()

    def func_in_class(self, x, y=1):
        return (x+y) * global_num


def func(y, z=100):
    x = z+global_num
    return x-y


data = [1, 'string', {1, 2}, {'a': 3, 'b': 4}, 
        func, OtherClass, SomeClass, SomeClass()]

data_types = ['num', 'str', 'set', 'dict', 'func', 
        'simple_class', 'complex_class', 'object']


def get_answer_files(format):
    return list('test_{0}_{1}.txt'.format(format, data_type) 
            for data_type in data_types)


def get_test_files(format):
    return list('test_{0}.{1}'.format(data_type, format) 
            for data_type in data_types)
