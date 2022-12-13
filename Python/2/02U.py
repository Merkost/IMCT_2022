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


def rotate(arr):
    matrix = []
    for i in zip(*arr):
        matrix.append(tuple(i))
    return matrix


def printMatrix(arr):
    for i in arr:
        print(" ".join(list(map(str, i))))

def printMatrixReversed(arr):
    for i in arr:
        print(" ".join(reversed(list(map(str, i)))))


height, width, turn = map(int, input().split())
lst = [tuple(input().split()) for _ in range(height)]
turn %= 4
if turn == 0:
    printMatrix(lst)
elif turn == 1:
    printMatrix(rotate(reversed(lst)))
    # [print(*i) for i in zip(*reversed(lst))]
elif turn == 2:
    printMatrixReversed(reversed(lst))
elif turn == 3:
    printMatrix(reversed(rotate(lst)))
    # [print(*i) for i in zip(*reversed(lst))]

    # [print(*zip(*[input().split()[::-1] for _ in range(height)]), sep = "\n")]

# def PrintMatrix(array):
#     [print(*[array[i][j] for j in range(len(array[0]))]) for i in range(len(array))]


# height, width, turn = map(int, input().split())
# turn %= 4
# if turn == 0:
#     [print(input()) for i in range(height)]
# elif turn == 1:
#     [print(*i) for i in zip(*[input().split() for _ in range(height)][::-1])]
# elif turn == 2:
#     [print(*i) for i in [input().split()[::-1] for _ in range(height)])]
# elif turn == 3:
#     [print(*i) for i in zip(*[input().split()[::-1] for _ in range(height)])]

"""
2 3 3
1 2 3
4 5 6

3 3 2
1 2 3
4 5 6
7 8 9
"""

# [[a, b] for a, b in zip(xrange(100), xrange(100))]

# elif turn % 4 == 1
# PrintMatrix3(tuple(zip(*[input().split()[::-1] for i in range(height)])))

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
