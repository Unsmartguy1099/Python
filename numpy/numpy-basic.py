import numpy as np

a = np.array([1,2,3])
print(a)

b =  np.array([[1.0,2.0,5.0],[23.0,1,9]])
print(b)

print(a.ndim)
print(b.ndim)
print(a.shape)
print(b.shape)

c =  np.array([[1.0,2.0,5.0],[23.0,1,9],[3,4,0]])

print(c.shape)

print(a.dtype)
print(b.dtype)

print(a.itemsize) #a single item size in bytes
print(b.itemsize)

aa = np.array([1,2,3,1,0],dtype='int16') #setting size for a single item
print(aa.itemsize)

print(aa.size*aa.itemsize) #size of the array in byte

##------------------------------------------------------------------
##--changing/accessng specific elements, rows, columns, etc---------

ab = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(ab)
print(ab.shape)

print(ab[1,5]) #accessing element
print(ab[1,:]) #getting a specific row
print(ab[:,2]) #getting a specific column

#[columns, startindex:endindex:stepsize]
print(ab[0,1:6:2])
print(ab[0,1:6])
print(ab[0,1:-1:2])

ab[1,5] = 70
print(ab)

ab[:,2] = 2
print(ab)

ab[1,:] = 2
print(ab)

ab[:,2] = [9,9]
print(ab)

#3d example------------------------------
d = np.array([[[1,2,3],[4,5,6]],
              [[7,8,9],[10,11,12]],
              [[13,14,15],[16,17,18]]])
print(d)

#get specific element
print(d[1,1,2])
print(d[:,1,:])
print(d[:,1,2])

d[:,1,2] = [1001,1011,1111] #input have to have same dimensions

print(d)

d[:,1,:]=[[ 1,  1,  1],
 [1, 1, 1],
 [1, 1, 1]]

print(d)

##----------------------------------------------------------------
##--initializing different types of arrays------------------------

z = np.zeros(5)
print(z)

z = np.zeros([2,3,3])
print(z)

z = np.ones([2,3,3],dtype="int32") #integer type
print(z)

z = np.full([2,2,2],99)
print(z)

z = np.full([2,2,2],99.0) #minimum 2 parameters
print(z)

z = np.full([2,2,2],99,dtype="float32")
print(z)
#-----------------------
z2 = np.full(z.shape,8)
print(z2)
#same
z2 = np.full_like(z,8) #also copies type
print(z2)
#----------------------

r = np.random.rand(2,3,3)
print(r)

r = np.random.random_sample(z.shape)
print(r)

r = np.random.randint(7,size = (10,10)) #1st parameter 7 means each number is from 0 to 6
print(r)

r = np.random.randint(2,7,size = (10,10)) #random numbers from 2-6
print(r)

r = np.random.randint(-3,4,size = (10,10)) 
print(r)

i = np.identity(5)
print(i)

i = np.identity(5,dtype="int32")
print(i)

#repeating
arr = np.array([[1,2,3]])
rp = np.repeat(arr,4,axis=0)
print(rp)
rp = np.repeat(arr,4,axis=1)
print(rp)

output = np.ones([5,5],dtype="int32")
z = np.zeros([3,3],dtype="int32")
z[1,1] = 9

output[1:4,1:4] = z #we can put -1 instead of 4
print(output)

#copying----------------------------------------

a = np.array([1,2,3])
b = a #! reference copy
b[0] = 100
print(a) #! reference copy, we didn't copy data
print(b) 

c = a.copy() #just data copy
b[0] = 55
print(c) 
print(b) 

#mathematics--------------------------------------
a = np.array([1,2,3,4])
print(a)

a=a+2
print(a)
a=a-2
print(a)
a=a/2
print(a)
a=a*2
print(a)

b = np.array([10,10,10,10])
b = a+b
b = np.array(b,dtype="int32")
print(b)

b = b**3
print(b)

b = np.sin(b)
print(b)

#Linear Algebra--------------------------

a = np.ones([2,3],dtype="int32")
b = np.full([3,2],2)
print(a,b)

mul = np.matmul(a,b)
print(mul)

det = np.linalg.det(mul)
print(det)

#statistics---------------------------------
stats = np.array([[1,2,3],[4,5,6]])

stat = np.min(stats)
print(stat)

stat = np.min(stats,axis=1) # min of both row
print(stat)

stat = np.max(stats,axis=1)
print(stat)

sm = np.sum(stats, axis=0)
print(sm)

sm = np.sum(stats)
print(sm)

#reorganizing array---------------------------
before = np.array([[1,2,3,4],[5,6,7,8]])
print(before)

after = before.reshape([8,1]) #multiplication of new dimensions have to be similar to multiplication of new dimensions
print(after)

after = before.reshape([4,2])
print(after)

v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])

stack = np.vstack([v1,v2])
print(stack)

h1 = np.array([1,2,3,4])
h2 = np.array([5,6,7,8])
stack = np.hstack([v1,v2])
print(stack)

#load data from file--------------------------
f = np.genfromtxt('data.txt',delimiter=',')
print(f)

f= f.astype('int32')
print(f)

#boolean masking and advanced indexing---------------------------
bl = f>10
print(bl)

i = f[f>11]
print(i)

i = np.any(f>17, axis=0) # 0=columns, 1=rows
print(i)

#i = f[f<11] & f[f>3]

print(i)

#indexing with a list
a = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
a=a[[1,2,4]]
print(a)