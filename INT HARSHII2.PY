import numpy as np

a=np.array([[1,2,3],[4,5,6]])

print(a)
print("type",type(a))

print("dimention",a.ndim)

print("shape",a.shape)
print("size",a.size)
print("datatype of elements",a.dtype)
print("itemsize",a.itemsize)

b=a.reshape(3,2)

print(b)



# Create 1-D array
a = np.arange(1,7)

print("1-D Array:")
print(a)

# Reshape into 2-D array
b = a.reshape(2,3)

print("After Reshape:")
print(b)

#

ab=np.arange(1,5)
print(ab)
p=ab.reshape(2,2)

print(p)

#

bb=np.arange(6)
print(bb)

aa=np.arange(1,5)
print(aa)
p=aa.reshape(2,2)
print(p)


#
a=np.array([1,5,3,19,13,7,3])
print(a[3])
print(a[2:5])
print(a[2::2])
print(a[::-1])


#
import numpy as np

arr = np.array([[1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10]])

print(arr[0, 1])


#
a=np.array([1,2,3,4,5,6,7,8])
a_slice = a[1:5]
a_slice[1] = 1000
print(a)

#
import numpy as np
b = np.array([1,2,5,7,8])
b[2:4]=99
print(b)

a=np.array([1,2,3,4,5,6])
print(a)

a_slice=a[2:5]
print(a_slice)
a_slice[2]=100
print("a_slice is",a_slice)
print("a is",a)#change occurs ism original
####get a copy created

aa=np.array([1,2,3,4,5,6])
print(aa)
aa_slice=aa[2:5].copy()
print(aa_slice)

aa_slice[2]=100
print("aa_slice is",aa_slice)
print(aa)


#
a = np.array( [20,30,40,50] )
b = np.arange(4)
print(b)


print
array([20,31,42,53])
