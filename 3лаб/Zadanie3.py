import numpy as np
#1
vector1 = np.array([1,2,3,4,5])
vector2 = np.array([10,13,16,19,22])

print(vector1)
print(vector2)
print("-"*25)

#8
vector3 = vector1 + vector2
vector4 = np.subtract(vector2, vector1)
vector5 = vector1 * vector2

print(vector3)
print(vector4)
print(vector5)
print("-"*25)

#10
dist = np.linalg.norm(vector4)
print(dist)
print("-"*25)

#18
matr1 = np.array([1,2,2,1]).reshape(2,2)
print(matr1)
print(np.linalg.eigvals(matr1))
print("-"*25)

#23
np.random.seed()
vector23 = np.random.randint(-10,11,size=5)
prodd = np.prod(vector23)
stdd = np.std(vector23)
mini = np.min(vector23)

print(vector23)
print(prodd)
print(stdd)
print(mini)
print("-"*25)

#26
vector26 = np.random.randint(-10,200,size=5)
print(vector26)
print(np.any(vector26>100))
