import numpy as np


def make_table(rows, columns):
    return np.arange(rows * columns).reshape(rows, columns).tolist()


def rectangle(matrix, row_start, row_stop, column_start, column_stop):
    arr = np.asarray(matrix)
    return arr[row_start:row_stop, column_start:column_stop].tolist()


def replace_rectangle(matrix, row_start, row_stop, column_start, column_stop, value):
    arr = np.asarray(matrix, dtype=float).copy()
    arr[row_start:row_stop, column_start:column_stop] = value
    return arr.tolist()


def matrix_vector_product(matrix, vector):
    return (np.asarray(matrix) @ np.asarray(vector)).tolist()
