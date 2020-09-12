from numpy import array, ones, zeros, linspace, eye, random, sqrt, exp, sin, log, sum, std

x = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
 [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
 [[19, 20, 21], [22, 23, 24], [25, 26, 27]]]

arr = array(x)

print(arr.shape)

print(arr[0])

print(arr[0, 1])

print(arr[:1, :])

print(arr[:1, :])

print(arr[1: , 2:])

print(arr[:, :, :1])

print(std(arr))
