# Group by allows us to group rows based on columns and perform aggregate functions on them.
from pandas import DataFrame

data = {
    'Company': 'GOOG GOOG MSFT MSFT FB FB'.split(),
    'Person': 'Sam Charlie Amy Vanessa Carl Sarah'.split(),
    'Sales': [200, 120, 340, 124, 243, 350]
}

df = DataFrame(data)

print(df)

print(df.groupby('Company').sum())

print(df.groupby('Company').count())

print(df.groupby('Company').max())

print(df.groupby('Company').describe())

print(df.groupby('Company').describe().transpose())
