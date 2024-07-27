# learn how to use Numpy(Numerical Python)
#Useful for mathematical operations and faster operations on numpy arrays
#Lists vs numpy arrays - time taken

import numpy as np
from time import process_time

#Lists
python_list = [i for i in range(10000)]
start_time = process_time
python_list = [i+5 for i in range(10000)]
end_time = process_time

print(end_time - start_time)

#Numpy Array
np_array = np.array([i for i in range(10000)])
start_time = process_time
np_array += 5
end_time = process_time

print(end_time - start_time)



#list
list1 = [1,2,3,4,5]
print(list1)
type(list1)


np_array = np.array([1,2,3,4,5])
print(np_array)
type(np_array)


#creating a 1dim array
a = np.array([1,2,3,4,5])
print(a)
a.shape

b = np.array([(1,2,3,4),(5,6,7,8)])
print(b)
b.shape

c = np.array([(1,2,3,4),(5,6,7,8)], dtype=float)
print(c)



#initial placeholders in numpy arrays
#create a numpy array of zeros

x = np.zeros((4,5))
print(x)


#create a numpy array of ones
y = np.ones((3,3))
print(y)

#create a numpy array of a particular value
m = np.full((5,4),5)
print(m)

#Create an identity matrix using numpy
n = np.eye(5)

#create a numpy array with random values
o = np.random.random(3,4)
print(0)

#create a random integer value array within a specific range
p = np.random.randint(10,100,(3,5)) #range of 10 - 100 for a 3x5 array
print(p)

#array of evenly spaced values
q = np.limspace(10,30,5) #values between 10 and 30 with 5 values and they should be evenly spaced

#array of evenly spaced values---> specifying the steps
r = np.arange(10,30,5)   # values between 10 - 30 with a step of 5


#convert a list to a numpy array
list2 = [10,20,20,20,30,40,50]
type(list2)
np_array = np.asarray(list2)
print(np_array)
type(np_array)





#Analyzing a numpy array
z = np.random.randint(10,90,(5,5))
print(z)
print(z.shape)  #array dimension
print(z.ndim)   #number of dimension
print(z.size)   #number of elements in the array
print(z.dtype)  #datatype of the values in the array


#MATHEMATICAL OPERATIONS ON A NUMPY ARRAY
print(list1 + list2)    #CONCATENATES/JOINS THE TWO LISTS

a = np.random.randint(0,10,(3,3))
b = np.random.randint(10,20,(3,3))

print(a, "\n", b)
print(a+b)
print(a-b)
print(a*b)
print(a/b)

#Or

print(np.add(a,b))
print(np.subtract(a,b))
print(np.multiply(a,b))
print(np.divide(a,b))


#ARRAY MANIPULATION
a = np.random.randint(0,30,(2,3))
a_transpose = np.transpose(a)
print(a_transpose)
print(a_transpose.shape)
print(a_transpose.ndim)

trans2 = a_transpose.T
print(trans2)
print(trans2.shape)
print(trans2.ndim)

#RESHAPING AN ARRAY
b = a.reshape(3,2)
print(b)
print(b.shape)