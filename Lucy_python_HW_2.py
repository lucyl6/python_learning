
# Hong Liu   # Include a section with your name
 
import numpy as np
from numpy import matrix as mx
A = np.random.random(15)  # Create matrix A with size (3,5) containing random numbers A = np.random.random(15)
A = A.reshape(3,5)
A = mx(A)


A.size  # Find the size of matrix A
len(A)  # Find the length of matrix A


A.resize((3,4))   # Resize (crop/slice) matrix A to size (3,4)


B = A.transpose()   # Find the transpose of matrix A and assign it to B


B[:, 0].min()    # Find the minimum value in column 1 of matrix B


A.min()   # Find the minimum values for the entire matrix A
A.max()   # Find the maximum values for the entire matrix A


X = np.random.random(4)    # Create vector X (an array) with 4 random numbers


from numpy import dot
def my_calculate(A, X):           # Create a function and pass vector X and matrix A in it
    D = dot(A, A.T)*dot(X, X.T)   # multiply vector X with matrix A and assign the result to D
    return D


Z = np.ndarray(shape=(2,3,2), dtype=complex)     # Create a complex number Z with absolute and real parts != 0


Z.real    # Show its real parts value
Z.imag    # Show its imaginary parts value
abs(Z)    # Show its absolute value


C = D*abs(Z)    # Multiply result D with the absolute value of Z and record it to C


B = np.array2string(B)   # Convert matrix B from a matrix to a string and overwrite B


print("Lucy Liu is done with WH2")    # Display a text on the screen: ‘Your Name is done with HW2‘
