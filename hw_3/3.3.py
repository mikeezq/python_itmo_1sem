import numpy as np

cache_dict = {}

class MatrixHashMixin:
    def hash(self):
        # sum of elements by module 256
        return sum(sum(row) for row in self.matrix) % 256

class Matrix(MatrixHashMixin):
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
            raise ValueError('Matrices have different dimensions')

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
        global cache_dict
        hash_self = self.hash()
        hash_other = other.hash()
        key = (hash_self, hash_other)
        if key in cache_dict:
            return cache_dict[key]
        else:
            matrix = other.matrix
            self.validate_matrix(matrix)
            if len(self.matrix[0]) != len(matrix):
                raise ValueError('Matrices dimensions do not allow multiplication')

            result = Matrix([[sum(a * b for a, b in zip(row, col)) for col in zip(*matrix)] for row in self.matrix])
            cache_dict[key] = result
            return result

    def actual_matmul(self, other):
        matrix = other.matrix
        self.validate_matrix(matrix)
        if len(self.matrix[0]) != len(matrix):
            raise ValueError('Matrices dimensions do not allow multiplication')

        result = Matrix([[sum(a * b for a, b in zip(row, col)) for col in zip(*matrix)] for row in self.matrix])
        return result

    def __getitem__(self, index):
        return self.matrix[index]

    def __str__(self):
        str_ = ""
        for row in self.matrix:
            str_ += " ".join(str(x) for x in row) + "\n"
        return str_

A_values = [[1, 2], [3, 4]]
C_values = [[4, 3], [2, 1]]
A = Matrix(A_values)
C = Matrix(C_values)

assert A.hash() == C.hash(), "Hashes are not equal"
assert A.matrix != C.matrix, "Matrices are equal"

B_values = np.random.randint(0, 10, (2, 2)).tolist()
B = Matrix(B_values)
D = Matrix(B_values)

AB = A @ B

CD = C @ D

actual_CD = C.actual_matmul(D)

if CD.matrix != actual_CD.matrix:
    print("Due to hash collision, cache returned incorrect result for C @ D")

with open("artifacts/3.3/A.txt", "w") as f:
    f.write(str(A))
with open("artifacts/3.3/B.txt", "w") as f:
    f.write(str(B))
with open("artifacts/3.3/C.txt", "w") as f:
    f.write(str(C))
with open("artifacts/3.3/D.txt", "w") as f:
    f.write(str(D))
with open("artifacts/3.3/AB.txt", "w") as f:
    f.write(str(AB))
with open("artifacts/3.3/CD.txt", "w") as f:
    f.write(str(CD))
with open("artifacts/3.3/hash.txt", "w") as f:
    f.write(f"hash(A) = {A.hash()}\n")
    f.write(f"hash(C) = {C.hash()}\n")
    f.write(f"hash(B) = {B.hash()}\n")
    f.write(f"hash(D) = {D.hash()}\n")

with open("actual_CD.txt", "w") as f:
    f.write(str(actual_CD))
