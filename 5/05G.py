from __future__ import annotations
from collections.abc import Callable
from typing import Any, Generic, TypeVar

C = TypeVar('C')


class Property(Generic[C]):

    def __init__(self, getter: Callable[[C], Any] | None = None,
                 setter: Callable[[C, Any], None] | None = None,
                 deleter: Callable[[C], None] | None = None,
                 doc: str | None = None,
                 default_value: list[Any] | None = None):
        '''Property decorator, supporting getting, setting, deleting handled property.

    Generic:

        C: the class property is set up for

    Arguments:

        getter: member function that handles getting the value
        setter: member function that handles setting the value
        deleters: member function that handles deleting the value
        doc: general documentation for the property
        default_value: if setter is not None calls it with `default_value` on object initialization'''
        self.fget = getter
        self.fset = setter
        self.fdel = deleter
        self.def_val = default_value
        if doc is None and getter is not None:
            doc = getter.__doc__
        self.doc = doc
        # if setter is not None:
        #     self.fset(C,  default_value)

        self._name = ''

    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError(f'Cannot read {self._name}')
        return self.fget(obj)
    #
    # def __set__(self, obj, value):
    #     if self.fset is None:
    #         raise AttributeError(f'Cannot set {self._name}')
    #     self.fset(obj, value)
    #
    # def __delete__(self, obj):
    #     if self.fdel is None:
    #         raise AttributeError(f"Cannot delete {self._name}")
    #     self.fdel(obj)

    def getter(self, getter: Callable[[C], Any]) -> Property[C]:
        '''Adds getter to the property

        Arguments:
            getter: member function that handles getting the value

        Returns:
            A copy of Property with updated getter value'''

        # prop = type(self)(getter, self.fset, self.fdel, self.__doc__)
        # prop._name = self._name
        # return prop

        self._getter = getter
        return self

        # return Property(getter, self._setter, self._deleter, self._doc, self._default_value)

    def setter(self, setter: Callable[[C, Any], None] | None = None, default_value: Any | None = None) -> Property[C] | Callable[[ Callable[[C, Any], None]], Property[C]]:
        '''Adds setter to the property

        Arguments:
            setter: member function that handles setting the value
            default_value: a value that is passed to `setter` on object initialization

        Returns:
            If `setter` is None returns a shorthand decorator function with set `default_value`.
            If `setter` is not None returns a copy of Property with updated setter and default_value arguments'''

        # prop = type(self)(self.fget, setter, self.fset, self.__doc__, default_value)
        # prop._name = self._name
        # return prop

        if setter is not None:
            self.fset = setter
            self.def_val = default_value
            return self
            # return Property(self.getter, setter, self._deleter, self._doc, default_value)

        # def foo(default_value):
        #     def wrapped(C, any):
        #         set
        #     return wrapped
        # return foo

    def deleter(self, deleter: Callable[[C], None]) -> Property:
        '''Adds deleter to the property

        Arguments:
            deleter: member function that handles deleting the value

        Returns:
            A copy of Property with updated deleter value'''
        self.fdel = deleter
        return self
        # return Property(self.getter, self._setter, deleter, self._doc, self._default_value)


class Person:

    @Property
    def name(self) -> str | None:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name


p1 = Person()
p2 = Person()
# p2.name = 'Petya'
print(p1.name)
print(p2.name)
