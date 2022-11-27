import pandas as pd


def get_busiest_states(data: pd.DataFrame) -> pd.Series:
    """
    Вычисляет Series, в котором индексы - наименования штатов, а значение - количество совершённых международных звонов.

    Параметры:
      data: DataFrame с данными

    Возвращаемое значение:
      Series отсортированный по убыванию значений.
    """
    return pd.Series(data.set_index(data['State'])['Total intl calls'].groupby(level=0).sum()).sort_values(ascending=False)


df = pd.read_csv('data.csv')
busiest_states = get_busiest_states(df)
print(busiest_states)
