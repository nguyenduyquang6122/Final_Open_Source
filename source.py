import numpy as np

a = np.array([[2,3],[4,5]])
b = np.array([[11,12],[13,14]])
c = np.array([1,2])
print("Tích hai ma trận: ",np.dot(a,b))
print("Tích vô hướng hai vector: ",np.vdot(a,b))
print("Định thức: ",np.linalg.det(a))
print("Ma trận nghịch đảo: ",np.linalg.inv(a))
print("Giải hệ phương trình: ",np.linalg.solve(a,c))