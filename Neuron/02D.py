import pandas as pd
from sklearn.impute import SimpleImputer
import numpy as np

def fillna_date(data: pd.DataFrame, function: str = 'mean') -> pd.DataFrame:
    '''Fills NaN values in every column in `data` with values obtained by applying aggregate `function` over a month.
       If every value within a month is NaN the fill value is obtained over a year.
       If every value within a year is NaN the fill value is obtained over the whole column.

    Arguments:
        data: a pandas DataFrame, with datetime index
        function: aggregate function to be used for obtaining fill value.
            Possible values are: "mean", "median", "max", "min", "sum"

    Returns:
        a new pandas DataFrame with NaN values replaced
        '''

    # f = getattr(pd.DataFrame, function)
    columns = data.columns.values.tolist()[1:]
    print(data.columns)
    # data[1] = pd.to_datetime(data[1])
    print(data)

    # m = data.mean(axis=1)
    # df = data.fillna(m)
    # print(df)

    # groupedMonth = data.groupby(pd.Grouper(freq='M')).agg(function)

    # groupedYear = data.groupby(pd.Grouper(freq='Y')).agg(function)



    # grouped = data.groupby([data.index.month, data.index.year])

    # data.fillna()
    data.fillna(method ='ffill')
    return data


data = pd.read_csv('02D_input.csv')
data = fillna_date(data)
# print(data)
# data.to_csv('output.csv')
