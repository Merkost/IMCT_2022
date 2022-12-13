import pandas as pd
import numpy as np

n, k = [int(i) for i in input().split()]
ai = {}
for i in input().split():
    ai[i] = {}
# data = [input().split() for _ in range(n)]
# m = int(input())
# test = [input().split() for _ in range(m)]
# data[0].append("value")
# df = pd.DataFrame(data=data, columns=ai)  # 1st row as the column names
# print(df)

for i in range(n):
    row = input().split()
    class_mark = int(row[-1])
    for j in range(len(ai.keys())):
        if row[j] not in ai[list(ai.keys())[j]]:
            ai[list(ai.keys())[j]][row[j]] = [0, 0]
        ai[list(ai.keys())[j]][row[j]][class_mark] += 1

total_error = 1.0
fin_setting = {}
fin_column = 0
for i in ai:
    err_sum = 0
    temp_setting = {}
    for j in ai[i]:
        err_sum += min(ai[i][j])
        if ai[i][j][0] == ai[i][j][1]:
            temp_setting[j] = 1
        else:
            temp_setting[j] = ai[i][j].index(max(ai[i][j]))
    if err_sum / n < total_error:
        total_error = err_sum / n
        fin_setting = temp_setting
        fin_column = list(ai.keys()).index(i)

for i in range(int(input())):
    row = input().split()
    print(fin_setting[row[fin_column]])

"""

10 4
Outlook Temperature Humidity Windy
overcast hot high FALSE 1
sunny mild high FALSE 0
overcast mild high TRUE 1
rainy mild normal FALSE 1
overcast hot normal FALSE 1
rainy mild high FALSE 1
rainy cool normal FALSE 1
rainy mild high TRUE 0
sunny hot high FALSE 0
sunny hot high TRUE 0
4
rainy cool normal TRUE
sunny cool normal FALSE
overcast cool normal TRUE
sunny mild normal TRUE



"""
