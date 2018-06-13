# 1. Include a section with your name
## HW 2: Lucy Liu   
# ------------------------------------------------

# 2. Create matrix A with size (3,5) containing random numbers A = np.random.random(15)
from numpy import matrix, array, random, min, max
A = random.random(15)  
A = A.reshape(3,5)
A = matrix(A)

# 3. Find the size and length of matrix A
A.size
len(A)

# 4. Resize (crop/slice) matrix A to size (3,4)
A = A[0:3,0:4]

# 5. Find the transpose of matrix A and assign it to B
B = A.T

# 6. Find the minimum value in column 1 of matrix B
B[:, 1].min()

# 7. Find the minimum and maximum values for the entire matrix A
A.min()
A.max()

# 8. Create vector X (an array) with 4 random numbers
X = array([random.random(4)])

# 9. Create a function and pass vector X and matrix A in it
def function_hw2(a, b):
    return a*b.T

# 10. in the new function multiply vector X with matrix A 
# and assign the result to D
D = function_hw2(X, A)

# 11. Create a complex number Z with absolute and real parts != 0
Z = 6+5j

# 12. Show its real and imaginary parts as well as its absolute value
Z.real
Z.imag
abs(Z)

# 13. Multiply result D with the absolute value of Z and record it to C
C = D*abs(Z)

# 14. Convert matrix B from a matrix to a string and overwrite B
B = str(B)

# 15. Display a text on the screen: ‘Your Name is done with HW2‘
print('%s is done with WH2' %'Lucy Liu')
