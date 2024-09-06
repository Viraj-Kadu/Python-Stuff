import numpy as np
arr = np.array([1,45,9,69,90])
print(np.arange(1,6,2,float))## start end step dtype
print(np.zeros((2,3),float)) ## 2 columns 3 rows dtype
print(np.ones((2,4))) ## 1svjust like 0s
print(np.full([2,3],69,float))## can put any number 
print(np.arange(10).reshape(2,5)) ## dimensions or reshape should give product 
                                #result as no of elements and if you dont know put -1
arr.sort()
print(arr)
