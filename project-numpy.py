import numpy as np

# 2-dimensional matrix
var1 = np.array([(2, 4, 6), (1, 3, 5)])
var2 = np.array([(2, 4, 6), (1, 3, 5)])

print(var1 + var2)

var3 = np.array([20000, 4, 6])
var4 = np.array([(20000, 4, 6), (20000, 4, 6), (20000, 4, 6), (20000, 4, 6)])

print(var3)
print(var3.itemsize)
print(var3.dtype)
print(var3.ndim)
print(var2.ndim)
print(var4.ndim)
print(var4.size)
print(var4.shape)

print('----------------------------')
var5 = np.array([(20000, 4, 6), (20000, 4, 6), (20000, 4, 6), (20000, 4, 6)])
var5 = var5.reshape(3, 4)
print(var5)


var6 = np.linspace(10, 50, 10)
print(var6)

print('----------------------------')
var7 = np.array([(2, 4, 6), (1, 3, 5), (7, 24, 21), (10, 30, 50)])
print(var7)
print(var7[0, 1])
print(var7[0:, 1])
print(var7[1:, 1])
print(var7.min())
print(var7.max())
print(var7.sum())


print('----------------------------')
var8 = np.array([(2, 4, 6), (1, 3, 5)])
var9 = np.array([(5, 9, 3), (6, 7, 15)])

print(var8+var9)
print(var8-var9)
print(var8/var9)

print(var8)
print(var8.ravel())

print(var8)
print(var8.sum(axis=0))
print(var8.sum(axis=1))

print(np.sqrt(var8))
print(np.std(var8))


print('----------------------------')
var10 = np.array([3, 6, 9])

print(np.exp(var10))
print(np.log(var10))
