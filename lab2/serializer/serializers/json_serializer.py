import json

from base_serializer import BaseSerializer


class JsonSerializer(BaseSerializer):

    def dump(self, obj, file_path, indent=4, convert=False):
        try:
            with open(file_path, "w") as write_file:
                if not convert:
                    obj = super().serialize_object(obj)
                json.dump(obj, write_file, indent=indent)
        except TypeError:
            return None

    def dumps(self, obj, indent=4):
        return json.dumps(super().serialize_object(obj), indent=indent)

    def load(self, file_path, convert=False):
        try:
            with open(file_path, "r") as read_file:
                if convert:
                    return json.load(read_file)
                return super().deserialize_object(json.load(read_file))
        except FileNotFoundError:
            return None

    def loads(self, str_obj):
        try:
            return super().deserialize_object(json.loads(str_obj))
        except Exception:
            return None
