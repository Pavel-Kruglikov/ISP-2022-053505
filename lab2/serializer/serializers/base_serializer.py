import inspect
import io
import builtins
import types

from abc import ABC, abstractmethod


class BaseSerializer(ABC):
    @abstractmethod
    def dump(self, obj, file_path, convert=False):
        pass

    @abstractmethod
    def dumps(self, obj):
        pass

    @abstractmethod
    def load(self, file_path, convert=False):
        pass

    @abstractmethod
    def loads(self, str_obj):
        pass

    @classmethod
    def serialize_object(cls, obj):
        template = {
            'representation': repr(obj),
            'name': cls._get_name(obj),
            'type': cls._get_type(obj),
            'base': cls._get_base(obj),
            'class_attr': cls._get_class_attr(obj),#получение атрибутов класса
            'func_param': cls._get_func_params(obj),#получение параметров функции
            
        }
        return {key : value for key, value in template.items() if value}

    
    @classmethod
    def save_function(cls, obj):
        copy_code = cls._copy_code(obj)
        copy_func = cls._copy_func(obj)
        from pprint import pprint
        pprint (copy_code)
        pprint(copy_func)
        fglobals = {key: cls.serialize_object(value) for key, value 
            in copy_func['globals'].items() if key in copy_code['names']}
        copy_func.update({'globals': fglobals})
        func_dict = {'CodeType': copy_code, 'FunctionType': copy_func} 
        return func_dict

    @classmethod
    def get_function(cls, func_dict):
        for key, value in func_dict['FunctionType']['globals'].items():
            func_dict['FunctionType']['globals'][key] = cls.deserialize_object(value)
        func_dict['FunctionType']['globals'].update({'__builtins__': builtins})
        func_code = types.CodeType(*func_dict['CodeType'].values())
        func_params = list(func_dict['FunctionType'].values())
        func = types.FunctionType(func_code, *func_params[:-2])
        func.__dict__.update(func_params[4]) 
        if func_params[5] is not None:
            func.__kwdefaults__ = func_params[5]
        return func
    @classmethod
    def _get_base(cls, obj):
        try:
            base = obj.__base__
            return cls.serialize_object(base) if base is not object else ()
        except:
            return None

    @classmethod 
    def get_type(cls, obj):
        if isinstance(obj, (types.FunctionType, types.MethodType)):
            return cls.save_function(obj)
        else:
            return obj

   

    @classmethod
    def _get_class_attr(cls, obj):
        base_types = (int, float, bool, str, list, tuple, dict, set)
        if isinstance(obj, (*base_types, types.FunctionType, types.MethodType)):
            return None
        try: 
            all_attr = {**{key: value for key, value in inspect.getmembers(obj, 
                        predicate=inspect.isfunction)}, 
                        **{key: value for key, value in inspect.getmembers(obj) 
                        if not (key.startswith('__') and key.endswith('__'))}}
            for key, value in all_attr.items():
                if not isinstance(value, base_types):
                    all_attr[key] = cls.serialize_object(value)
            return all_attr
        except AttributeError:
            return None

    @staticmethod
    def _copy_code(obj):
        keys = [
            "argcount", "posonlyargcount", "kwonlyargcount", 
            "nlocals", "stacksize", "flags", "code", "consts",
            "names", "varnames", "filename", "name", "firstlineno",
            "lnotab", "freevars", "cellvars"
        ]
        values = [getattr(obj.__code__, 'co_' + key) for key in keys]
        return dict(zip(keys, values))

    @staticmethod
    def _copy_func(obj):
        keys = [
            "globals", "name", "defaults", 
            "closure", "dict", "kwdefaults"
        ]
        values = [getattr(obj, f'__{key}__') for key in keys]
        return dict(zip(keys, values))

    @staticmethod
    def _get_name(obj):
        try:
            return obj.__name__
        except:
            return None

    @staticmethod
    def _get_type(obj):
        return str(type(obj)).split('\'')[1]#разбиваем строку по указанному разделителю и возвращаем список строк

    @staticmethod
    def _get_func_params(obj):
        try:
            full_args = inspect.getfullargspec(obj)
            args_spec = (full_args.args, full_args.varargs, full_args.varkw, 
                        full_args.defaults, full_args.kwonlyargs, 
                        full_args.kwonlydefaults, full_args.annotations)
            return dict(zip(full_args._fields, args_spec))
        except:
            return None
