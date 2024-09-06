import numpy as np #numpy == static array
arr = [1,2,3,5] # dynamic array
arr.append(10) 
arr1 = np.array([1,2,3]) #1d np array
arr2 = np.array([[1,2],[2,3]]) #2d np array 
# print(arr1[:2]) #slicing 
# print(arr[:2]) 
# print(arr[::2])# with gaps of 2
# print(arr1[::-1])# reverse 
# print(arr2[1,:1])  ## command + /

print(np.shape(arr2)) ## row and colums 
print(np.size(arr2)) ## no or elements 
print(np.ndim(arr2)) ## 2d ?? 3d ??
print(arr2.dtype)