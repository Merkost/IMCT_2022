"""


Условие:
Пусть задана некоторая матрица.Требуется написать программу, выполняющую поворот этой матрицы по часовой
стрелке k ∈ Z раз.При k < 0 такой поворот эквивалентен повороту против часовой стрелки | k | раз. В задаче
запрещено пользоваться какими - либо пакетами. Формат входных данных Первая строка входного файла содержит
натуральные числа n , m , k — количество строк, столбцов и поворотов.В каждой их следующих n строк содержится по m
натуральных чисел — значения элементов матрицы. Формат выходных данных Выходной файл должен содержать повернутую
матрицу. Каждая строка матрицы записывается в отдельной строке, при этом элементы разделены символом "пробел",
аналогично входным данным.
"""


def PrintMatrix(array):
    for i in range(len(array)):
        print(*[array[i][j] for j in range(len(array[0]))])


matrix = []
height, width, turn = map(int, input().split())
if turn % 4 == 0:
    for i in range(height):
        print(input())
elif turn % 4 == 1:
    for i in range(height):
        matrix.insert(0, list(input().split()))
    PrintMatrix(list(zip(*matrix)))
elif turn % 4 == 2:
    for i in range(height):
        matrix.insert(0, list(input().split())[::-1])
    PrintMatrix(matrix)
else:
    for i in range(height):
        matrix.append(list((input().split())))
    PrintMatrix(list(zip(*matrix))[::-1])

    # for i in range(height):
    #     matrix.append(list(input().split()))

    # if turn % 4 == 0:
    #     PrintMatrixFaster(matrix)
    # elif turn % 4 == 1:
    #     PrintMatrixFaster(list(zip(*matrix[::-1])))
    # elif turn % 4 == 2:
    #     PrintMatrixFaster(list(map(lambda x: x[::-1], matrix[::-1])))
    # elif turn % 4 == 3:
    #     PrintMatrixFaster(list(zip(*matrix))[::-1])





"""
2 3 3
1 2 3
4 5 6

3 3 2
1 2 3
4 5 6
7 8 9
"""
