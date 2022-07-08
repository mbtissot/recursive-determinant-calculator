# Recursive Determinant Calculator

This code find the determinant of square matrices by reducing the size of the matrix from $N\times N$ to $(N-1)\times (N-1)$, until the final matrix is $2\times 2$. (Using recursion is inefficient and slow for actually computing determinants, use some online tool instead. I wrote it just for the fun of doing it recursively)

My favorite algorithm for finding the determinant of matrices, is using [Laplace Expansion](https://en.wikipedia.org/wiki/Laplace_expansion). For matrices bigger than $3\times 3$, it very boring to do, but usually doesn't need as much brainpower as other methods.

As its my favorite method, i tried to code a program that find the determinant by doing it. (It also uses recursion, which i find really cool, even though i am great at breaking things with it.)

## Example of Laplace Expansion

To better illustrate how to program works, we are going to compute the determinant of a general $3\times 3$ matrix below:



![Example of 3x3 determinant calculation](~/Desktop/Development/recusrive-determinant/3by3-determinant.png "3x3 Determinant")


$$ det\left(\begin{bmatrix}
        a&b&c\\d&e&f\\g&h&i
    \end{bmatrix}\right) = a   \begin{bmatrix}e & f \\h & i \end{bmatrix} - b   \begin{bmatrix}d & f \\g & i \end{bmatrix} + c  \begin{bmatrix}d & e \\g & h \end{bmatrix} \\
    = a(ei-fh) - b(ei-fg) + c(eh-eg) $$

### Some additional stuff to change on the functions file

Running the code as is, will compute the determinant of some random matrix, without showing you the 'sub-matrices', which makes this code basically pointless and inefficient, since there are quicker and easier algorithms to compute the determinant.

If you want to see the sub-matrices, open the 'determinant_functions.py' file, and uncomment the `print` statement on line 35.