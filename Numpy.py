# Practise:1

'''from numpy import *

arr = array([1, 2, 3, 4, 5, 6],int)
print(arr)'''

# CodeByintrastudy_sb
# Printing 2D Array
# import numpy as np
# a = np.array([(1, 2, 3), (4, 5, 6)])
# print(a)
# CodeByintrastudy_sb
import numpy as np
import time
import sys
S = range(1000)   # list
# space occupied by my list
print(sys.getsizeof(5)*len(S))
# space occupied by Numpy Array
D = np.arange(1000)
print(D.size*D.itemsize)





