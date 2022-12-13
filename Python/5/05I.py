from __future__ import annotations
import inspect
import typing
from pydoc import locate
import sys


def return_type(f):
    try:
        return typing.get_type_hints(f).get('return', None)
    except TypeError:
        return None


def type_check(value, annotation):
    if isinstance(annotation, type):
        return isinstance(value, annotation)
    elif annotation == typing.T or annotation == typing.Any:
        return True
    elif isinstance(annotation, typing._GenericAlias):
        if annotation.__origin__ == list:
            if not isinstance(value, list):
                return False
            inner_annotation = annotation.__args__[0]
            return all(type_check(val, inner_annotation) for val in value)


def check_types(f):
    isclass = inspect.isclass(f)
    clsname = f.__name__
    if isclass:
        for name, method in inspect.getmembers(f):
            ismethod = inspect.ismethod(method)
            isfunc = inspect.isfunction(method)
            isbuiltin = inspect.isbuiltin(method)
            if (not ismethod and not isfunc) or isbuiltin:
                print(f"Decorating function class {name}, func {method}")
                return func_decorator(f)
            else:
                print(f"Method {method} from {name} not included to decor")
                setattr(f, name, func_decorator(method))
                return f
    else:
        print("Decorating function %s" % clsname)
        return func_decorator(f)
        # setattr(f, name, func_decorator(method))
        # # func_decorator(f)
    # return f


def func_decorator(f, isClass: bool = False):
    def wrapper(*args, **kwargs):
        cl = inspect.getclosurevars(f).globals
        sig = inspect.signature(f)
        vars = ', '.join('{}={}'.format(*pair) for pair in zip(sig.parameters, args))
        params = {k: v for k, v in zip(sig.parameters, args)}
        # print('wrapped call to {}({})'.format(func_name, params))
        for key, value in sig.parameters.items():
            # print(f.__qualname__)
            name = str(value.annotation)
            parameter = params[key]
            parameter_type = type(parameter)
            # if (parameter_type is list):
            #     type_hints = typing.get_type_hints(f)
            #     parameter_type_name = str(typing.get_args(type_hints[key])[1])
            # else:
            #     parameter_type_name = parameter_type.__name__

            # if not isinstance(value, annotations[name]):
            # loc = locate(value.annotation)
            # ev = eval(value.annotation)
            # print(value.annotation)
            # print(value.name)
            if (isClass):
                attr = getattr(sys.modules[__name__], value.annotation)
            types = value.annotation.split(" | ")
            # if not isinstance(locate(value.annotation), parameter_type):
            #     print("not")
            print(f.__annotations__['return'])
            check = [type_check(parameter, locate(i)) for i in types]
            if not any(x for x in check if x is True):
                raise TypeCheckError(key)
        name = f.__qualname__
        name = f.__name__
        returned = f(*args)
        rettype = return_type(f)


        res = sig.return_annotation
        evaluationName = eval(res)
        loc = locate(sig.return_annotation)
        check = [type_check(returned, locate(i)) for i in sig.return_annotation.split(" | ")]
        if not any(x for x in check if x is True):
            raise TypeCheckError("return")
        # returned_type = type()
        # if (returned_type is list):
        #     type_hints = typing.get_type_hints(f)
        #     parameter_type_name = str(typing.get_args(type_hints["return"])[1])
        # else:
        #     parameter_type_name = returned_type.__name__
        # if parameter_type_name not in sig.return_annotation.split(" | "):
        #     raise TypeCheckError("return")
        # if parameter_type_name == f.__qualname__.split(".")[0]:
        #     ret = f(*args)
        #     return ret

        ret = f(*args, **kwargs)
        return ret

    return wrapper


class TypeCheckError(Exception):
    name: str

    def __init__(self: TypeCheckError, name):
        # Call the base class constructor with the parameters it needs
        super().__init__()

        self.name = name


@check_types
def pow(x: int | list[int], p: int) -> int | list[int]:
    if isinstance(x, list):
        return [i ** p for i in x]

    return x ** p


print(type_check([0], typing.List[int]))
try:

    # print(pow(2, 2))

    print(*pow([1, 2, 3], 3))

    print(*pow((1, 2, 3), 3))

except TypeCheckError as e:

    print(f'Failed {e.name}')


# def check_types(f):
#     def wrapper(*args):
#         func_name = f.__name__
#         sig = inspect.signature(f)
#         vars = ', '.join('{}={}'.format(*pair) for pair in zip(sig.parameters, args))
#         params={k:v for k,v in zip(sig.parameters, args)}
#         print('wrapped call to {}({})'.format(func_name, params))
#         for key, value in sig.parameters.items():
#             parameter = params[key]
#             parameter_type = type(parameter)
#             if value.annotation != parameter_type:
#                 raise TypeCheckError(key)
#             msg='call to {}({}): {} failed {})'.format(func_name, vars, key, value.annotation.__name__)
#             assert value.annotation(params[key]), msg
#         ret = f(*args)
#         print('  returning {} with annotation: "{}"'.format(ret, sig.return_annotation))
#         return ret
#     return wrapper
