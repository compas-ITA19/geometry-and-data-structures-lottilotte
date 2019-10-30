# Assignment 2, Geometry - Task 3:
# Define a function for computing the cross products of two arrays of vectors.
#   i. The input arrays have the same length (same number of vectors).
#   ii. Prototype in pure Python (loop over the arrays).
#   iii. Make Numpy equivalent without loops.

__author__ = "Lotte Aldinger"
__email__ = "aldinger@arch.ethz.ch"
__date__ = "30.10.2019"

from numpy import array
from numpy import cross
from numpy import random
from compas.geometry import cross_vectors

# ==============================================================================
# Functions
# ==============================================================================

def crossproduct_python(array1, array2):
    """
    Compute cross products for two arrays of vectors with a for loop and using the compas cross product function.

   Parameters
    ----------
    array1 : Numpy array of vectors. 
    array2 : Numpy array of vectors. 

    Returns
    -------
    Array
        Array with cross products of the two numpy arrays.
    """
    if len(array1) == len(array2):
        return array([cross_vectors(ui, vi) for ui, vi in zip(array1, array2)])
    else:
        print("Error: Arrays don't have the same length. ")
        return None

def crossproduct_numpy(array1, array2):
    """
    Compute cross products for two arrays of vectors with numpy.

   Parameters
    ----------
    array1 : Numpy array of vectors. 
    array2 : Numpy array of vectors. 

    Returns
    -------
    Array
        Array with cross products of the two numpy arrays.
    """
    if len(array1) == len(array2):
        return cross(array1, array2)
    else:
        print("Error: Arrays don't have the same length. ")
        return None

# ==============================================================================
# Input and Output
# ==============================================================================

# test with manual generation of vector array
u1 = [1, 0, 0]
u2 = [2, 0, 0]

v1 = [0, 1, 0]
v2 = [0, 2, 0]

a1 = array([u1, u2])
a2 = array([v1, v2])

print(a1)
print(a2)

a3_py = crossproduct_python(a1, a2)
print(a3_py)

a3_np = crossproduct_numpy(a1, a2)
print(a3_np)

print(a3_py == a3_np) # verify results

# test with random numpy generation vector array with n vectors
n = 3
b1 = random.random((n,3))
b2 = random.random((n,3))

print(b1)
print(b2)

b3_py = crossproduct_python(b1, b2)
print(b3_py)

b3_np = crossproduct_numpy(b1, b2)
print(b3_np)

print(b3_py == b3_np) # verify results
