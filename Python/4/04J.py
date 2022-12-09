"""


Условие:
Требуется написать программу, вычисляющую следующую итерацию игры «Жизнь». Игра проходит в прямоугольной
области размером N на M, состоящей из символов точка (.), обозначающий мёртвую клетку, и решётка (#), обозначающий
живую. Новое состояние каждой клетки определяется состоянием её 8 соседей по следующим правилам:

! если мёртвая клетка имеет ровно три живых соседа, она становится живой;
! если живая клетка имеет меньше двух или больше трёх живых соседей, она становится мёртвой;
! иначе состояние клетки не изменяется.

При этом соседями граничных клеток будут соответствующие граничные клетки с другой стороны области.
Так, левым соседом самой левой клетки поля будет являться самая правая клетка в той же строке.
Формат входных данных Входные данные содержат текущее состояние игры.
Формат выходных данных Выходные данные должны содержать следующую итерацию игры в том же формате.

..........
..........
..........

...#.
.....
#####
##...
#...#


.#.
.#.
.#.

"""
import sys
from copy import deepcopy

matrix = list(map(lambda x: [lst for lst in x.rstrip("\n")], sys.stdin.readlines()))
resultMatrix = deepcopy(matrix)
matrixColumnslen = len(matrix[0])
matrixRowslen = len(matrix)
matrixColumnEndIndex = matrixColumnslen - 1
matrixRowEndIndex = matrixRowslen - 1


def PrintMatrix(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if j == len(array[0]) - 1:
                print(array[i][j], sep=" ")
            else:
                print(array[i][j], sep=" ", end='')


def checkPoint(i, j):
    neighbours = []

    neighbours.append(matrix[i - 1][j - 1])
    neighbours.append(matrix[i - 1][j])
    neighbours.append(matrix[i - 1][j + 1])

    neighbours.append(matrix[i + 1][j + 1])
    neighbours.append(matrix[i + 1][j])
    neighbours.append(matrix[i + 1][j - 1])

    neighbours.append(matrix[i][j - 1])
    neighbours.append(matrix[i][j + 1])
    checkNeighboursFor(i, j, neighbours)


def checkNeighboursFor(i, j, neighbours):
    aliveNeighbours = neighbours.count("#")

    if matrix[i][j] == "." and aliveNeighbours == 3:
        resultMatrix[i][j] = "#"
    elif matrix[i][j] == "#" and aliveNeighbours not in (2, 3):
        resultMatrix[i][j] = "."


def checkCorners():
    rightDownNeighbours = []
    rightDownNeighbours.append(matrix[matrixRowEndIndex][matrixColumnEndIndex - 1])
    rightDownNeighbours.append(matrix[matrixRowEndIndex - 1][matrixColumnEndIndex])
    rightDownNeighbours.append(matrix[matrixRowEndIndex - 1][matrixColumnEndIndex - 1])

    rightDownNeighbours.append(matrix[matrixRowEndIndex][0])
    rightDownNeighbours.append(matrix[matrixRowEndIndex - 1][0])

    rightDownNeighbours.append(matrix[0][0])
    rightDownNeighbours.append(matrix[0][matrixColumnEndIndex])
    rightDownNeighbours.append(matrix[0][matrixColumnEndIndex -1])

    checkNeighboursFor(matrixRowEndIndex, matrixColumnEndIndex, rightDownNeighbours)

    rightUpNeighbours = []
    rightUpNeighbours.append(matrix[0][matrixColumnEndIndex - 1])
    rightUpNeighbours.append(matrix[1][matrixColumnEndIndex - 1])
    rightUpNeighbours.append(matrix[1][matrixColumnEndIndex])

    rightUpNeighbours.append(matrix[0][0])
    rightUpNeighbours.append(matrix[1][0])

    rightUpNeighbours.append(matrix[matrixRowEndIndex][matrixColumnEndIndex])
    rightUpNeighbours.append(matrix[matrixRowEndIndex][matrixColumnEndIndex - 1])
    rightUpNeighbours.append(matrix[matrixRowEndIndex][0])

    checkNeighboursFor(0, matrixColumnEndIndex, rightUpNeighbours)

    leftDownNeighbours = []
    leftDownNeighbours.append(matrix[matrixRowEndIndex - 1][0])
    leftDownNeighbours.append(matrix[matrixRowEndIndex - 1][1])
    leftDownNeighbours.append(matrix[matrixRowEndIndex][1])
    # From the other side of the matrix
    leftDownNeighbours.append(matrix[0][0])
    leftDownNeighbours.append(matrix[0][1])
    leftDownNeighbours.append(matrix[0][matrixColumnEndIndex])

    leftDownNeighbours.append(matrix[matrixRowEndIndex][matrixColumnEndIndex])
    leftDownNeighbours.append(matrix[matrixRowEndIndex - 1][matrixColumnEndIndex])

    checkNeighboursFor(matrixRowEndIndex, 0, leftDownNeighbours)

    leftUpNeughbours = []
    leftUpNeughbours.append(matrix[0][1])
    leftUpNeughbours.append(matrix[1][0])
    leftUpNeughbours.append(matrix[1][1])
    # From the other side of the matrix
    leftUpNeughbours.append(matrix[matrixRowEndIndex][0])
    leftUpNeughbours.append(matrix[matrixRowEndIndex][1])
    leftUpNeughbours.append(matrix[matrixRowEndIndex][matrixColumnEndIndex])

    leftUpNeughbours.append(matrix[0][matrixColumnEndIndex])
    leftUpNeughbours.append(matrix[1][matrixColumnEndIndex])

    checkNeighboursFor(0, 0, leftUpNeughbours)


def checkLeftBorderPoint(i, j):
    leftPointNeighbours = []
    leftPointNeighbours.append(matrix[i - 1][j + 1])
    leftPointNeighbours.append(matrix[i][j + 1])
    leftPointNeighbours.append(matrix[i + 1][j + 1])

    leftPointNeighbours.append(matrix[i + 1][j])
    leftPointNeighbours.append(matrix[i - 1][j])

    # From the other side of the matrix
    leftPointNeighbours.append(matrix[i + 1][matrixColumnEndIndex])
    leftPointNeighbours.append(matrix[i][matrixColumnEndIndex])
    leftPointNeighbours.append(matrix[i - 1][matrixColumnEndIndex])

    checkNeighboursFor(i, j, leftPointNeighbours)


def checkRightBorderPoint(i, j):
    rightPointNeighbours = []
    rightPointNeighbours.append(matrix[i - 1][j - 1])
    rightPointNeighbours.append(matrix[i][j - 1])
    rightPointNeighbours.append(matrix[i + 1][j - 1])

    rightPointNeighbours.append(matrix[i - 1][j])
    rightPointNeighbours.append(matrix[i + 1][j])

    # From the other side of the matrix
    rightPointNeighbours.append(matrix[i - 1][0])
    rightPointNeighbours.append(matrix[i][0])
    rightPointNeighbours.append(matrix[i + 1][0])

    checkNeighboursFor(i, j, rightPointNeighbours)


def checkUpBorderPoint(i, j):
    upPointNeighbours = []
    upPointNeighbours.append(matrix[i + 1][j - 1])
    upPointNeighbours.append(matrix[i + 1][j])
    upPointNeighbours.append(matrix[i + 1][j + 1])

    upPointNeighbours.append(matrix[i][j - 1])
    upPointNeighbours.append(matrix[i][j + 1])

    # From the other side of the matrix
    upPointNeighbours.append(matrix[matrixRowEndIndex][j - 1])
    upPointNeighbours.append(matrix[matrixRowEndIndex][j])
    upPointNeighbours.append(matrix[matrixRowEndIndex][j + 1])

    checkNeighboursFor(i, j, upPointNeighbours)


def checkDownBorderPoint(i, j):
    downPointNeighbours = []
    downPointNeighbours.append(matrix[i - 1][j - 1])
    downPointNeighbours.append(matrix[i - 1][j])
    downPointNeighbours.append(matrix[i - 1][j + 1])

    downPointNeighbours.append(matrix[i][j - 1])
    downPointNeighbours.append(matrix[i][j + 1])

    # From the other side of the matrix
    downPointNeighbours.append(matrix[0][j - 1])
    downPointNeighbours.append(matrix[0][j])
    downPointNeighbours.append(matrix[0][j + 1])

    checkNeighboursFor(i, j, downPointNeighbours)


def checkBorders():
    checkCorners()

    if matrixRowslen > 2:
        for i in range(1, matrixRowEndIndex):
            checkLeftBorderPoint(i, 0)
            checkRightBorderPoint(i, matrixColumnEndIndex)

    if matrixColumnslen > 2:
        for j in range(1, matrixColumnEndIndex):
            checkUpBorderPoint(0, j)
            checkDownBorderPoint(matrixRowEndIndex, j)


def checkHorizontal():
    checkNeighboursFor(0, 0, [matrix[0][1], matrix[0][matrixColumnEndIndex],
                              matrix[0][0], matrix[0][1], matrix[0][matrixColumnEndIndex],
                              matrix[0][0], matrix[0][1], matrix[0][matrixColumnEndIndex]])
    checkNeighboursFor(0, matrixColumnEndIndex, [matrix[0][matrixColumnEndIndex - 1], matrix[0][0],
                                                 matrix[0][matrixColumnEndIndex - 1], matrix[0][matrixColumnEndIndex],
                                                 matrix[0][0],
                                                 matrix[0][matrixColumnEndIndex - 1], matrix[0][matrixColumnEndIndex],
                                                 matrix[0][0]])
    # index out of range warning
    for j in range(1, matrixColumnslen - 1):
        checkNeighboursFor(0, j, [matrix[0][j - 1], matrix[0][j + 1],
                                  matrix[0][j - 1], matrix[0][j], matrix[0][j + 1],
                                  matrix[0][j - 1], matrix[0][j], matrix[0][j + 1]])


def checkVertical():
    checkNeighboursFor(0, 0, [matrix[0][0], matrix[0][0],
                              matrix[1][0], matrix[1][0], matrix[1][0],
                              matrix[matrixRowEndIndex][0], matrix[matrixRowEndIndex][0],
                              matrix[matrixRowEndIndex][0], ])
    checkNeighboursFor(matrixRowEndIndex, 0, [matrix[matrixRowEndIndex - 1][0]])

    # index out of range warning
    for j in range(1, matrixRowslen - 1):
        checkNeighboursFor(j, 0, [matrix[j - 1][0], matrix[j + 1][0],
                                  matrix[j - 1][0], matrix[j][0], matrix[j + 1][0],
                                  matrix[j - 1][0], matrix[j][0], matrix[j + 1][0]])


if matrixRowslen == matrixColumnslen:
    if matrixRowslen == 1:
        checkNeighboursFor(0, 0, [matrix[0][0], matrix[0][0], matrix[0][0], matrix[0][0],
                                  matrix[0][0], matrix[0][0], matrix[0][0], matrix[0][0]])
        PrintMatrix(resultMatrix)
    elif matrixRowslen == 2:
        checkBorders()
        PrintMatrix(resultMatrix)
    else:
        checkBorders()
        for i in range(1, matrixRowslen - 1):
            for j in range(1, matrixColumnslen - 1):
                checkPoint(i, j)
        PrintMatrix(resultMatrix)
elif matrixRowslen == 1:
    checkHorizontal()
    PrintMatrix(resultMatrix)
elif matrixColumnslen == 1:
    checkVertical()
    PrintMatrix(resultMatrix)
else:
    checkBorders()
    for i in range(1, matrixRowslen - 1):
        for j in range(1, matrixColumnslen - 1):
            checkPoint(i, j)
    PrintMatrix(resultMatrix)

