# # Python Program illustrating
# # numpy.linalg.lstsq() method


# import numpy as np
# import matplotlib.pyplot as plt

# # x co-ordinates
# x = np.arange(0, 9)
# A = np.array([x, np.ones(9)])
# print(A)

# # # linearly generated sequence
# # y = [19, 20, 20.5, 21.5, 22, 23, 23, 25.5, 24]
# # # obtaining the parameters of regression line
# # w = np.linalg.lstsq(A.T, y)[0] 

# # # plotting the line
# # line = w[0]*x + w[1] # regression line
# # plt.plot(x, line, 'r-')
# # plt.plot(x, y, 'o')
# # plt.show()
import numpy as np

# Tạo ma trận hệ số A và vector giá trị b
A = np.array([[1, 2], [3, 4]])
b = np.array([5, 7])

# Giải hệ phương trình Ax = b bằng hàm lstsq
x, residuals, rank, s = np.linalg.lstsq(A, b, rcond=None)

print("Giải của hệ phương trình:", x)
print("Sai số tổng bình phương:", residuals)
print("Hạng của ma trận A:", rank)
print("Giá trị giả nghịch đảo của ma trận A:", s)
