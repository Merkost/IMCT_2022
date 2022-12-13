"""
dir*

Условие:
То же для произвольного встроенного класса (Вывести сначала все публичные атрибуты класса в алфавитном порядке,
а затем все приватные атрибуты, тоже в алфавитном порядке, каждый с новой строки.)
"""

cls = input()
m = dir(eval(cls))

private = [i for i in m if (i.startswith("__"))]
public = [i for i in m if (not i.startswith("__"))]

print("\n".join(sorted(public)))
print("\n".join(sorted(private)))
