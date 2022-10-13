"""
dir

Условие:
Вывести сначала все публичные атрибуты класса str в алфавитном порядке, а затем все приватные атрибуты,
тоже в алфавитном порядке, каждый с новой строки. Названия приватных методов начинаются с символа '_' (ascii 95).
"""
m = dir(str)

private = [i for i in m if (i.startswith("__"))]
public = [i for i in m if (not i.startswith("__"))]

print("\n".join(sorted(public)))
print("\n".join(sorted(private)))
