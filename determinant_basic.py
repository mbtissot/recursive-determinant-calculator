import numpy as np
import random
from determinant_functions import *

'''

With the block of code below, you will create a n x n matrix
with integer entries from -k to k.

'''
n = 3
k = 50
matrix_to_calculate = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        matrix_to_calculate[i][j] = random.randint(-k,k)

''' 

Or maybe you want to find the determinant of a given matrix (actually useful).
To do this, you can follow the same pattern of the matrix below.
Follow the same pattern. If you want to increase/decrease the rank of the matrix,
simply add another row and column, or remove one row and column.

'''

'''

matrix_to_calculate = np.array([[10, 1, 8],
                                [-20, 0, 15],
                                [0, 12, 15]])

'''

determinante = determinant(matrix_to_calculate)
print('Original matrix: \n{}'.format(matrix_to_calculate))
print('Determinant: {}'.format(determinante))