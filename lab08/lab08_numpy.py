import numpy as np


# Задание 1. Создание векторов и матриц
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


# Задание 2. Индексы и срезы в векторе
print("\nЗадание 2")
print("Третий элемент:", hours[2])
print("Последний элемент:", hours[-1])
print("Элементы с индексами 2-5:", hours[2:6])
print("Каждый второй элемент:", hours[::2])
print("В обратном порядке:", hours[::-1])


# Задание 3. Строки и столбцы таблицы
temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])

print("\nЗадание 3")
print("shape:", temperatures.shape)
print("ndim:", temperatures.ndim)
print("size:", temperatures.size)
print("Вторая строка, третий столбец:", temperatures[1, 2])
print("Первая строка:", temperatures[0])
print("Последний столбец:", temperatures[:, -1])
print("Первые две строки без первого столбца:")
print(temperatures[:2, 1:])
print("Центральный фрагмент 2x2:")
print(temperatures[0:2, 1:3])


# Задание 4. Прямоугольные срезы
matrix = np.arange(1, 26).reshape(5, 5)

print("\nЗадание 4")
print("Первые три строки:")
print(matrix[:3])
print("shape:", matrix[:3].shape)

print("Последние две строки:")
print(matrix[-2:])
print("shape:", matrix[-2:].shape)

print("Первые два столбца:")
print(matrix[:, :2])
print("shape:", matrix[:, :2].shape)

print("Строки 1-3 и столбцы 2-4:")
print(matrix[1:4, 2:5])
print("shape:", matrix[1:4, 2:5].shape)

print("Правый нижний угол 2x2:")
print(matrix[-2:, -2:])
print("shape:", matrix[-2:, -2:].shape)


# Задание 5. Изменение массива с помощью срезов
vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9

print("\nЗадание 5")
print("vector:", vector)
print("small_matrix:")
print(small_matrix)

# Нужен именно .copy(), потому что изменения в changed_hours
# не должны затрагивать исходный массив hours.
changed_hours = hours.copy()
changed_hours[2:5] = 99
changed_hours[::2] = -1

print("changed_hours:", changed_hours)
print("исходный hours:", hours)

changed_matrix = matrix.copy()
changed_matrix[1, :] = 0
changed_matrix[:, -1] = -1
changed_matrix[1:4, 1:4] = 100

print("changed_matrix:")
print(changed_matrix)
print("исходная matrix:")
print(matrix)


# Задание 6. Изменение формы
numbers = np.arange(12)
table = numbers.reshape(3, 4)
transposed = table.T

print("\nЗадание 6")
print("Форма numbers:", numbers.shape)
print("Форма table:", table.shape)
print("Форма transposed:", transposed.shape)
print("table:")
print(table)
print("transposed:")
print(transposed)

# reshape(3, 4) работает, потому что 3 * 4 = 12 элементов.
# reshape(5, 3) вызовет ошибку, потому что 5 * 3 = 15, а в массиве 12 элементов.
