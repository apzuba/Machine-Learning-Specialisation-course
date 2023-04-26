import numpy as np


def compute_entropy(y):

    entropy = 0.

    n = y.shape[0]
    pos = np.count_nonzero(y)
    p_1 = pos/n

    if p_1 == 0 or p_1 == 1:
        entropy = 0
    else:
        entropy = -p_1*np.log2(p_1) - (1 - p_1)*np.log2(1 - p_1)     
    
    return entropy

def split_dataset(X, node_indices, feature):

    left_indices = []
    right_indices = []
    
    for i in node_indices:
        curr_val = X[i,feature]
        if curr_val == 1:
            left_indices.append(i)
        elif curr_val == 0:
            right_indices.append(i)
        
    return left_indices, right_indices



X = np.array([[1,1,1],[1,0,1],[1,0,0],[1,0,0],[1,1,1],[0,1,1],[0,0,0],[1,0,1],[0,1,0],[1,0,0]])
root_indices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = np.array([1,1,0,0,1,0,0,1,1,0])

left_indices = np.where(X[:,0] != 0)[0]
right_indices = np.delete(root_indices, left_indices)

