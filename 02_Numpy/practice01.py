import numpy as np

arr = np.array([
    [[7,8,9], [10, 11, 12]],
    [[1,2,3], [4, 5, 6]]
])
# print(arr.shape)
# print(arr.ndim)
# print(arr.dtype)

zeros = np.zeros((2,3))
# print(zeros)

ones = np.ones((5, 10))
# print(ones)

full = np.full((2, 3), 13)
# print(full)

arr = np.arange(1, 24, 2)
print(arr)

print(arr.size)
print(arr.reshape((2, 6)))
print(arr.reshape((3, 4)))
reshaped = (arr.reshape((4, 3)))
print(reshaped.T)

print(reshaped.flatten())