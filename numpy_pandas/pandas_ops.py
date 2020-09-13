from pandas import DataFrame

df = DataFrame({
    'col1': [1, 2, 3, 4],
    'col2': [444, 555, 666, 444],
    'col3': ['abc', 'def', 'ghi', 'xyz'],
})

print(df)

print(df.head)


print(df['col2'].unique())

print(df['col2'].nunique())

print(df['col2'].value_counts())

print(df[df['col1'] > 2])


# apply method

print(df['col2'].apply(lambda x: x*2))

print(df['col3'].apply(len))



print(df.sort_values(by='col2'))

print(df.isnull)


df = DataFrame({
    'A': 'foo foo foo bar bar bar'.split(),
    'B': 'one one two two one one'.split(),
    'C': 'x y x y x y'.split(),
    'D': [1, 3, 2, 5, 4, 1]
})


print(df)
print(df.pivot_table(values='D', index=['A', 'B'], columns='C'))
