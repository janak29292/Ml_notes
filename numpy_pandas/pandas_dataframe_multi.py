from pandas import MultiIndex, DataFrame
from numpy import random

outside = 'G1 G1 G1 G2 G2 G2'.split()
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside, inside))
hier_index = MultiIndex.from_tuples(hier_index)

print(hier_index)

df = DataFrame(random.randn(6,2), hier_index, ['A', 'B'])
print(df)


print(df.loc['G1'])

print(df.loc['G1'].loc[1])

df.index.names = ['Groups', 'Num']

print(df)

print(df.xs('G1'))

# Cross section (Skip outer index)
print(df.xs(1, level='Num'))
