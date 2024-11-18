import numpy as np

# Given an array, rotate the array to the right by k steps, where k is non-negative. 


import numpy as np

def rotate_array(arr, k):
    """
    Rotates the array to the right by k steps.
    arr: Input numpy array
    k: Number of steps to rotate
    return: Rotated numpy array
    """
  
    return np.concatenate((arr[-k:], arr[:-k]))


arr = np.array([1, 2, 3, 4, 5, 6, 7])
k = 2

rotated_arr = rotate_array(arr, k)
print(f"Rotate {k} steps to the right:", rotated_arr)

