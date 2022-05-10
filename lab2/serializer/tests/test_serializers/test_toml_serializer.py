import unittest
from os import path, curdir

from serializer.serializers.toml_serializer import TomlSerializer
from test_data import data, get_answer_files, get_test_files


class TomlSerializerTestCase(unittest.TestCase):
    def setUp(self):
        self.test_toml_ser = TomlSerializer()
        self.path_dir = path.join(
                    path.abspath(curdir),
                    'test_answers',
                    'test_toml'
                    )
        self.data = data
        self.answer_files = get_answer_files('toml')
        self.toml_files = get_test_files('toml')

    def test_dump(self):
        for value, test_toml, answer_file in zip( 
                                    self.data[:-4],
                                    self.toml_files[:-4],
                                    self.answer_files[:-4]):
            self.test_toml_ser.dump(
                value, path.join(self.path_dir, test_toml))
            with open(path.join(
                    self.path_dir, test_toml), 'r') as rf:
                result = rf.read()
            with open(path.join(
                    self.path_dir, answer_file), 'r') as rf:
                answer = rf.read()
            self.assertEqual(result, answer)
        self.assertIsNone(
            self.test_toml_ser.dump(None, self.data[:-1])
        )

    def test_dumps(self):
        for value, answer_file in zip(self.data[:-4],
                                     self.answer_files[:-4]):
            with open(path.join(
                    self.path_dir, answer_file), 'r') as rf:
                answer = rf.read()
            self.assertEqual(
                self.test_toml_ser.dumps(value), answer
            )
        self.assertIsNone(
            self.test_toml_ser.dump(self.data[:-1], self.data[:-1])
        )

    def test_load(self):
        for value, test_toml in zip(self.data[:-4],
                                    self.toml_files[:-4]):
            self.assertEqual(
                self.test_toml_ser.load(path.join(
                    self.path_dir, test_toml)), value
            )
        func = self.test_toml_ser.load(path.join(
            self.path_dir, self.toml_files[4]),
            convert=True)
        self.assertEqual(type(func), dict)
        simple_class = self.test_toml_ser.load(path.join(
                    self.path_dir, self.toml_files[5]))
        self.assertEqual(type(simple_class), type)
        complex_class = self.test_toml_ser.load(path.join(
                    self.path_dir, self.toml_files[6]))
        self.assertTrue(hasattr(complex_class, 'func_in_class'))
        complex_object = self.test_toml_ser.load(path.join(
                    self.path_dir, self.toml_files[7]))
        self.assertEqual(complex_object.other.string, 'string')
        self.assertIsNone(self.test_toml_ser.load('incorrect_path'))

    def test_loads(self):
        for value, answer_file in zip(self.data[:-4],
                                      self.answer_files[:-4]):
            with open(path.join(
                    self.path_dir,
                    answer_file), 'r') as rf:
                data_ = rf.read()
            self.assertEqual(
                self.test_toml_ser.loads(data_), value
                    )

        def get_data():
            for data_file in self.answer_files[4:]:
                with open(path.join(
                        self.path_dir,
                        data_file), 'r') as rf:
                    data_ = rf.read()
                yield data_

        data_ = get_data()
        func = self.test_toml_ser.loads(next(data_))
        self.assertEqual(func(12), 101)
        simple_class = self.test_toml_ser.loads(next(data_))
        self.assertEqual(type(simple_class), type)
        complex_class = self.test_toml_ser.loads(next(data_))
        self.assertTrue(hasattr(complex_class, 'func_in_class'))
        complex_object = self.test_toml_ser.loads(next(data_))
        self.assertEqual(complex_object.other.string, 'string')
        self.assertIsNone(self.test_toml_ser.loads('bad_data'))


if __name__ == "__main__":
    unittest.main()
