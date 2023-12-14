import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import messagebox as mb

def get_matrix_size():
    if not size_entry.get():
        mb.showwarning("Warning!", "Please enter a value for the matrix size")
        return None

    try:
        size_matrix = int(size_entry.get())
        if(size_matrix <= 0):
            mb.showerror("Error!","The size of the matrix must be positive integers")
            raise ValueError
        
        
        return size_matrix
    except ValueError:
        return None
    
def creat_matrix(frame_matrix, label):
    size_matrix = get_matrix_size()

    if size_matrix is not None:
        if frame_matrix is frame_matrix_C:
            label.grid(row=1, columnspan=2)
            for widget in frame_matrix.winfo_children():
                widget.destroy()

            global entry_C
            entry_C = [Entry(frame_matrix) for i in range(size_matrix)]

            for row in range(size_matrix):
                entry_C[row].grid(row=row, column=0,padx=5, pady=5)
        if frame_matrix is frame_matrix_A:
            label.grid(row=1, columnspan=2)
            for widget in frame_matrix.winfo_children():
                widget.destroy()
            
            global entry_A
            entry_A = [[Entry(frame_matrix) for i in range(size_matrix)] for i in range(size_matrix)]

            for row in range(size_matrix):
                for col in range(size_matrix):
                    entry_A[row][col].grid(row=row, column=col, padx=5, pady=5)
        if frame_matrix is frame_matrix_B:
            label.grid(row=1, columnspan=2)
            for widget in frame_matrix.winfo_children():
                widget.destroy()
            
            global entry_B
            entry_B = [[Entry(frame_matrix) for i in range(size_matrix)] for i in range(size_matrix)]

            for row in range(size_matrix):
                for col in range(size_matrix):
                    entry_B[row][col].grid(row=row, column=col, padx=5, pady=5)

def erase_matrix(frame_matrix, label):
    for widget in frame_matrix.winfo_children():
        widget.destroy()
    label.grid_forget()

def get_value_matrix(frame_matrix):
    size_matrix = get_matrix_size()
    if size_matrix is not None:
        try:
            global matrix_A, matrix_B, vector_C
            if frame_matrix.winfo_exists() and frame_matrix is frame_matrix_A:
                matrix_A = [[int(entry_A[row][col].get()) for col in range(size_matrix)] for row in range(size_matrix)]
            elif frame_matrix.winfo_exists() and frame_matrix is frame_matrix_B:
                matrix_B = [[int(entry_B[row][col].get()) for col in range(size_matrix)] for row in range(size_matrix)]
            elif frame_matrix.winfo_exists() and frame_matrix is frame_matrix_C:
                vector_C = [int(entry_C[row].get()) for row in range(size_matrix)]
            else:
                return False
        except ValueError:
            mb.showerror("Error", "Please enter valid numerical values for all entries")
            return False
        return True

def matrix_calculation(n):
    if n == 1:
        mb.showinfo("Announcement!", "You choose to calculate the basic values of matrix 1 including: rank, trace, determinant, inverse, power, eigen value and eigen vector of matrix")
        if get_value_matrix(frame_matrix_A):
            try:
                x = np.linalg.inv(matrix_A)
                text_inv = f"- Inverse of matrix 1:\n {x}\n"
            except np.linalg.LinAlgError:
                text_inv = "- Inverse of matrix 1 is not exist"
            label_resutl.config(text=f"- Rank of matrix 1: {np.linalg.matrix_rank(matrix_A)}\n"
                                + f"- Trace of matrix 1: {np.trace(matrix_A)}\n"
                                + f"- Determinant of a matrix 1: {np.linalg.det(matrix_A)}\n"
                                + text_inv
                                + f"- An eigen value of a matrix 1:\n {np.linalg.eig(matrix_A)[0]}\n"
                                + f"- An eigen vector of a matrix 1:\n {np.linalg.eig(matrix_A)[1]}\n")
    if n == 2:
        mb.showinfo("Announcement!", "You choose to calculate the basic values of matrix 2 including: rank, trace, determinant, inverse, power, eigen value and eigen vector of matrix")
        if get_value_matrix(frame_matrix_B):
            try:
                x = np.linalg.inv(matrix_B)
                text_inv = f"- Inverse of matrix 2:\n {x}\n"
            except np.linalg.LinAlgError:
                text_inv = "- Inverse of matrix 2 is not exist"
            label_resutl.config(text=f"- Rank of matrix 2: {np.linalg.matrix_rank(matrix_B)}\n"
                                + f"- Trace of matrix 2: {np.trace(matrix_B)}\n"
                                + f"- Determinant of a matrix 2: {np.linalg.det(matrix_B)}\n"
                                + text_inv
                                + f"- An eigen value of a matrix 2:\n {np.linalg.eig(matrix_B)[0]}\n"
                                + f"- An eigen vector of a matrix 2:\n {np.linalg.eig(matrix_B)[1]}\n")
            
        

w = Tk()
w.title("Application to support Linear Algebra")

frame_choose = Frame(w)
frame_choose.grid(row=0, columnspan=3)

size_label = Label(frame_choose, text="Entry size of matrix:")
size_label.grid(row=0, column=0)
size_entry = Entry(frame_choose)
size_entry.grid(row=0, column=1)

frame_A = Frame(w)
frame_A.grid(row=1, column=0, padx=5, pady=5)

creat_A = Button(frame_A, text="Creat matrix 1", command=lambda: creat_matrix(frame_matrix_A, label_A))
creat_A.grid(row=0, column=0)

erase_A = Button(frame_A, text="Erase matrix 1", command=lambda: erase_matrix(frame_matrix_A, label_A))
erase_A.grid(row=0, column=1)

label_A = Label(frame_A, text="Entry matrix 1:")


frame_matrix_A = Frame(frame_A)
frame_matrix_A.grid(row=2, columnspan=2)

frame_B = Frame(w)
frame_B.grid(row=1, column=1, padx=5, pady=5)

creat_B = Button(frame_B, text="Creat matrix 2", command=lambda: creat_matrix(frame_matrix_B, label_B))
creat_B.grid(row=0, column=0)

erase_B = Button(frame_B, text="Erase matrix 2", command=lambda: erase_matrix(frame_matrix_B, label_B))
erase_B.grid(row=0, column=1)

label_B = Label(frame_B, text="Entry matrix 2:")

frame_matrix_B = Frame(frame_B)
frame_matrix_B.grid(row=2, columnspan=2)

frame_C = Frame(w)
frame_C.grid(row=1, column=2, padx=5, pady=5)

creat_C = Button(frame_C, text="Creat vector result", command=lambda: creat_matrix(frame_matrix_C, label_C))
creat_C.grid(row=0, column=0)

erase_C = Button(frame_C, text="Erase vector result", command=lambda: erase_matrix(frame_matrix_C, label_C))
erase_C.grid(row=0, column=1)

label_C = Label(frame_C, text="Entry vector result:")

frame_matrix_C = Frame(frame_C)
frame_matrix_C.grid(row=2, columnspan=2)

frame_choose_cal = Frame(w)
frame_choose_cal.grid(row=2, columnspan=2)

button_cal_basic = Button(frame_choose_cal, text="Cal matrix 1", command=lambda: matrix_calculation(1))
button_cal_basic.grid(row=0, column=0, padx=5, pady=5)

button_cal_basic = Button(frame_choose_cal, text="Cal matrix 2", command=lambda: matrix_calculation(2))
button_cal_basic.grid(row=0, column=1, padx=5, pady=5)

label_resutl = Label(w, text="", justify='left', font=('Helvetica',10, 'bold'))
label_resutl.grid(row=3, column=0)

w.mainloop()

#Tính toán cơ bản
# a = np.array([[2,3],[4,5]])
# b = np.array([[11,12],[13,14]])
# c = np.array([1,2])
# print("Ma trận A: \n", a)
# print("Ma trận B: \n", b)
# print("Ma trận kết quả: \n", c)
# # print("Thứ hạng của ma trận: \n", np.linalg.matrix_rank(b))
# # print("Tổng đường chéo của ma trận: \n",np.trace(a))
# # print("Định thức: \n",np.linalg.det(a))
# # print("Ma trận nghịch đảo: \n",np.linalg.inv(a))
# # print("Nâng ma trận lên lũy thừa n(số nguyên): \n", np.linalg.matrix_power(a,2))
# d, e = np.linalg.eig(a)
# print("Giá trị riêng: \n", d)
# print("Vectors riêng: \n", e)

#Tính tích 2 vector
# # print("Tích hai ma trận: \n",np.dot(a,b))
# # print("Tích vô hướng hai vector: \n",np.vdot(a,b))

#Tính nghiệm của hệ phương trình 
# print("Nghiệm hệ phương trình: \n",np.linalg.solve(a,c))
# w = np.linalg.lstsq(a.T,c)[0]
# print("Nghiệm bình phương nhỏ nhất cho phương trình ma trận tuyến tính: \n",w)
# line = w[0]*a+w[1]
# plt.plot(a, line, 'r-', label='Fitted line')
# plt.plot(a, c, 'o', label='Original data')
# plt.legend()
# plt.show()