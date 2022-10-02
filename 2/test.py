with open("input.txt", "r") as file:
    lines = file.read().splitlines()

timeInRoute = [0, 0]
timeDeparture = [0, 0]

try:
    timeInRoute[0] = int(lines[1].split()[0])
except:
    None

try:
    timeInRoute[1] = int(lines[1].split()[1])
except:
    None

try:
    timeDeparture[0] = int(lines[0].split()[0])
except:
    None

try:
    timeDeparture[1] = int(lines[0].split()[1])
except:
    None


resultHours = 0
resultHours += timeDeparture[0]
resultHours += timeInRoute[0]


resultMinutes = timeDeparture[1] + timeInRoute[1]

resultHours %= 24
if resultMinutes > 59:
    resultHours += 1
    resultMinutes -= 60

with open("output.txt", "w") as result:
    result.write(str(resultHours) + " " + str(resultMinutes))
