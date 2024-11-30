import numpy as np


class Matrix:
    def __init__(self, matrix):
        self.validate_matrix(matrix)
        self.matrix = matrix

    @staticmethod
    def validate_matrix(matrix):
        if not matrix:
            raise ValueError('Matrix is empty')
        if not isinstance(matrix, list) or not isinstance(matrix[0], list):
            raise ValueError('Matrix is not a list of lists')

    def __add__(self, other):
        matrix = other.matrix
        self.validate_matrix(matrix)
        if len(self.matrix) != len(matrix) or len(self.matrix[0]) != len(matrix[0]):
            raise ValueError('Matrices have different number of dimensions')

        return Matrix([[a + b for a, b in zip(row, matrix[i])] for i, row in enumerate(self.matrix)])

    def __mul__(self, other):
        matrix = other.matrix
        if len(self.matrix) != len(matrix) or len(self.matrix[0]) != len(matrix[0]):
            raise ValueError("Matrices must have the same dimensions for element-wise multiplication")

        result = []
        for i in range(len(self.matrix)):
            row = [self.matrix[i][j] * matrix[i][j] for j in range(len(self.matrix[0]))]
            result.append(row)

        return Matrix(result)

    def __matmul__(self, other):
        matrix = other.matrix
        self.validate_matrix(matrix)
        if len(self.matrix[0]) != len(matrix):
            raise ValueError('Matrices have different number of dimensions')

        return Matrix([[sum(a * b for a, b in zip(row, col)) for col in zip(*matrix)] for row in self.matrix])

    def __getitem__(self, index):
        return self.matrix[index]

    def __str__(self):
        str_ = ""
        for row in self.matrix:
            str_ += " ".join(str(x) for x in row) + "\n"
        return str_


np_a = np.random.randint(0, 10, (10, 10))
np_b = np.random.randint(0, 10, (10, 10))
a = Matrix(np_a.tolist())
b = Matrix(np_b.tolist())

with open("artifacts/3.1/matrix+.txt", "w") as f:
    print("matrix a:\n" + str(a), file=f)
    print("matrix b:\n" + str(b), file=f)
    print("matrix a + b:\n" + str(a + b), file=f)

with open("artifacts/3.1/matrix*.txt", "w") as f:
    print("matrix a:\n" + str(a), file=f)
    print("matrix b:\n" + str(b), file=f)
    print("matrix a * b:\n" + str(a * b), file=f)

with open("artifacts/3.1/matrix@.txt", "w") as f:
    print("matrix a:\n" + str(a), file=f)
    print("matrix b:\n" + str(b), file=f)
    print("matrix a @ b:\n" + str(a @ b), file=f)