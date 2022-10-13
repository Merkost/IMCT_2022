"""
Убрать соседа

Условие:
Дан массив чисел. Необходимо удалить элементы, за которыми в этом массиве следует ноль.
Формат входных данных: Входные данные содержат ряд чисел, разделенных пробелом.
Формат выходных данных: Выходные данные должны содержать преобразованный массив.
"""
import sys

massive = input().split()
indexesToDel = []

[indexesToDel.append(i) if (massive[i + 1] == "0") else massive[i] for i in range(len(massive) - 1)]

resultMassive = [x.strip() for i, x in enumerate(massive) if (i not in indexesToDel)]

print(" ".join(resultMassive))

# for i in range(1, len(massive)):
#     if massive[i] != "0":
#         resultMassive.append(massive[i - 1])


# resultMassive.append(massive[len(massive)-1])
#
# if resultMassive[len(resultMassive) - 1] == "0":
#     resultMassive.pop(len(resultMassive)-2)




# from itertools import dropwhile
#
# l = 'ABCDEFG'
# element = 'D'
#
# list(dropwhile(lambda x: x != element, massive))


# mas = ["" if massive[i + 1] and i != m == "0" else massive[i] for i in range(len(massive) - 2)]
# print(" ".join(mas) + " " + massive[len(massive) - 1])
