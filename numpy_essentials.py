# learn how to use Numpy(Numerical Python)
#Useful for mathematical operations and faster operations on numpy arrays
#Lists vs numpy arrays - time taken

import numpy as np
from time import process_time

# Lists vs Numpy Arrays - Time Taken

# Lists
python_list = [i for i in range(10000)]
start_time = process_time()
python_list = [i + 5 for i in python_list]
end_time = process_time()
print("List operation time:", end_time - start_time)

# Numpy Array
np_array = np.array([i for i in range(10000)])
start_time = process_time()
np_array += 5
end_time = process_time()
print("Numpy array operation time:", end_time - start_time)

# Lists and Arrays
list1 = [1, 2, 3, 4, 5]
print("Python list:", list1)
print("Type of list1:", type(list1))

np_array = np.array([1, 2, 3, 4, 5])
print("NumPy array:", np_array)
print("Type of np_array:", type(np_array))

# Creating 1D and 2D Arrays
a = np.array([1, 2, 3, 4, 5])
print("Array a:", a)
print("Shape of a:", a.shape)

b = np.array([(1, 2, 3, 4), (5, 6, 7, 8)])
print("Array b:\n", b)
print("Shape of b:", b.shape)

c = np.array([(1, 2, 3, 4), (5, 6, 7, 8)], dtype=float)
print("Array c:\n", c)

# Initial Placeholders in NumPy Arrays
# Create a numpy array of zeros
x = np.zeros((4, 5))
print("Array x of zeros:\n", x)

# Create a numpy array of ones
y = np.ones((3, 3))
print("Array y of ones:\n", y)

# Create a numpy array of a particular value
m = np.full((5, 4), 5)
print("Array m with value 5:\n", m)

# Create an identity matrix using numpy
n = np.eye(5)
print("Identity matrix n:\n", n)

# Create a numpy array with random values
o = np.random.random((3, 4))
print("Array o with random values:\n", o)

# Create a random integer value array within a specific range
p = np.random.randint(10, 100, (3, 5))  # Range of 10 - 100 for a 3x5 array
print("Random integer array p:\n", p)

# Array of evenly spaced values
q = np.linspace(10, 30, 5)  # Values between 10 and 30 with 5 values evenly spaced
print("Array q of evenly spaced values:\n", q)

# Array of evenly spaced values with steps
r = np.arange(10, 30, 5)  # Values between 10 - 30 with a step of 5
print("Array r with steps:\n", r)

# Convert a list to a NumPy array
list2 = [10, 20, 20, 20, 30, 40, 50]
np_array = np.asarray(list2)
print("Converted NumPy array from list2:\n", np_array)

# Analyzing a NumPy Array
z = np.random.randint(10, 90, (5, 5))
print("Array z:\n", z)
print("Shape of z:", z.shape)  # Array dimension
print("Number of dimensions:", z.ndim)  # Number of dimensions
print("Number of elements in the array:", z.size)  # Number of elements
print("Data type of the array:", z.dtype)  # Data type of the values

# Mathematical Operations on a NumPy Array
print("Concatenated lists (list1 + list2):", list1 + list2)  # Concatenates/joins the two lists

a = np.random.randint(0, 10, (3, 3))
b = np.random.randint(10, 20, (3, 3))

print("Array a:\n", a)
print("Array b:\n", b)
print("a + b:\n", a + b)
print("a - b:\n", a - b)
print("a * b:\n", a * b)
print("a / b:\n", a / b)

# Or
print("Using NumPy functions:")
print("a + b:\n", np.add(a, b))
print("a - b:\n", np.subtract(a, b))
print("a * b:\n", np.multiply(a, b))
print("a / b:\n", np.divide(a, b))

# Array Manipulation
a = np.random.randint(0, 30, (2, 3))
a_transpose = np.transpose(a)
print("Transposed array:\n", a_transpose)
print("Shape of transposed array:", a_transpose.shape)
print("Number of dimensions of transposed array:", a_transpose.ndim)

trans2 = a_transpose.T
print("Transposed back:\n", trans2)
print("Shape of transposed back array:", trans2.shape)
print("Number of dimensions of transposed back array:", trans2.ndim)

# Reshaping an Array
b = a.reshape(3, 2)
print("Reshaped array:\n", b)
print("Shape of reshaped array:", b.shape)
