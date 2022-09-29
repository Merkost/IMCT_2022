
with open("input.txt", "r") as file:
    lines = file.read().splitlines()

dt = list(map(lambda x: float(x), lines[0].split(" ")))
vv = list(map(lambda x: float(x), lines[1].split(" ")))
vv.sort()
ww = list(map(lambda x: float(x), lines[0].split(" ")))
ww.sort()

d = dt[0]
t = dt[1]
v1 = vv[0]
v2 = vv[1]
w1 = ww[0]
w2 = ww[1]

result = 0.0
if (t*w1 == d):
    result = 0.0
elif (d%v2==w2):
    result = d//v2

with open("output.txt", "w") as f:
    f.write(str(result))
