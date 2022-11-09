"""

Средние взвешенные

Условие Требуется написать программу, которая вычисляет средние арифметическое, гармоническое и геометрическое
заданного вариационного ряда. При решении задачи необходимо использовать библиотеку numpy.
Формат входного файла
Входные данные содержат число  n, за которым следует  n  строк, состоящих из пар чисел: вещественное число  x i  и
соответствующая ему частота  m i  (т.е. количества элементов x i  в исходной выборке).
Формат выходного файла
Выходные данные должны содержать три числа, разделённых пробелом: средние арифметическое, гармоническое и
геометрическое с точностью не менее 3 знаков после запятой.
"""
import numpy as np

with open("input.txt", "r") as file, open("output.txt", "w") as result:
    count = int(file.readline())
    arr = np.hstack(np.array(
        [np.repeat(float(value), int(repeat)) for value, repeat in [file.readline().split() for i in range(count)]]))
    mean = ('%.3f' % arr.mean()).rstrip('0').rstrip('.')
    harmonic = ('%.3f' % (len(arr) / np.sum(1.0 / arr))).rstrip('0').rstrip('.')
    geometric = ('%.3f' % (arr.prod() ** (1.0 / len(arr)))).rstrip('0').rstrip('.')
    result.write('{0} {1} {2}'.format(mean, harmonic, geometric))
