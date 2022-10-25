"""
Time

Условие:
Требуется реализовать на языке Python класс Time.

class Time:
    # Конструктор, принимающий четыре целых числа: часы, минуты, секунды и миллисекунды.
    # В случае, если передан отрицательный параметр, вызвать исключение ValueError.
    # После конструирования, значения параметров времени должны быть корректными:
    # 0 <= GetHour() <= 23
    # 0 <= GetMinute() <= 59
    # 0 <= GetSecond() <= 59
    # 0 <= GetMillisecond() <= 999
    def __init__(self, hours=0, minutes=0, seconds=0, milliseconds=0):
        pass
    def GetHour(self):
        pass
    def GetMinute(self):
        pass
    def GetSecond(self):
        pass
    def GetMillisecond(self):
        pass
    # Прибавляет указанное количество времени к текущему объекту.
    # После выполнения этой операции параметры времени должны остаться корректными.
    def Add(self, time):
        pass
    # Оператор str должен представлять время в формате
    # HH:MM:SS.milliseconds
    def __str__(self):
        pass

Формат выходных данных Код решения должен содержать только определение и реализацию класса.

"""


class Time:
    # Конструктор, принимающий четыре целых числа: часы, минуты, секунды и миллисекунды.

    # В случае, если передан отрицательный параметр, вызвать исключение ValueError.
    # После конструирования, значения параметров времени должны быть корректными:
    # 0 <= GetHour() <= 23
    # 0 <= GetMinute() <= 59
    # 0 <= GetSecond() <= 59
    # 0 <= GetMillisecond() <= 999
    def __init__(self, hours=0, minutes=0, seconds=0, milliseconds=0):
        if hours < 0 or minutes < 0 or seconds < 0 or milliseconds < 0:
            raise ValueError

        self.milliseconds = 0
        self.seconds = 0
        self.minutes = 0
        self.hours = 0

        if (milliseconds < 1000):
            self.milliseconds = milliseconds
        else:
            self.milliseconds = milliseconds % 1000
            self.seconds = milliseconds // 1000

        secondsSumm = self.seconds + seconds
        if (secondsSumm < 60):
            self.seconds = secondsSumm
        else:
            self.seconds = secondsSumm % 60
            self.minutes += secondsSumm // 60

        minutesSumm = self.minutes + minutes
        if (minutesSumm < 60):
            self.minutes = minutesSumm
        else:
            self.minutes = minutesSumm % 60
            self.hours += minutesSumm // 60

        hoursSumm = self.hours + hours
        if (hoursSumm < 24):
            self.hours = hoursSumm
        else:
            self.hours = hoursSumm % 24

    def GetHour(self):
        return self.hours

    def GetMinute(self):
        return self.minutes

    def GetSecond(self):
        return self.seconds

    def GetMillisecond(self):
        return self.milliseconds

    # Прибавляет указанное количество времени к текущему объекту.
    # После выполнения этой операции параметры времени должны остаться корректными.
    def Add(self, time):
        millisSumm = self.milliseconds + time.milliseconds
        if (millisSumm < 1000):
            self.milliseconds += time.milliseconds
        else:
            millisPart = millisSumm % 1000
            self.milliseconds = millisPart
            addPart = millisSumm // 1000
            self.seconds += addPart

        secondsSumm = self.seconds + time.seconds
        if (secondsSumm < 60):
            self.seconds += time.seconds
        else:
            self.seconds = secondsSumm % 60
            self.minutes += secondsSumm // 60

        minutesSumm = self.minutes + time.minutes
        if (minutesSumm < 60):
            self.minutes += time.minutes
        else:
            self.minutes = minutesSumm % 60
            self.hours += minutesSumm // 60

        hoursSumm = self.hours + time.hours
        if (hoursSumm < 24):
            self.hours += time.hours
        else:
            self.hours = hoursSumm % 24

    # Оператор str должен представлять время в формате
    # HH:MM:SS.milliseconds
    def __str__(self):
        return '{0}:{1}:{2}.{3}'.format(str(self.hours).zfill(2), str(self.minutes).zfill(2),
                                        str(self.seconds).zfill(2), self.milliseconds)


time = Time(25, 11, 12, 1)

print(str(time))

time.Add(Time(0, 0, 0, 1010))

print(str(time))

time.Add(Time(0, 0, 0, 1010))

print(str(time))


