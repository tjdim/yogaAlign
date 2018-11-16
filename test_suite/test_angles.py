import sys
sys.path.append('../')
from yoga.joints import *

u = [1, 0]
v1 = [0, -1]
v2 = [0, 1]

print(u)
print(v1)
print(v2)

print(get_angles_vectors(u, v1))
print(get_angles_vectors(u, v2))
print(get_angles_vector_sign(u, v1))
print(get_angles_vector_sign(u, v2))

u = [1, 1]
v1 = [0, -1]
v2 = [0, 1]

print(u)
print(v1)
print(v2)

print(get_angles_vectors(u, v1))
print(get_angles_vectors(u, v2))
print(get_angles_vector_sign(u, v1))
print(get_angles_vector_sign(u, v2))