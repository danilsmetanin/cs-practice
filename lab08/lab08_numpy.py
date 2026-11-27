import numpy as np

hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3)

print("hours:", hours)
print("shape:", hours.shape)
print("ndim:", hours.ndim)
print("size:", hours.size)
print("dtype:", hours.dtype)
print("line:", line)
print("zeros:", zeros)
print("unknown_table:")
print(unknown_table)
print("identity:")
print(identity)

print("third:", hours[2])
print("last:", hours[-1])
print("2-5:", hours[2:6])
print("every second:", hours[::2])
print("reversed:", hours[::-1])

temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])

print("shape:", temperatures.shape)
print("ndim:", temperatures.ndim)
print("size:", temperatures.size)
print("element:", temperatures[1, 2])
print("first row:", temperatures[0])
print("last column:", temperatures[:, -1])
print("first two rows without first column:")
print(temperatures[:2, 1:])
print("center 2x2:")
print(temperatures[0:2, 1:3])

matrix = np.arange(1, 26).reshape(5, 5)

print("first three rows:")
print(matrix[:3])
print(matrix[:3].shape)

print("last two rows:")
print(matrix[-2:])
print(matrix[-2:].shape)

print("first two columns:")
print(matrix[:, :2])
print(matrix[:, :2].shape)

print("rows 1-3, columns 2-4:")
print(matrix[1:4, 2:5])
print(matrix[1:4, 2:5].shape)

print("bottom right 2x2:")
print(matrix[-2:, -2:])
print(matrix[-2:, -2:].shape)

vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9

print("vector:", vector)
print("small matrix:")
print(small_matrix)

# copy() нужен, чтобы не изменить исходный hours
changed_hours = hours.copy()
changed_hours[2:5] = 99
changed_hours[::2] = -1

print("changed hours:", changed_hours)
print("hours:", hours)

changed_matrix = matrix.copy()
changed_matrix[1, :] = 0
changed_matrix[:, -1] = -1
changed_matrix[1:4, 1:4] = 100

print("changed matrix:")
print(changed_matrix)
print("matrix:")
print(matrix)

numbers = np.arange(12)
table = numbers.reshape(3, 4)
transposed = table.T

print("numbers:", numbers.shape)
print("table:", table.shape)
print("transposed:", transposed.shape)
print(table)
print(transposed)

# 3 * 4 = 12, поэтому reshape(3, 4) работает.
# 5 * 3 = 15, а элементов 12, поэтому reshape(5, 3) даст ошибку.
