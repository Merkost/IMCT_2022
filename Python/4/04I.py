"""
Увеличить по позициям

Условие:
Даны массив и список индексов (номеров элементов). Нумерация начинается с 1. Необходимо прибавить единицу к
каждому элементу массива, индекс которого есть в списке индексов. Формат входных данных Первая строка входных
данных содержит два числа N и M — длины массива и списка индексов соответственно. Вторая строка содержит N целых
чисел — элементы массива. Третья строка содержит M целых чисел — индексы. Формат выходных данных Выходные данные
должны содержать преобразованный массив.
"""

n, m = input().split()
numbers = [int(x) for x in input().split()]
indexes = [int(x) - 1 for x in input().split()]
numbersIndexes = list(map(int, range(0, len(numbers))))

# for index in indexes:
#     if index in numbersIndexes:
#         numbers[index] += 1

num = [num + 1 if i in indexes else num for i, num in enumerate(numbers)]
print(*num)
print(*numbers)
