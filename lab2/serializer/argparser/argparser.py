import argparse
import configparser


def get_file():
    parser = argparse.ArgumentParser(description='Serializer')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-j', '--json',
                       nargs='+', type=str,
                       help="Serialization to json")
    group.add_argument('-t', '--toml',
                       nargs='+', type=str,
                       help="Serialization to toml")
    group.add_argument('-y', '--yaml',
                       nargs='+', type=str,
                       help="Serialization to yaml")
    group.add_argument('-c', '--config',
                       nargs=1, type=str,
                       help="Get information from config file")
    args = vars(parser.parse_args())
    format_, file_ = tuple(*{arg: value for arg, value
                             in args.items() if value}.items())
    if format_ == 'config':
        config = configparser.ConfigParser()
        config.read(file_[0])
        return config['FORMAT']['serializer'], [config['FILE']['name']]
    else:
        return format_, file_
