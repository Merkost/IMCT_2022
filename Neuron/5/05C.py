import numpy as np

r = open("input.txt", "r")
n = int(r.readline())
x = np.array([])
y = np.array([])
for _ in range(n):
    string = list(map(int, r.readline().split()))
    x = np.append(x,string[0])
    y = np.append(y,string[1])
fit = np.polyfit(x, y, 2)
w = open("output.txt", "w")
w.write(" ".join(map(str,[round(i, 3) for i in fit])))