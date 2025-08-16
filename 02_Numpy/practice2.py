import numpy as np

arr = np.arange(1, 13)
# print(arr)

# print(arr[2:5])
# print(arr[0:8:2])
# print(arr[::2])
# print(arr[4:])
# print(arr[:4])

# print(arr.shape)

arr_reshaped = arr.reshape((3, 4))
# print(arr_reshaped)

r_first = arr_reshaped[0]
# print(r_first)

r_last = arr_reshaped[2]
# print(r_last)

# first two rows
# print(f'First two row: \n {arr_reshaped[:2]}')

# first two elements of first row
# print(f'First two elements of first row: \n {arr_reshaped[:1, :2]}')

# first two elements of first two row
# print(f'first two elements of first two row: \n {arr_reshaped[:2, :2]}')

# first column
# print(f'first column: \n {arr_reshaped[:, :1]}')
# print(f'shape: {(arr_reshaped[:, :1]).shape}')
# print(f'dimension: {(arr_reshaped[:, :1]).ndim}')

# last two column
# print(f'Last two column: \n {arr_reshaped[:, -2:]}')


# sorting
arr = np.array([10, 7, 15, 2, 19, 1])
# print(np.sort(arr))

arr_2D = np.array([[3,1,2], [0,4,5]])
# print(np.sort(arr_2D, axis=0))          # sort the column
# print(np.sort(arr_2D, axis=1))          # sort the rows 
# default sorting axis is -1, 1 and -1 act same in 2D array, but may vary in greater dimension array.

# filtering (inside big bracket)
arr = np.arange(1, 21)
even_num = arr[arr%2 ==0]
# print(even_num)

# we can do filter with mask and index

# index
arr = np.arange(1, 50, 3)
# index in multiple of 5 [5, 10, 15, 20, ..... so on]
index = [4, 9, 14]
# print(arr[index])

# mask
arr = np.arange(1, 101)
mask = (arr % 5) ==0
# print(arr[mask])

# where
arr = np.array([3, 6, 9, 12, 15])
# where = np.where(arr/3 == 3)
# print(where)
# print(arr[where])

what = np.where((arr/3)==5, 'yes', 'no')            # (condition, value on true, value on false)
# print(what)


# adding and removing data
original = np.array([[1, 2, 3], [4, 5, 6]])
# print("original: \n", original)

new_row = np.array([7, 8, 9])
with_new_row = np.vstack((original, new_row))
# print("with new row: \n", with_new_row)

new_col = np.array([[6], [15]])                     # should be 2D. 
with_new_col = np.hstack((original, new_col))
# print("with new col: \n", with_new_col)

zero = np.zeros((2, 3 ,4))
# print(zero)
# print(zero.shape)

depth = np.zeros((3, 4))
# print(np.concatenate([zero, depth], axis=2))

arr_2D = np.zeros((2, 2, 3))
print(arr_2D)
print(arr_2D.shape)


row = np.zeros((3))
