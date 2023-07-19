from re import U
import numpy as np



u = np.array([4, -4, -3])
v = np.array([4,2,4])

print (u)

x = np.dot(u.transpose(), v)

print (x)
