"""
Грибы

Условие:
Аня очень хорошо разбирается в грибах. Грибы бывают разные. Опята, лисички. сыроежки, подосиновики,
подберезовики, обабки, маслята, оленьи рожки, поганки (ядовитые). Boletus edulis (белые грибы) — самые хорошие.
Нужно посчитать, сколько Boletus edulis собрала Аня. Формат входных данных В первой строке содержится число N N —
количество грибов. В следующих N N строках — названия грибов. Формат выходных данных Выходные данные должны
содержать одно число — количество Boletus edulis. Регистр не имеет значения, т.е. к примеру BoLeTuS eDuLiS и
bolETUS edulIS — один и тот же гриб.
"""

words = []

times = int(input())
for i in range(times):
    words.append(input())

print(sum(x == "boletus edulis" for x in list(map(lambda x: x.lower(), words))))