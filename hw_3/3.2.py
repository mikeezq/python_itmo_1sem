import numpy as np

class ArithmeticMixin:
    def __add__(self, other):
        return Matrix(self.matrix + other.data)

    def __sub__(self, other):
        return Matrix(self.matrix - other.data)

    def __mul__(self, other):
        return Matrix(self.matrix * other.data)

    def __truediv__(self, other):
        return Matrix(self.matrix / other.data)

    def __matmul__(self, other):
        return Matrix(self.matrix @ other.data)


class FileMixin:
    def write_to_file(self, header, file):
        file.write(header)
        print(str(self), file=file)


class StringMixin:
    def __str__(self):
        str_ = ""
        matrix = self.matrix
        for row in matrix:
            str_ += " ".join(str(x) for x in row) + "\n"
        return str_


class GetterSetterMixin:
    @property
    def matrix(self):
        return self._matrix

    @matrix.setter
    def data(self, value):
        self.validate_matrix(value)
        self._matrix = value

    @staticmethod
    def validate_matrix(data):
        if not isinstance(data, np.ndarray):
            raise ValueError("Matrix data must be a numpy array")
        if data.ndim != 2:
            raise ValueError("Matrix data must be 2-dimensional")


class Matrix(ArithmeticMixin, FileMixin, StringMixin, GetterSetterMixin):
    def __init__(self, matrix):
        self._matrix = np.array(matrix)


np_a = np.random.randint(0, 10, (10, 10))
np_b = np.random.randint(0, 10, (10, 10))

a = Matrix(np_a)
b = Matrix(np_b)

with open("artifacts/3.2/matrix+.txt", "w") as f:
    a.write_to_file("matrix a:\n", f)
    b.write_to_file("matrix b:\n", f)
    (a + b).write_to_file("matrix a + b:\n", f)

with open("artifacts/3.2/matrix*.txt", "w") as f:
    a.write_to_file("matrix a:\n", f)
    b.write_to_file("matrix b:\n", f)
    (a * b).write_to_file("matrix a * b:\n", f)

with open("artifacts/3.2/matrix@.txt", "w") as f:
    a.write_to_file("matrix a:\n", f)
    b.write_to_file("matrix b:\n", f)
    (a @ b).write_to_file("matrix a @ b:\n", f)
