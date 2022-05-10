from os import path

from serializer.argparser.argparser import get_file
from serializer.serializers.factory_serializer import SerializerFactory


def main():
    format_, files = get_file()
    factory = SerializerFactory()
    out_ser = factory.get_serializer(format_)
    for file_ in files:
        file_name, extension = path.splitext(file_)
        if format_ != extension[1:]:
            in_ser = factory.get_serializer(extension[1:])
            obj_dict = in_ser.load(file_, convert=True)
            out_ser.dump(obj_dict, f'{file_name}.{format_}', convert=True)


if __name__ == "__main__":
    main()
