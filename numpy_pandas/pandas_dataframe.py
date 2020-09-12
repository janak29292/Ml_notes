# DATAFRAME PART 1
# Create dataframe and grab information

from pandas import DataFrame
from numpy import array, random

random.seed(101)

df = DataFrame(random.randn(5,4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
print(df)

print(df['W'])
print(df.W)
# A dataframe is a group of series that shares an index

print(df[['W', 'Z']])

df['new'] = df.W + df.Y

print(df)

df.drop('new', axis=1, inplace=True)
# axis=0 default is for rows
# inplace=False is default which does not changes df

print(df)
print(df.shape)


#  Rows

print(df.loc['A'])
print(df.iloc[0])

# Values and subsets from DataFrame
print(df.loc['B', 'Y'])

print(df.loc[['A', 'B'], ['W', 'Y']])


# DATAFRAME PART 2
# Conditional Selection and multi-indexing

print(df > 0)
print(df[df > 0])

# filtering
print(df['W'] > 0)
print(df[df['W'] > 0])


print(df[df['W'] > 0]['X'])
print(df[df['W'] > 0][['X']])
print(df[df['W'] > 0][['X', 'Y']])


# Multiple conditional selection
# filtering with AND Condition
print(df[(df['W'] > 0) & (df['Y'] > 0)])

# filtering with OR Condition
print(df[(df['W'] > 1) | (df['Y'] > 1)])


# Reset index
print(df.reset_index(inplace=False))
# print(df)


# Set Index
new_ind = 'CA NY WY OR CO'.split()

df['States'] = new_ind

print(df)

print(df.set_index('States', inplace=False))
# print(df)


# Multi Index and Index Heirarchy
