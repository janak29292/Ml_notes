from numpy import array
from pandas import Series

labels = ['a', 'b', 'c']
my_data = [10, 20, 30]
arr = array(my_data)
d = {'a': 10, 'b': 20, 'c': 30}

x = Series(my_data)
print(x)

x = Series(my_data, labels)
print(x)

x = Series(arr)
print(x)

x = Series(d)
print(x)

x = Series(['a', 1, lambda x: x+1])
print(x)

ser1 = Series([1,2,3,4], ['USA', 'Gerrmany', 'USSR', 'Japan'])
print(ser1)

ser2 = Series([1,2,5,4], ['USA', 'Gerrmany', 'Italy', 'Japan'])
print(ser2)

print(ser1 + ser2)

# lookups are like dictionary or array
