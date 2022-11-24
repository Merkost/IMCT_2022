import pandas as pd
import numpy as np

n, k = [int(i) for i in input().split()]
data = [input().split() for _ in range(n+1)]
m = int(input())
test = [input().split() for _ in range(m)]
data[0].append("value")
df = pd.DataFrame(data=data[1:], columns = data[0])  # 1st row as the column names
print(df)

print(df) overcast

for i in range(k):
    inner_df = pd.DataFrame(columns=["name", "one", "zero"])
    for value in df[df.columns[0]].unique():
        inner_df.append([value, df[df.columns[0] == value]])



print(df)



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