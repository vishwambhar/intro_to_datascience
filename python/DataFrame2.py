__author__ = 'vishyoo'

from pandas import DataFrame, Series

def create_dataframe():
    data = {'name': Series(['Peter', 'Ponty', 'Delli', 'Sophia']),
            'age': Series([34, 56, 23, 21]),
            'fare': Series([6.25, 8, 9, 7.5]),
            'survived?': Series([False, True, False, True])
            }
    df = DataFrame(data);
    print(df)

create_dataframe();
