import pandas as pd


def join_dataframes(data: pd.DataFrame, states: pd.DataFrame) -> pd.DataFrame:
    """
    Возвращает объединённый DataFrame

    Параметры:
      data: DataFrame с пользователями
      states: DataFrame с штатами

    Возвращаемое значение:
      объединённый DataFrame, содержащий поля 'Total day calls', 'Total night calls', 'State' в данном порядке
    """
    return data.join(states, on = 'State ID').drop('State ID', axis=1)
    # return pd.merge(data, states, left_on='State ID', right_on='ID', how='left').drop('State ID', axis=1)


states = pd.read_csv('02C_states.csv', index_col='ID')
data = pd.read_csv('02C_data.csv', index_col='ID')
joined_df = join_dataframes(data, states)
print(joined_df)
