"""
CamelCase

Условие:
При написании сложных программ важное значение имеет стандартизация стиля кодирования, в частности формата
записи имён переменных. Часто используются следующие два стандарта для имён переменных, состоящих из нескольких
слов: Слова записываются друг за другом через знак подчёркивания с маленькой буквы (например my_variable). Слова
записываются друг за другом подряд, при этом каждое слово начинается с большой буквы (например MyVariable).
Требуется написать программу, переводящую имя переменной из одного стандарта в другой. Рекомендуется рассмотреть
частичные решения: Имя состоит из одного слова Формат входного файла Входной файл содержит одну строку — имя
переменной в каком-либо из стандартов. Формат выходного файла Выходной файл должен содержать имя переменной,
переведённое в другой стандарт. Ограничения Входное имя имеет длину не более 255 символов, содержит только
латинские буквы и символ подчёркивания, заведомо соответствует одному из стандартов.
"""
import re as regex


def getCase(s: str):
    underscored = s.split("_")
    if len(underscored) > 1:
        return ''.join(list(map(lambda x: x.capitalize(), underscored)))
    elif s.islower():
        return s.capitalize()
    else:
        return '_'.join(list(map(lambda x: x.lower(), regex.findall('.[^A-Z]*', s))))


with open("input.txt", "r") as file:
    string = file.read()

with open("output.txt", "w") as f:
    f.write(getCase(string))
