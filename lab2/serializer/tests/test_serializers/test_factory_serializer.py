import unittest

import sys
sys.path.append("..")
from serializer.serializers.factory_serializer import SerializerFactory


class SerializerFactoryTestCase(unittest.TestCase):
    def setUp(self):
        self.factory = SerializerFactory()

    def test_get_serializer(self):
        self.assertTrue(self.factory.get_serializer('json'))
        self.assertRaises(
            ValueError, self.factory.get_serializer, None
        )

    def test_add_serializer(self):
        self.factory.add_serializer({'SomeSerializer': None})
        self.assertEqual(
            self.factory._serializers.get('SomeSerializer'), None
        )
        self.assertRaises(
            TypeError, self.factory.add_serializer, None
        )


if __name__ == "__main__":
    unittest.main()
