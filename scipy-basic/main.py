import scipy as sp
import numpy as np
from scipy import integrate
from scipy import cluster
from scipy import fftpack
from scipy import special
from scipy import integrate
from scipy import linalg
# help(integrate)

# sp.info(fftpack)
# sp.source(cluster)


fun1 = special.kelvin(15)
print(fun1)


fun2 = special.xlogy(2, 10)
print(fun2)

fun3 = special.exp10(50)
print(fun3)

fun4 = special.sindg(60)
print(fun4)

fun5 = special.cosdg(60)
print(fun5)

print('---------------------')


def var1(x): return x**3


fun6 = integrate.quad(var1, 0, 6)
print(fun6)


def var2(y, x): return x * y**4


fun6 = integrate.dblquad(var2, 0, 6, lambda x: 0, lambda x: 1)
print(fun6)


print('---------------------')

var3 = np.array([[2, 4, 6], [1, 3, 5]])
print(var3)

trans1 = sp.fft(var3)
print(trans1)


print('---------------------')

array1 = np.array(([1, 3], [2, 4]))
array2 = np.array(([5, 9], [6, 8]))

print(array1, array2)
print('\n')
fun7 = sp.linalg.solve(array1, array2)
print(fun7)

fun8 = sp.linalg.inv(array1)
print(fun8)
