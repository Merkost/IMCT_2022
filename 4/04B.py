"""

Норма L1

Условие:
Дан вектор произвольной размерности. Необходимо посчитать так называемую норму L1 для этого вектора. Норма
L1 — это сумма абсолютных величин компонент вектора (абсолютная величина вычисляется функцией abs). Формат входных
данных Входные данные содержат целые числа — компоненты вектора, записанные в одной строке через пробел. Формат
выходных данных Выходные данные должны содержать одно целое число — норму L1 этого вектора.
"""

print(sum([abs(i) for i in map(int, input().split())]))