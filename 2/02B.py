"""
Время в пути

Условие:
Время отправления и время прибытия поезда задаются в виде Ч М, где Ч - час от 0 до 23, М - минута от 0 до 59.
Время в пути задаётся аналогично в формате Ч М, где Ч - количество часов от 0 до 999, а М - количество минут от0 до 59.
Требуется по данному времени отправления и времени в пути вычислить время прибытия поезда (возможно,
в другие сутки).
Формат входного файла: В первой строке входного файла содержится время отправления, во второй — время в пути.
Формат выходного файла: В выходном файле должна быть единственная строка, содержащая время прибытия.

"""

with open("input.txt", "r") as file:
    lines = file.read().splitlines()

timeDeparture = list(map(lambda x: int(x), lines[0].split()))
timeInRoute = list(map(lambda x: int(x), lines[1].split()))

resultHours = timeDeparture[0] + timeInRoute[0]
resultMinutes = timeDeparture[1] + timeInRoute[1]

resultHours %= 24
if resultMinutes > 59:
    resultHours += 1
    resultMinutes -= 60

with open("output.txt", "w") as result:
    result.write(str(resultHours) + " " + str(resultMinutes))

