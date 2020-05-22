# CodeByintrastudy_sb
import numpy

np.set_printoptions(legacy='1.13')

N = int(input())
#for i in range(0,N)
#a = np.array()

'''np.set_printoptions(legacy='1.13')

N = int(input())

A = np.array([input().split() for i in range(N)], float)
print(np.linalg.det(A))'''
numpy.set_printoptions(legacy='1.13')

N = int(input())

A = numpy.array([input().split() for i in range(N)], float)
print(numpy.linalg.det(A))
