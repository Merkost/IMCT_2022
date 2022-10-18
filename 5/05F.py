import re


class Student:

    def __init__(self):
        self._name = None

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        rg = r"[ a-zA-Z]+"

        if isinstance(value, str) and re.fullmatch(rg, value):
            self._name = value
        else:
            raise ValueError


std = Student()
std.name = 123
print(std.name)
std.name = "xyixxx  z123"
print(std.name)
