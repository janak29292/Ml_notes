# Merge, Join and Concatenate

from pandas import DataFrame, concat, merge


# Concatenate

df1 = DataFrame({
        'A': 'A0 A1 A2 A3'.split(),
        'B': 'B0 B1 B2 B3'.split(),
        'C': 'C0 C1 C2 C3'.split(),
        'D': 'D0 D1 D2 D3'.split(),
    }, index=[0, 1, 2, 3]
)

df2 = DataFrame({
        'A': 'A4 A5 A6 A7'.split(),
        'B': 'B4 B5 B6 B7'.split(),
        'C': 'C4 C5 C6 C7'.split(),
        'D': 'D4 D5 D6 D7'.split(),
    }, index=[4, 5, 6, 7]
)


df3 = DataFrame({
        'A': 'A8 A9 A10 A11'.split(),
        'B': 'B8 B9 B10 B11'.split(),
        'C': 'C8 C9 C10 C11'.split(),
        'D': 'D8 D9 D10 D11'.split(),
    }, index=[8, 9, 10, 11]
)

print(concat([df1, df2, df3]))

print(concat([df1, df2, df3], axis=1))


# Merge


left = DataFrame({
    'key': 'K0 K1 K2 K3'.split(),
    'A': 'A0 A1 A2 A3'.split(),
    'B': 'B0 B1 B2 B3'.split(),
})


right = DataFrame({
    'key': 'K0 K1 K2 K3'.split(),
    'C': 'C0 C1 C2 C3'.split(),
    'D': 'D0 D1 D2 D3'.split(),
})

print(merge(left, right, how="inner", on='key'))


left = DataFrame({
    'key1': 'K0 K0 K1 K2'.split(),
    'key2': 'K0 K1 K0 K1'.split(),
    'A': 'A0 A1 A2 A3'.split(),
    'B': 'B0 B1 B2 B3'.split(),
})


right = DataFrame({
    'key1': 'K0 K1 K1 K2'.split(),
    'key2': 'K0 K0 K0 K0'.split(),
    'C': 'C0 C1 C2 C3'.split(),
    'D': 'D0 D1 D2 D3'.split(),
})

print(left)
print(right)

# print(merge(left, right, on=['key1', 'key2']))
#
# print(merge(left, right, how='outer', on=['key1', 'key2']))
#
# print(merge(left, right, how='right', on=['key1', 'key2']))

print(merge(left, right, how='left', on=['key1', 'key2']))

# Join
# Here keys that we are joining on are on aur index instead of our columns


left = DataFrame({
        'A': 'A0 A1 A2'.split(),
        'B': 'B0 B1 B2'.split(),
    }, index=['K0', 'K1', 'K2']
)

right = DataFrame({
        'C': 'C0 C2 C3'.split(),
        'D': 'D0 D2 D3'.split(),
    }, index=['K0', 'K2', 'K3']
)


print(left.join(right))

print(left.join(right, how="outer"))
