import numpy as np

'''

The function 'determinant' tests whether the matrix in question is square or not.
If it isn't, it prints 'Matrix is not square', and halts. 
If it is, it calls the function 'find_determinant'

'''


def determinant(matrix):
    if matrix.shape[0] == matrix.shape[1]:
        firstrow = matrix[0]
        return find_determinant(matrix, firstrow)
    else:
        print('Matriz não é quadrada.')

        
'''

Calculates the determinant recursively. It can only calculate the determinant
of 2x2 matrices, so if the matrix is bigger than 2x2, it creates sub matrices
using the function 'new_matrix' and find the determinant of the sub-matrices.

'''
def find_determinant(matrix, first_row):
    det = 0
    firstrow = matrix[0]
    if matrix.shape[0]==2:
        return (matrix[0][0]*matrix[1][1]) - (matrix[0][1]*matrix[1][0]) #2x2 determinant
    else:
        for i in range(matrix.shape[0]):
            #print(new_matrix(matrix, i)) #This prints all the sub-matrices. Uncomment if u want
            valor = ((-1)**(i))*firstrow[i]*find_determinant(new_matrix(matrix, i), firstrow)
            det = det + valor
    return det
            
'''

The function 'new_matrix' creates sub matrices of a given matrix (size NxN, with N>2)
while forgetting some row and some column of the original matrixx (See README.md)

'''
def new_matrix(matrix, n):
    newmatrix = np.zeros((matrix.shape[0]-1, matrix.shape[0]-1))
    ci = 0
    for i in range(matrix.shape[0]):
        cj = 0
        if i==0:
            continue
        else:
            ci+=1
            for j in range(matrix.shape[0]):
                if j==n:
                    continue
                else:
                    cj+=1
                    newmatrix[ci-1][cj-1] = matrix[i][j]
    return newmatrix
