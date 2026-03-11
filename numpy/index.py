import numpy as np

arr = np.array([1, 2, 3, 4, 5])
arr2 = np.array([1, 4, 5, 3, 3])

print(arr + arr2)
print((arr + arr2) * 2)

# shape and dimensions
print(arr.shape)
print(arr.ndim)

# indexing
print(arr[3])
print(arr[0:2])  # return the value just before till 2

# print(np.zeros((2, 3)))
# print(np.ones((2, 3)))
# print(np.eye(2))

# arrange
print(np.arange(2, 20, 4))
print(np.linspace(0, 1, 5))

#multiplication
# A = np.array([[1,2],[3,4]])
# B = np.array([[5,6],[7,8]])

# C = A @ B
# print(C)

a = np.array([1,2,3,4])

print(np.sum(a))
print(np.mean(a))
print(np.max(a))
print(np.std(a))