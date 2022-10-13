"""
ShiftableList

Условие:
Требуется реализовать на языке Python класс ShiftableList(list), который наследуется от list и реализует
операторы циклического сдвига влево (<<) и вправо (>>). Результатом выполнения этих операций должен быть новый
объект, при этом исходный не изменяется. Если операнд справа от оператора сдвига имеет тип, отличный от int,
необходимо вызвать исключение TypeError. В случае, если величина сдвига отрицательна, должен выполниться сдвиг в
противоположную сторону на количество позиций, равное модулю этой величины.

Формат выходных данных:
Код решения должен содержать только определение и реализацию класса.

"""
import copy


class ShiftableList(list):

    def __init__(self, *args):
        super(ShiftableList, self).__init__(args[0])

    # - битовый сдвиг влево (x << y).
    def __lshift__(self, count):
        if type(count) is not int:
            raise TypeError
        if count < 0:
            return self.__rshift__(abs(count))

        arrlen = len(self)
        if count > arrlen:
            count = count % arrlen

        newlist = copy.copy(self)[::-1]
        for i in range(count):
            newlist.insert(0, newlist.pop(len(newlist) - 1))
        return list(reversed(newlist))

    # - битовый сдвиг вправо (x >> y).
    def __rshift__(self, count):
        if type(count) is not int:
            raise TypeError
        if count < 0:
            return self.__lshift__(abs(count))

        arrlen = len(self)
        if count > arrlen:
            count = count % arrlen

        newlist = copy.copy(self)
        for i in range(count):
            newlist.insert(0, newlist.pop(len(newlist) - 1))
        return newlist


lst = ShiftableList(['a', 'b', 'c'])
lst2 = lst << 30
print(lst)
print(', '.join(lst2))
lst = ShiftableList(['a', 'b', 'c'])
lst2 = lst >> -2
print(''.join(lst), ''.join(lst2))
