"""
PrintMatrix

Условие:
Требуется реализовать на языке Python функцию PrintMatrix(mat), которая принимает двумерный массив и
печатает его. Пример использования функции в примерах тестов. Формат выходных данных Код решения должен содержать
только определение и реализацию функции.
"""

def PrintMatrix(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if j == len(array[0])-1:
                print(array[i][j], sep = " ")
            else:
                print(array[i][j], sep = " ", end = ' ')

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
PrintMatrix(mat)