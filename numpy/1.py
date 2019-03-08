import numpy as np
s = [1,2,3,4,5,6,7]
nps = np.array(s)
print(nps[4])
list = [2,34.3,54,6,7]
print(np.array(list))
# print(np.eye(6))
print(np.array([[34,56,23,89], [11,45,76,34]]).dtype)
npss = nps[1: 4]
npss[2] = 10000000
print(s, nps, npss)
three_d_arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
copied_values = three_d_arr[0].copy() 
three_d_arr[0]= 99  

print ("New value of three_d_arr: {}".format(three_d_arr)) 
three_d_arr[0] = copied_values
print(" three_d_arr again: {}".format(three_d_arr))
matrix_arr =np.array([[3,4,5],[6,7,8],[9,5,1]])
print("+++++++++=\n",matrix_arr[:, :2])
print(matrix_arr==[3])