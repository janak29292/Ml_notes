from numpy import array, ones, zeros, linspace, eye, random, sqrt, exp, sin, log, sum, std, arange

x = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
 [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
 [[19, 20, 21], [22, 23, 24], [25, 26, 27]]]

arr = array(x)


print(arr.max())
print(arr.argmax())


print(arange(0, 20, 3))
print(linspace(0, 1, 10))
print(random.rand(5))
print(random.rand(5, 5))
print(random.randn(5))
print(eye(4))
print(zeros(5))
print(ones((5,5)))

print(arr.shape)
print(arr.reshape(27))

print(arr[0])

print(arr[0, 1])

print(arr[:1, :])

print(arr[:1, :])

print(arr[1: , 2:])

print(arr[:, :, :1])

print(std(arr))
print(std(arr, axis=0))
print(std(arr, axis=1))
print(std(arr, axis=2))


print(arr)
print(arr % 2 ==0)
print(arr[arr % 2 ==0])
print(len(arr[arr % 2 ==0]))


print(arr - 10)
print((arr - 10)/10)
print((arr - 10)/0)
