from __future__ import annotations

h_s = int(input())
m_s = int(input())
s_s = int(input())

min_s = min(h_s, m_s, s_s)
max_s = max(h_s, m_s, s_s)

h_len = len(str(h_s))
m_len = len(str(m_s))
s_len = len(str(s_s))



class Time:
    # Конструктор, принимающий три целых числа: часы, минуты, секунды.
    def __init__(self, hours: int = 0, minutes: int = 0, seconds: int = 0):
        if hours < 0 or minutes < 0 or seconds < 0:
            raise ValueError

        self.seconds = 0
        self.minutes = 0
        self.hours = 0

        secondsSumm = self.seconds + seconds
        if secondsSumm < s_s:
            self.seconds = secondsSumm
        else:
            self.seconds = secondsSumm % s_s
            self.minutes = secondsSumm // s_s

        minutesSumm = self.minutes + minutes
        if minutesSumm < m_s:
            self.minutes = minutesSumm
        else:
            self.minutes = minutesSumm % m_s
            self.hours += minutesSumm // m_s

        hoursSumm = self.hours + hours
        if hoursSumm < h_s:
            self.hours = hoursSumm
        else:
            self.hours = hoursSumm % h_s

    def __eq__(self, other: Time):
        return self.hours == other.hours and self.minutes == other.minutes and self.seconds == other.seconds

    def __gt__(self, other):
        if self.hours < other.hours:
            return False
        elif self.minutes < other.minutes:
            return False
        elif self.seconds < other.seconds:
            return False
        else:
            return True

    def __sub__(self, other) -> Time:
        # newh = int(math.fabs(self.hours - other.hours))
        # news = (self.seconds - other.seconds)
        # newm = int(math.fabs(self.minutes - other.minutes))
        # newh = int(math.fabs(self.hours - other.hours))
        subFromMins = 0
        secondsSub = self.seconds - other.seconds
        if (secondsSub < 0):
            secondsSub = s_s - (other.seconds - self.seconds)
            subFromMins = 1

        subFromHours = 0
        minutesSub = self.minutes - other.minutes
        if (minutesSub < 0):
            minutesSub = m_s - (other.minutes - self.minutes) - subFromMins
            subFromHours = 1
        elif (minutesSub == 0 and subFromMins == 1):
            subFromHours = 1
        elif (subFromMins > 0):
            minutesSub -= 1

        hoursSub = self.hours - other.hours
        if (hoursSub < 0):
            hoursSub = h_s - (other.hours - self.hours) - subFromHours
        elif (hoursSub == 0 and subFromHours == 1):
            hoursSub = h_s - 1
        elif (subFromHours > 0):
            hoursSub -= 1

        return Time(hoursSub, minutesSub, secondsSub)


    def __find_nearest_same_numbers(self, nextNum) -> str:
        if int(nextNum) > min_s:
            return "0"

        # hour_list = list(str(self.hours))
        # hours_len = len(hour_list)
        # if int(nextNum * h_len) > self.hours:
        #     return nextNum
        # elif int(nextNum * m_len) > self.minutes:
        #     return nextNum
        # elif int(nextNum * s_len) > self.seconds:
        #     return nextNum
        # else:
        #     return self.__find_nearest_same_numbers(nextNum + 1)

        if int(nextNum * h_len) == self.hours:
            if int(nextNum * m_len) <= self.minutes or (int(nextNum * m_len) == self.minutes and int(nextNum * s_len) < self.seconds):
                return self.__find_nearest_same_numbers(nextNum + 1)

        return str(nextNum)

    def NearestSameNumbers(self) -> str:
        min_current = min(self.hours, self.minutes, self.seconds)
        max_current = max(self.hours, self.minutes, self.seconds)
        hours_length = int(len(str(self.hours)))
        hours_length_def = int(len(str(h_s)))

        if (hours_length > 1):
            hour_list = list(str(self.hours))
            if (h_len > hours_length):
                last_hour_max_same = 1
            elif hour_list[0] < hour_list[1]:
                last_hour_max_same = int(hour_list[1]) - int(hour_list[0])
            else:
                last_hour_max_same = hour_list[0]
                if int(last_hour_max_same) >= min_s:
                    last_hour_max_same = 0
        else:
            last_hour_max_same = self.hours

        if self.hours > int(hours_length_def * str(last_hour_max_same)):
            return "0"
        else:
            # if self.hours in range(int(str(min_s) * hours_length), int(str(max_s) * hours_length) - 1)
            return self.__find_nearest_same_numbers(last_hour_max_same)

    def TimeToZeros(self) -> Time:

        if self.seconds > 0:
            news = s_s - self.seconds
        else:
            news = 0

        if news != 0:
            newm = m_s - self.minutes - 1
        else:
            newm = m_s - self.minutes

        if newm != 0 or news != 0:
            newh = h_s - self.hours - 1
        else:
            newh = h_s - self.hours

        return Time(newh, newm, news)

    def TimeToSeconds(self: Time) -> int:
        minutes = self.hours * m_s
        minutes += self.minutes

        sec = minutes * s_s
        sec += self.seconds
        return sec

    # Оператор str должен представлять время в формате
    # HH:MM:SS.milliseconds
    def __str__(self):
        return '{0}:{1}:{2}'.format(str(self.hours).zfill(h_len), str(self.minutes).zfill(m_len),
                                    str(self.seconds).zfill(s_len))


h = int(input())
m = int(input())
s = int(input())



time = Time(h, m, s)
# print(time)

nums = time.NearestSameNumbers()
# print(nums)
nearestSameTime = Time(int(len(str(h_s)) * nums), int(len(str(m_s)) * nums), int(len(str(s_s)) * nums))
# print(nearestSameTime)

if (int(nums) == 0):
    timeToZeros = time.TimeToZeros()
    print(timeToZeros.TimeToSeconds())
elif (time > nearestSameTime):
    result = (time - nearestSameTime).TimeToSeconds()
    print(result)
else:
    result = (nearestSameTime - time).TimeToSeconds()
    print(result)

"""

24
60
60
23
50
00

=600


627
5
777
49
3
2

=239425


627
5
777
42
4
1

=239425

"""
