class Matrix:
    def __init__(self, matrix):
        self.__matrix = self.__validate_matrix(matrix)
    
    def swapRows(self, r1, r2):
        self.__matrix[r1 - 1], self.__matrix[r2 - 1] = self.__matrix[r2 - 1], self.__matrix[r1 - 1]
    
    def swapCollums(self, c1, c2):
        for i in self.__matrix:
            i[c1 - 1], i[c2 - 1] = i[c2 - 1], i[c1 - 1]
    
    def display(self):
        for m in self.__matrix:
            print(m)
    
    def sumRow(self, r):
        summa = 0
        for i in self.__matrix[r - 1]:
            summa += i
        return summa
    
    def sumColl(self, c):
        summa = 0
        for i in self.__matrix:
            summa += i[c - 1]
        return summa
    
    def sumDiagonal(self):
        summa = 0
        for i in range(len(self.__matrix)):
            summa += self.__matrix[i][i]
        return summa
    # multiplication method
    def __mul__(self, other):
        if type(other) == int:
            return Matrix(self.__multiply_by_scalar(self.__matrix, other))
        elif type(other) == Matrix:
            return Matrix(self.__multiply_by_matrix(self.__matrix, other.__matrix))
        else:
            raise TypeError('Matrix can be multiplyed only by matirx or scalar number')

    @staticmethod
    def __multiply_by_matrix(a, b):
        if len(a[0]) != len(b):
            raise ValueError('Columns of matrix A have to be equal to Rows of matrix B')
        
        resmat = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]
        for i in range(len(resmat)):
            for j in range(len(resmat[i])):
                for it in [a[i][k] * b[k][j] for k in range(len(a[0]))]:
                    resmat[i][j] += it
        return resmat

    @staticmethod
    def __multiply_by_scalar(a, b):
        for i in range(len(a)):
            for j in range(len(a[i])):
                a[i][j] *= b
        return a
    # ----------------------------------------------------------------------
    # determinant method
    def det(self):
        return self.r_det(self.__is_quadratic(self.__matrix))

    @classmethod
    def __is_quadratic(cls, matrix):
        for row in matrix:
            if len(matrix) != len(row):
                raise Exception('To find determinant matrix should be quadratic')
        return matrix
    
    @classmethod
    def __validate_matrix(cls, matrix):
        for i in matrix:
            for j in i:
                if type(j) != int:
                    raise TypeError('Components of matrix have to be integer')
        return matrix
    
    def r_det(self, mx):
            if len(mx) == 2:
                return (mx[0][0] * mx[1][1]) - (mx[0][1] * mx[1][0])
            else:
                return sum([(mx[0][i] * ((-1) ** (1 + (i + 1)))) * self.r_det(self.m(mx, 0, i)) for i in range(len(mx))])
    
    def m(self, mx, i, j):
                m = [[coll for coll in row] for row in mx]
                if len(m) == 2:
                    return m
                else:
                    del m[i]
                    for k in m:
                        del k[j]
                    return m
    # ---------------------------------------------------------------------------

m1 = Matrix([[4, 2, 3, 7], [4, 3, 6, 9], [7, 8, 9, 9], [1, 2, 3, 4]])
# m1 = Matrix([[1, 2, 5], [4, 5, 5], [2, 1, 1]])
m1.display()
print(m1.det())
