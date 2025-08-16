import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# print(arr[0] + arr[1])

# multi_dimensional array
arr0 = np.array(1)   # 0-D

arr1 = np.array([1, 2])  # 1-D because this array contain elements of 0-D
arr2 = np.array([[1, 2], [3, 4]])  # 2-D because this array contain elements of 1-D. elements are [1,2] and [3,4]. can contain single element so.
# same thing apply on 2-D, 3-D, likewise. 

# arr3 = np.array(
#     [
#         [[1,2], [3,4]],
#         [[5,6], [7,8]]
#      ])
# print(arr3[0,0,0]) # accessing 1
# print(arr3[1,0,1]) # accessing 6

# num = np.array([ [[1,2,11],[3,4,12]], [[5,6,13],[7,8,14]] ])

# print(num[0,1]) 
# print(num[0,1,2])

# print(num[0,0:])
# print(num[0,1,1:])

# we want [4,12] and [8,14].
# (0:) = select both element of array
# (1) = select second sub-element from both element
# (1:) = select 2nd and 3rd item of both sub-element
# print(num[0:,1,1:])

# print(num.dtype)
# print

# import time
# start = time.time()
# py_list = [i*2 for i in range(1000)]
# # print(py_list)

# print("\n List operation time: ", time.time() - start)

# np_arr = np.arange(4) * 2
# print(np_arr)