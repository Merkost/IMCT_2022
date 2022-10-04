"""
Индекс предыдущего вхождения

Условие:
Пусть имеется некоторый список строк. Требуется для каждой строки определить индекс предыдущего вхождения
этой строки в список. Формат входных данных Входной файл содержит n строк. Строки состоят из заглавных и строчных
букв латинского алфавита, цифр и символов пробел. Формат выходных данных Выходной файл должен содержать n целых
чисел — индексы предыдущих вхождений строк. Если строка встречается впервые требуется вывести -1.

First string
Second string
third string
4 string
5 string

"""
import sys

lis = list(map(lambda x: x.rstrip("\n"), sys.stdin.readlines()))
di = dict(map(lambda x: {x: [i] if x % 2 == 0 else False} for i, x in enumerate(lis)))
print(dict)
backwardList = lis[-1::-1]
result = ["-1"]
listLen = len(lis)
if len(lis) > 1:
    for i in range(1, listLen):
        try:
            # print(f'word: {word}, min i: {len(lis) - i}')
            result.append(listLen - 1 - backwardList.index(lis[i], listLen - i))
        except:
            result.append("-1")
print(*result)


# import sys
#
# lis = list(map(lambda x: x.rstrip("\n"), sys.stdin.readlines()))
# backwardList = lis[-1::-1]
# print("-1")
# listLen = len(lis)
# if len(lis) > 1:
#     for i in range(1, listLen):
#         try:
#             # print(f'word: {word}, min i: {len(lis) - i}')
#             print(listLen - 1 - backwardList.index(lis[i], listLen - i))
#         except:
#             print("-1")


# import sys
#
# lis = sys.stdin.readlines()
#
# for i in range(len(lis)):
#     word = input()
#     try:
#         result = len(lis) - lis[-1::-1].index(word) - 1
#     except:
#         result = -1
#     print(result)
#     lis.append(word)