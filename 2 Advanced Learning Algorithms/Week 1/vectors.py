import numpy as np

A = np.array([[1,-1,0.1], [2,-2,0.2]])

AT = A.T                #transpose function

W = np.array([[3,5,7,9], [4,6,8,0]])

Z = np.matmul(AT,W)
Z = AT @ W              #the same as np.matmul


# EXAMPLE 2 - calc Dense layers

AT = np.array([[200, 17]])
W = np.array([[1, -3, 5], [-2, 4, -6]])
B = np.array([[-1, 1, 2]])

def g(x):
    result = (1/(1 + np.exp(-x)))
    result = (np.rint(result)).astype(int)
    return result

def dense(a_in, W, b):
    z = np.matmul(a_in,W) + B
    a_out = g(z)
    return a_out

dense(AT, W, B)