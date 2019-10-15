import numpy as np
a = np.array([1,2])
b = np.array([2,1])

z = np.log(a) 
print(z)

z = np.exp(a)
print(z)

z = np.sqrt(a)
print(z)

z = np.dot(a,b)
z = a.dot(b)
print(z)

#to find magnitude of a

z = np.linalg.norm(a)
print(z)

#angle b/w two vectors

cosangle = a.dot(b) / np.linalg.norm(a) * np.linalg.norm(b)
print(cosangle)

# to print angle in radian
angle = np.arccos(cosangle)
print(angle)

#official documntation is against using matrix
#so we convert matrix into array

a = np.matrix([[1,2,3],[4,5,6]])
print(a)
print(a[0,0])
x = np.array(a)
print(x)
print(x.T) #transpose

#to primt 1-D array of zeros
z = np.zeros(5)
print(z)

m = np.zeros((2,2)) #5×5 matrix of zeros
#print(m)

#for 1's
o = np.ones((3,3))
#print(o)

#no from random varuable b/w 0 & 1
r = np.random.random((2,2))
#print(r)  #matrix 2×2 of random no. b/w 0&1

#no from gaussian distribution
#with mean 0 and variance 1
h = np.random.randn(2,2)
print(h)

#for mean and variance
print(h.mean())
print(h.var())

p = np.array([[1,2,3],[2,2,1],[6,7,9]])
q = np.array([[4,5],[6,7],[6,8]])

r = p.dot(q)
#print(r)

#to find incverse
pinv = np.linalg.inv(p)
print(pinv)

# to check if inverse is correct
 #we multiply it by array
#if we get identity matrix thn right

correct = p.dot(pinv)
print(correct)

#matrix determinent

#to find determinent of an array
d = np.linalg.det(p)
print(d)

#diagonal of matrix

di = np.diag(p)
#print(di)

#to make diagonal matrix

x = np.diag([1,2,3,4])
#print(x)

#trace of a matrix

x = np.trace(x)
#print(x)
    
    