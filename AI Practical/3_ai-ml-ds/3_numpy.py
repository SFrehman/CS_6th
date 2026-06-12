import numpy as np

# Creating arrays
arr = np.array([1, 2, 3, 4])                 # Create a 1D array from a list
matrix = np.array([[1, 2], [3, 4]])          # Create a 2D array (matrix)
zeros = np.zeros((3, 3))                     # Create a 3x3 matrix filled with 0s
ones = np.ones((2, 4))                       # Create a 2x4 matrix filled with 1s
full = np.full((2, 2), 7)                    # Create a 2x2 matrix filled with 7s
identity = np.eye(3)                         # Create a 3x3 identity matrix
arange = np.arange(0, 10, 2)                 # Create array from 0 to 8, stepping by 2
linspace = np.linspace(0, 1, 5)              # Create 5 evenly spaced values between 0 and 1


shape = matrix.shape                         # Get dimensions (rows, columns) -> (2, 2)
dims = matrix.ndim                           # Get number of dimensions -> 2
dtype = matrix.dtype                         # Get data type of elements -> int64
size = matrix.size                           # Get total number of elements -> 4