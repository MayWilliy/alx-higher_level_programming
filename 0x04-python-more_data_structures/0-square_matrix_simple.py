#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
	n_matrix = matrix.copy()
	for j in range(len(matrix)):
		n_matrix[j] = list(map(lambda x: x**2, matrix[j]))
	return (n_matrix)
