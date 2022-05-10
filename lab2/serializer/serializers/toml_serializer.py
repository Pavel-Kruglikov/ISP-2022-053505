import toml

from base_serializer import BaseSerializer


class TomlSerializer(BaseSerializer):
    def dump(self, obj, file_path, convert=False):
        try:
            with open(file_path, "w") as write_file:
                if not convert:
                    obj = super().serialize_object(obj)
                toml.dump(obj, write_file)
        except Exception:
            return None

    def dumps(self, obj):
        return toml.dumps(super().serialize_object(obj))

    def load(self, file_path, convert=False):
        try:
            with open(file_path, "r") as read_file:
                if convert:
                    return toml.load(read_file)
                return super().deserialize_object(toml.load(read_file))
        except FileNotFoundError:
            return None

    def loads(self, str_obj):
        try:
            return super().deserialize_object(toml.loads(str_obj))
        except Exception:
            return None
