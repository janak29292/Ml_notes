from numpy import nan
from pandas import DataFrame

d = {
    'A': [1,2,nan],
    'B': [5, nan, nan],
    'C': [1,2,3]
}

df = DataFrame(d)

print(df)

# drop rows with missing value
print(df.dropna())
# drop columns with missing value
print(df.dropna(axis=1))

# drop row with 2 or more missing values
print(df.dropna(thresh=2))


# Fill missing data
print(df.fillna(value='fill'))

print(df['A'].fillna(value=df['A'].mean()))
