import numpy as np
a = np.array([1,2,3])
#print(a+a)
a = np.matrix([[1,2,3],[4,5,6]])
print(a)
print(a[0,0])
x = np.array(a)
print(x)
print(x.T) #transpose


z = np.zeros(5)
print(z)

m = np.zeros((5,5)) #5×5 matrix of zeros
print(m)

o = np.ones((3,3))
print(o)

r = np.random.random((2,2))
print(r)  #matrix 2×2 of random no. b/w 0&1

h = np.random.randn(2,2)
print(h)

print(h.mean())
print(h.var())

p = np.array([[1,2,3],[2,2,1],[6,7,9]])
q = np.array([[4,5],[6,7],[6,8]])

r = p.dot(q)
print(r)

pinv = np.linalg.inv(p)
print(pinv)

#check if inverse is correct
 #we multiply it by p 
#if we get identity matrix thn right

correct = p.dot(pinv)
print(correct)

#matrix determinent

d = np.linalg.det(p)
print(d)

#diagonal of matrix

di = np.diag(p)
print(di)

#to make diagonal matrix

x = np.diag([1,2])
print(x)
    
    