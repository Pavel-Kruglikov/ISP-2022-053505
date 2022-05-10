from json_serializer import JsonSerializer
from toml_serializer import TomlSerializer
from yaml_serializer import YamlSerializer


class SerializerFactory:
    def __init__(self):
        self._serializers = {'json': JsonSerializer,
                             'toml': TomlSerializer,
                             'yaml': YamlSerializer}

    def get_serializer(self, format_):
        serializer = self._serializers.get(format_, None)
        if serializer is None:
            raise ValueError(format_)
        return serializer()

    def add_serializer(self, serializer):
        try:
            self._serializers.update(serializer)
        except TypeError:
            raise TypeError(serializer)
