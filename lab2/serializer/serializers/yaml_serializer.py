from base_serializer import BaseSerializer

import yaml


class YamlSerializer(BaseSerializer):
    def dump(self, obj, file_path, convert=False):
        try:
            with open(file_path, "w") as write_file:
                if not convert:
                    obj = super().serialize_object(obj)
                yaml.safe_dump(obj, write_file, default_flow_style=False)
        except Exception:
            return None

    def dumps(self, obj):
        return yaml.safe_dump(super().serialize_object(obj), indent=4)

    def load(self, file_path, convert=False):
        try:
            with open(file_path, "r") as read_file:
                if convert:
                    return yaml.safe_load(read_file)
                return super().deserialize_object(yaml.safe_load(read_file))
        except FileNotFoundError:
            return None

    def loads(self, str_obj):
        try:
            return super().deserialize_object(yaml.safe_load(str_obj))
        except AttributeError:
            return None
