import numpy as np

#* creating arrays--------------------
# create a list named list1
list1 = [2, 4, 6, 8]
print(list1)

# create numpy array using list1
array1 = np.array(list1)
print(array1)
# Output: [2 4 6 8]

# create numpy array using a list
array1 = np.array([2, 4, 6, 8])
print(array1)
# Output: [2  4  6 8]

# create an array with 4 elements filled with zeros
array1 = np.zeros(4) 
print(array1)
# Output: [0. 0. 0. 0.]

# create an array with 4 elements filled with zeros(type defined)
array1 = np.zeros(4,dtype="int32") 
print(array1)
# Output: [0. 0. 0. 0.]

# create an array with 4 elements filled with ones(type defined)
array1 = np.ones(4,dtype="int32") 
print(array1)
# Output: [0. 0. 0. 0.]

# create an array with values from 0 to 4
array1 = np.arange(5)
print("Using np.arange(5):", array1)

# create an array with values from 1 to 8 with a step of 2
array2 = np.arange(1, 9, 2)
print("Using np.arange(1, 9, 2):",array2)

# generate an array of 5 random numbers
array1 = np.random.rand(5)
print(array1)

# create an empty array of length 4
array1 = np.empty(4)
print(array1)


#* creating N-D arrays--------------------
# create a 2D array with 2 rows and 4 columns
array1 = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8]])
print(array1)

# create a 3D array with 2 "slices", each of 3 rows and 4 columns
array1 = np.array([[[1, 2, 3, 4],
                [5, 6, 7, 8], 
                [9, 10, 11, 12]],
                     
                [[13, 14, 15, 16], 
                 [17, 18, 19, 20], 
                 [21, 22, 23, 24]]])
print(array1)

# create 2D array with 2 rows and 3 columns filled with zeros
array1 = np.zeros((2, 3))
print("2-D Array: ")
print(array1)

# create 3D array with dimensions 2x3x4 filled with zeros
array2 = np.zeros((2, 3, 4))
print("\n3-D Array: ")
print(array2)

# Create a 2-D array with elements initialized to 5 
numpy_array = np.full((2, 2), 5)
print("Array:", numpy_array)

# create a 2D array of 2 rows and 2 columns of random numbers
array1 = np.random.rand(2, 2)
print("2-D Array: ")
print(array1)

# create a 3D array of shape (2, 2, 2) of random numbers
array2 = np.random.rand(2, 2, 2)
print("\n3-D Array: ")
print(array2)

# create an empty 2D array with 2 rows and 2 columns
array1 = np.empty((2, 2))
print("2-D Array: ")
print(array1)

# create an empty 3D array of shape (2, 2, 2) 
array2 = np.empty((2, 2, 2))
print("\n3-D Array: ")
print(array2)


#* data types--------------------
#&-2. int8, int16, int32, int64 - signed integer types with different bit sizes
#&-3. uint8, uint16, uint32, uint64 - unsigned integer types with different bit sizes
#&-4. float32, float64 - floating-point types with different precision levels
#&-5. complex64, complex128 - complex number types with different precision levels

# create an array of integers 
array1 = np.array([2, 4, 6])
# check the data type of array1
print(array1.dtype) 
# Output: int64

# create an array of  integers
int_array = np.array([-3, -1, 0, 1])
# create an array of floating-point numbers
float_array = np.array([0.1, 0.2, 0.3])
# create an array of complex numbers
complex_array = np.array([1+2j, 2+3j, 3+4j])

# check the data type of int_array
print(int_array.dtype)  # prints int64
# check the data type of float_array
print(float_array.dtype)  # prints float64
# check the data type of complex_array
print(complex_array.dtype)  # prints complex128

# create an array of 32-bit integers
array1 = np.array([1, 3, 7], dtype='int32')
print(array1, array1.dtype)

# create an array of 8-bit integers
array1 = np.array([1, 3, 7], dtype='int8')
# create an array of unsigned 16-bit integers
array2 = np.array([2, 4, 6], dtype='uint16')
# create an array of 32-bit floating-point numbers
array3 = np.array([1.2, 2.3, 3.4], dtype='float32')
# create an array of 64-bit complex numbers
array4 = np.array([1+2j, 2+3j, 3+4j], dtype='complex64')

# print the arrays and their data types
print(array1, array1.dtype)
print(array2, array2.dtype)
print(array3, array3.dtype)
print(array4, array4.dtype)

#create an array of integers
int_array = np.array([1, 3, 5, 7])
# convert data type of int_array to float
float_array = int_array.astype('float')
# print the arrays and their data types
print(int_array, int_array.dtype)
print(float_array, float_array.dtype)


#* array attributes--------------------
#&-1. ndim -	 returns number of dimension of the array
#&-2. size -	 returns number of elements in the array
#&-3. dtype -	 returns data type of elements in the array
#&-4. shape -	 returns the size of the array in each dimension.
#&-5. itemsize - returns the size (in bytes) of each elements in the array
#&-6. data -     returns the buffer containing actual elements of the array in memory

# create a 2-D array 
array1 = np.array([[2, 4, 6],
                  [1, 3, 5]])
# check the dimension of array1
print(array1.ndim) 
# Output: 2

array1 = np.array([[1, 2, 3],
                 [6, 7, 8]])
# return total number of elements in array1
print(array1.size)
# Output: 6

array1 = np.array([[1, 2, 3],
                [6, 7, 8]])
# return a tuple that gives size of array in each dimension
print(array1.shape)
# Output: (2,3)

# create an array of integers 
array1 = np.array([6, 7, 8])
# check the data type of array1
print(array1.dtype) 
# Output: int64

# create a default 1-D array of integers
array1 = np.array([6, 7, 8, 10, 13], dtype=np.int64)
# create a 1-D array of 32-bit integers 
array2 = np.array([6, 7, 8, 10, 13], dtype=np.int32)
# use of itemsize to determine size of each array element of array1 and array2
print(array1.itemsize)  # prints 8
print(array2.itemsize)  # prints 4 (by default 4)

array1 = np.array([6, 7, 8])
array2 = np.array([[1, 2, 3],
                   	    [6, 7, 8]])
# print memory address of array1's and array2's data
print("\nData of array1 is: ",array1.data)
print("Data of array2 is: ",array2.data)


#* input output--------------------
#& NumPy offers input/output (I/O) functions for loading and saving data to and from files.
#& 1. The binary format is designed for efficient storage and retrieval of large arrays.
#& 2. The text format is more human-readable and can be easily edited in a text editor.

#& functions
#& 1. save() -      saves an array to a binary file in the NumPy .npy format.
#& 2. load() -      loads data from a binary file in the NumPy .npy format
#& 3. savetxt() -   saves an array to a text file in a specific format
#& 4. loadtxt() -	loads data from a text file.

# create a NumPy array
array1 = np.array([[1, 3, 5], 
                   [7, 9, 11]])
# save the array to a file
np.save('file1.npy', array1)

# load the saved NumPy array
loaded_array = np.load('file1.npy')
# display the loaded array
print(loaded_array)

# create a NumPy array
array2 = np.array([[1, 3, 5], 
                   [7, 9, 11]])
# save the array to a file
np.savetxt('file2.txt', array2)

# load the saved NumPy array
loaded_array = np.loadtxt('file2.txt')
# display the loaded array
print(loaded_array)


#* array indexing--------------------
array1 = np.array([1, 3, 5, 7, 9])
# access numpy elements using index
print(array1[0])    # prints 1
print(array1[2])    # prints 5
print(array1[4])    # prints 9

# create a numpy array
numbers = np.array([2, 4, 6, 8, 10])
# change the value of the first element
numbers[0] = 12
print("After modifying first element:",numbers)    # prints [12 4 6 8 10]
# change the value of the third element
numbers[2] = 14
print("After modifying third element:",numbers)    # prints [12 4 14 8 10]

#& negative array indexing
#& array ->           1  3  5  7  9 
#& index ->           0  1  2  3  4
#& negative index -> -5 -4 -3 -2 -1

# create a numpy array
numbers = np.array([1, 3, 5, 7, 9])
# access the last element
print(numbers[-1])    # prints 9
# access the second-to-last element
print(numbers[-2])    # prints 7

# create a numpy array
numbers = np.array([2, 3, 5, 7, 11])
# modify the last element
numbers[-1] = 13
print(numbers)    # Output: [2 3 5 7 13]
# modify the second-to-last element
numbers[-2] = 17
print(numbers)    # Output: [2 3 5 17 13]

# create a 2D array 
array1 = np.array([[1, 3, 5, 7], 
                       [9, 11, 13, 15],
                       [2, 4, 6, 8]])
# access the element at the second row and fourth column
element1 = array1[1, 3]  # returns 15
print("4th Element at 2nd Row:",element1)  
# access the element at the first row and second column
element2 = array1[0, 1]  # returns 3
print("2nd Element at First Row:",element2)  

# create a 2D array 
array1 = np.array([[1, 3, 5], 
             [7, 9, 2], 
             [4, 6, 8]])
# access the second row of the array
second_row = array1[1, :]
print("Second Row:", second_row)  # Output: [7 9 2]
# access the third column of the array
third_col = array1[:, 2]
print("Third Column:", third_col)  # Output: [5 2 8]

#& To access an element of a 3D array, we use three indices separated by commas
#& 1. The first index refers to the slice
#& 2. The second index refers to the row
#& 3. The third index refers to the column. 

# create a 3D array with shape (2, 3, 4)
array1 = np.array([[[1, 2, 3, 4], 
                   [5, 6, 7, 8], 
                   [9, 10, 11, 12]],
                     
                    [[13, 14, 15, 16], 
                    [17, 18, 19, 20], 
                    [21, 22, 23, 24]]])
# access a specific element of the array
element = array1[1, 2, 1]
# print the value of the element
print(element) 
# Output: 22

element = array1[1,:,:]
print(element) 
element = array1[:,2,:]
print(element) 
element = array1[:,:,1]
print(element) 


#* array slicing--------------------
#& array[start:stop:step] default step size is 1

# create a 1D array 
array1 = np.array([1, 3, 5, 7, 8, 9, 2, 4, 6])

# slice array1 from index 2 to index 6 (exclusive)
print(array1[2:6])  # [5 7 8 9]

# slice array1 from index 0 to index 8 (exclusive) with a step size of 2
print(array1[0:8:2])  # [1 5 8 2]

# slice array1 from index 3 up to the last element
print(array1[3:])  # [7 8 9 2 4 6]

# items from start to end
print(array1[:])   # [1 3 5 7 8 9 2 4 6]


# create a numpy array
numbers = np.array([2, 4, 6, 8, 10, 12])
# modify elements from index 3 onwards
numbers[3:] = 20
print(numbers)
# Output: [ 2  4  6 20 20 20]

# create a numpy array
numbers = np.array([2, 4, 6, 8, 10, 12])
# modify the first 3 elements
numbers[:3] = 40
print(numbers)
# Output: [40 40 40  8 10 12]

# create a numpy array
numbers = np.array([2, 4, 6, 8, 10, 12])
# modify elements from indices 2 to 5
numbers[2:5] = 22
print(numbers)
# Output: [2 4 22 22 22 12]

# create a numpy array
numbers = np.array([2, 4, 6, 8, 10, 12])
# modify every second element from indices 1 to 5
numbers[1:5:2] = 16
print(numbers)
# Output: [ 2 16  6 16 10 12]

# create a numpy array
numbers = np.array([2, 4, 6, 8, 10, 12])

# slice the last 3 elements of the array
# using the start parameter
print(numbers[-3:])    # [8 10 12]
# slice elements from 2nd-to-last to 4th-to-last element
# using the start and stop parameters
print(numbers[-5:-2])    # [4 6 8] 
# slice every other element of the array from the end
# using the start, stop, and step parameters
print(numbers[-1::-2])   # [12 8 4]

#& Reverse NumPy Array Using Negative Slicing
# create a numpy array
numbers = np.array([2, 4, 6, 8, 10, 12])
# generate reversed array
reversed_numbers = numbers[::-1]
print(reversed_numbers)
# Output: [12 10 8 6 4 2]

#& 2D NumPy Array Slicing
#& array[row_start:row_stop:row_step, col_start:col_stop:col_step]
# create a 2D array
array1 = np.array([[1, 3, 5, 7], 
                   [9, 11, 13, 15]])
print(array1[:2, :2])

# create a 2D array 
array1 = np.array([[1, 3, 5, 7], 
                      [9, 11, 13, 15],
                      [2, 4, 6, 8]])
# slice the array to get the first two rows and columns
subarray1 = array1[:2, :2]
# slice the array to get the last two rows and columns
subarray2 = array1[1:3, 2:4]
# print the subarrays
print("First Two Rows and Columns: \n",subarray1)
print("Last two Rows and Columns: \n",subarray2)


#* numPy array reshaping--------------------
#& np.reshape(array, newshape, order = 'C')
#& orders C,F,A

array1 = np.array([1, 3, 5, 7, 2, 4, 6, 8])
# reshape a 1D array into a 2D array 
# with 2 rows and 4 columns
result = np.reshape(array1, (2, 4))
print(result)

# reshape a 1D array into a 2D array 
# with 4 rows and 2 columns
array1 = np.array([1, 3, 5, 7, 2, 4, 6, 8])
result1 = np.reshape(array1, (4, 2))
print("With 4 rows and 2 columns: \n",result1)

# reshape a 1D array into a 2D array with a single row
result2 = np.reshape(array1, (1, 8))
print("\nWith a single row: \n",result2)

# create a 1D array
array1 = np.array([1, 3, 5, 7, 2, 4, 6, 8])
# reshape the 1D array to a 3D array
result = np.reshape(array1, (2, 2, 2))
# print the new array
print("1D to 3D Array: \n",result)

#& Flatten N-d Array to 1-D Array Using reshape()
# flatten 2D array to 1D
array1 = np.array([[1, 3], [5, 7], [9, 11]])
result1 = np.reshape(array1, -1)
print("Flattened 2D array:", result1)
# flatten 3D array to 1D
array2 = np.array([[[1, 3], [5, 7]], [[2, 4], [6, 8]]])
result2 = np.reshape(array2, -1)
print("Flattened 3D array:", result2)

