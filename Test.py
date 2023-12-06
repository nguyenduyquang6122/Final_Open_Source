import numpy as np
def matrix_product(A, B):
    return np.dot(A, B)
def vector_dot_product(A, B):
    return np.vdot(A, B)
def matrix_determinant(A):
    return np.linalg.det(A)
def matrix_inverse(A):
    return np.linalg.inv(A)
def solve_linear_system(A, b):
    try:
        x = np.linalg.solve(A, b)
        return x
    except np.linalg.LinAlgError:
        print("Hệ phương trình không có nghiệm hoặc có vô số nghiệm.")


a = np.array([[2,3],[4,5]])
b = np.array([[11,12],[13,14]])
c = np.array([1,2])

print("Tích hai ma trận:", matrix_product(a, b))
print("Tích vô hướng hai vector:", vector_dot_product(a, b))
print("Định thức:", matrix_determinant(a))
print("Ma trận nghịch đảo:", matrix_inverse(a))
print("Giải hệ phương trình:", solve_linear_system(a, c))
