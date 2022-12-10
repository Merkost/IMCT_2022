
import pandas as pd
from matplotlib import pyplot as plt


def draw_bars(data: pd.DataFrame, column: str, target_column: str) -> None:
    """
        Отображает долю целевых значений `target_column` при каждом уникальном значении категориального признака `column` в виде слолбчатой диаграммы.

        Параметры:
            data: таблица данных.
            column: название категориального признака.
            target_column: название целевой переменной.
    """
    index = data[target_column].groupby(data[column]).value_counts(normalize=True).mul(100)
    df = pd.DataFrame(index)
    print(df)
    #stck = df.unstack().plot(ax = plt.gca(), kind='bar', stacked=True, width=0.78, rot=0)
    for i in df.unstack():
        print(i)
    stck = plt.bar(df.unstack(), stacked=True, width=0.78, rot=0, height = 1)
    stck.legend(data[target_column].unique(), loc='upper right', title=target_column)
    for c in stck.containers:
        labels = ['%.2f %%' % v if v > 5.0 else '' for v in c.datavalues]
        stck.bar_label(c, label_type='center', labels=labels)
    stck.set_xlim(left = data[column].min() - 1, right = data[column].max() + 1)

data = pd.read_csv('03С_data.csv')

plt.figure(figsize=(10, 5))
plt.rcParams.update({ 'font.size': 8 })

draw_bars(data, 'Customer service calls', 'Churn')
plt.savefig('output.png')