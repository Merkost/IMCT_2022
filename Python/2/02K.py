"""
Космический корабль

Условие:
Запуск космического корабля это очень торжественное событие, требующее обратного отсчета.
Формат входных данных: На вход программа получает одно число N N — количество секунд до запуска.
Формат выходных данных: Программа должна вывести обратный отсчет от N N до 1, завершающийся командой "Start".
Каждый шаг отсчета сопровождается восклицательными знаками. С каждой секундой их количество увеличивается
на единицу, так что команда "Start"сопровождается N восклицательными знаками.
"""

seconds = int(input())

for i in range(seconds):
    print((seconds - i), ("!" * i), sep = '')
print("Start", "!" * seconds, sep = '')