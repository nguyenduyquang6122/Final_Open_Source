import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import messagebox as mb
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
def get_matrix_size():
    if not size_entry.get():
        mb.showwarning("Cảnh báo!", "Vui lòng nhập giá trị cho kích thước ma trận")
        return None

    try:
        size_matrix = int(size_entry.get())
        if(size_matrix <= 0):
            mb.showerror("Lỗi!","Kích thước của ma trận phải là số nguyên dương")
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

def erase_matrix(frame_matrix, label, matrix_type, result_label):
    for widget in frame_matrix.winfo_children():
        widget.destroy()
    label.grid_forget()
    if frame_matrix is not frame_matrix_C:
        label_result_X.config(text="")
    result_label.config(text="")
    global entry_A, entry_B, entry_C, matrix_A, matrix_B, vector_C
    if matrix_type == 'A':
        entry_A = None
        matrix_A = None
    elif matrix_type == 'B':
        entry_B = None
        matrix_B = None
    elif matrix_type == 'C':
        entry_C = None
        vector_C = None

def get_value_matrix(frame_matrix):
    size_matrix = get_matrix_size()
    if size_matrix is not None:
        try:
            global entry_A, entry_B, entry_C, matrix_A, matrix_B, vector_C
            if frame_matrix.winfo_exists() and frame_matrix is frame_matrix_A:
                if 'entry_A' not in globals():
                    mb.showerror("Lỗi", "Vui lòng tạo ma trận 1 trước")
                    return False
                if entry_A is None:
                    mb.showerror("Lỗi", "Vui lòng tạo ma trận 1 trước")
                    return False
                matrix_A = [[int(entry_A[row][col].get()) for col in range(size_matrix)] for row in range(size_matrix)]
            elif frame_matrix.winfo_exists() and frame_matrix is frame_matrix_B:
                if 'entry_B' not in globals():
                    mb.showerror("Lỗi", "Vui lòng tạo ma trận 2 trước")
                    return False
                if entry_B is None:
                    mb.showerror("Lỗi", "Vui lòng tạo ma trận 2 trước")
                    return False
                matrix_B = [[int(entry_B[row][col].get()) for col in range(size_matrix)] for row in range(size_matrix)]
            elif frame_matrix.winfo_exists() and frame_matrix is frame_matrix_C:
                if 'entry_C' not in globals():
                    mb.showerror("Lỗi", "Vui lòng tạo vector kết quả trước")
                    return False
                if entry_C is None:
                    mb.showerror("Lỗi", "Vui lòng tạo vector kết quả trước")
                    return False
                vector_C = [int(entry_C[row].get()) for row in range(size_matrix)]
            else:
                return False
        except ValueError:
            mb.showerror("Lỗi", "Vui lòng nhập giá trị số hợp lệ cho tất cả các mục")
            return False
        return True
def draw_graph1(matrix_A_np, vector_C, w,frame_graph):
    fig, ax = plt.subplots()
    ax.plot(matrix_A_np, w[0] * matrix_A_np + w[1], 'r-', label='Fitted line')
    ax.plot(matrix_A_np, vector_C, 'y', label='Original data')
    ax.legend()
    ax.set_title('He PT 1')
    # Thay đổi kích thước của hình vẽ
    fig.set_size_inches(3, 2)

    canvas = FigureCanvasTkAgg(fig, master=frame_graph)
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

def draw_graph2(matrix_B_np, vector_C, w,frame_graph):
    fig, ax = plt.subplots()
    ax.plot(matrix_B_np, w[0] * matrix_B_np + w[1], 'r-', label='Fitted line')
    ax.plot(matrix_B_np, vector_C, 'o', label='Original data')
    ax.legend()
    ax.set_title('He PT 2')
    # Thay đổi kích thước của hình vẽ
    fig.set_size_inches(3, 2)

    canvas = FigureCanvasTkAgg(fig, master=frame_graph)
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
def matrix_calculation(n):
    if n == 1:
        mb.showinfo("Thông báo!", "Bạn chọn tính các giá trị cơ bản của ma trận 1 gồm: hạng, tổng đường chéo, định thức, nghịch đảo, lũy thừa, giá trị riêng và vectơ riêng của ma trận")
        if get_value_matrix(frame_matrix_A):
            try:
                x = np.linalg.inv(matrix_A)
                text_inv = f"- Ma trận nghịch đảo 1:\n {x}\n"
            except np.linalg.LinAlgError:
                text_inv = "- Ma trận nghịch đảo 1 không tồn tại"
            label_resutl_A.config(text=f"- Bậc ma trận 1: {np.linalg.matrix_rank(matrix_A)}\n"
                                + f"- Tổng đường chéo ma trận 1: {np.trace(matrix_A)}\n"
                                + f"- Định thức ma trận 1: {np.round(np.linalg.det(matrix_A), 2)}\n"
                                + text_inv
                                + f"- Giá trị ma trận  1:\n {np.linalg.eig(matrix_A)[0]}\n"
                                + f"- Vector ma trận 1:\n {np.linalg.eig(matrix_A)[1]}\n")
    elif n == 2:
        mb.showinfo("Thông báo!", "Bạn chọn tính các giá trị cơ bản của ma trận 2 gồm: hạng, tổng đường chéo, định thức, nghịch đảo, lũy thừa, giá trị riêng và vectơ riêng của ma trận")
        if get_value_matrix(frame_matrix_B):
            try:
                x = np.linalg.inv(matrix_B)
                text_inv = f"- Ma trận nghịch đảo 2:\n {x}\n"
            except np.linalg.LinAlgError:
                text_inv = "- Ma trận nghịch đảo 2 không tồn tại"
            label_resutl_B.config(text=f"- Bậc ma trận 2: {np.linalg.matrix_rank(matrix_B)}\n"
                                + f"- Tổng đường chéo 2: {np.trace(matrix_B)}\n"
                                + f"- Định thức ma trận 2: {np.round(np.linalg.det(matrix_B), 2)}\n"
                                + text_inv
                                + f"- Giá trị ma trận 2:\n {np.linalg.eig(matrix_B)[0]}\n"
                                + f"- Vector ma trận 2:\n {np.linalg.eig(matrix_B)[1]}\n")
    if n == 3:
        mb.showinfo("Thông báo!", "Bạn đã chọn tính tích hai ma trận")
        if get_value_matrix(frame_matrix_A) and get_value_matrix(frame_matrix_B):
            try:
                result_1 = np.dot(matrix_A, matrix_B)
                result_2 = np.vdot(matrix_A, matrix_B)
                label_result_X.config(text=f"-Tích hai ma trận:\n {result_1}\n"
                                      + f"-Tích vô hướng hai ma trận:\n {result_2}")
            except ValueError:
                mb.showerror("Lỗi",
                             "Hai ma trận không thể nhân với nhau vì số cột của ma trận thứ nhất không bằng số hàng của ma trận thứ hai")
    # if n == 4:
    #     mb.showinfo("Thông báo!", "Bạn đã chọn tính tích vô hướng hai vector")
    #     if get_value_matrix(frame_matrix_A) and get_value_matrix(frame_matrix_B):
    #         try:
    #             vector_A = np.squeeze(matrix_A)
    #             vector_B = np.squeeze(matrix_B)
    #             result = np.dot(vector_A, vector_B)
    #             label_result_E.config(text="Kết quả tích vô hướng 2 vector:\n" + str(result))
    #         except ValueError:
    #             mb.showerror("Lỗi", "Hai vector không cùng kích thước")
    if n == 4:
        mb.showinfo("Thông báo!, Bạn sẽ tính nghiệm của phương trình và nghiệm bình phương nhỏ nhất của phương trình 1")
        if get_value_matrix(frame_matrix_A) and get_value_matrix(frame_matrix_C):
            if len(matrix_A) == 1 and len(matrix_A[0]) == 1:
                mb.showerror("Lỗi", "Kích thước của ma trận A phải lớn hơn 1x1.")
            else:
                matrix_A_np = np.array(matrix_A)
                if np.linalg.det(matrix_A_np) != 0:
                    w = np.linalg.lstsq(matrix_A_np.T, vector_C, rcond=None)[0]
                    draw_graph1(matrix_A_np, vector_C, w, frame_graph1)
                    label_result_D.config(
                        text=f"- Nghiệm của hệ phương trình 1 là:\n {np.linalg.solve(matrix_A, vector_C)}\n"
                        + f"- Nghiệm bình phương nhỏ nhất \n của hệ phương trình 1 là:\n {w} \n")
                else:
                    mb.showerror("Lỗi", "Ma trận A không thể giải được.")
        else:
                mb.showerror("Lỗi", "Nhập giá trị cho ma trận A và vector C trước khi tính toán.")
    if n == 5:
        mb.showinfo("Thông báo!, Bạn sẽ tính nghiệm của phương trình và nghiệm bình phương nhỏ nhất của phương trình 2")
        if get_value_matrix(frame_matrix_B) and get_value_matrix(frame_matrix_C):
            if len(matrix_B) == 1 and len(matrix_B[0]) == 1:
                mb.showerror("Lỗi", "Kích thước của ma trận B phải lớn hơn 1x1.")
            else:
                matrix_B_np = np.array(matrix_B)
                if np.linalg.det(matrix_B_np) != 0:
                    w = np.linalg.lstsq(matrix_B_np.T, vector_C, rcond=None)[0]
                    draw_graph2(matrix_B_np, vector_C, w,frame_graph2)
                    label_result_E.config(
                        text=f"- Nghiệm của hệ phương trình 2 là:\n {np.linalg.solve(matrix_B, vector_C)}\n"
                             + f"- Nghiệm bình phương nhỏ nhất \n  của hệ phương trình 2 là:\n {w} \n")
                else:
                    mb.showerror("Lỗi", "Ma trận B không thể giải được.")
        else:
            mb.showerror("Lỗi", "Nhập giá trị cho ma trận B và vector C trước khi tính toán.")
w = Tk()
w.title("Ứng dụng hỗ trợ môn học ĐSTT")

frame_choose = Frame(w)
frame_choose.grid(row=0, columnspan=3)
frame_graph1 = Frame(w)
frame_graph1.grid(row=4, columnspan=4, rowspan=2)  
frame_graph2 = Frame(w)
frame_graph2.grid(row=6, columnspan=4, rowspan=2)

size_label = Label(frame_choose, text="Kích thước ma trận:")
size_label.grid(row=0, column=0)
size_entry = Entry(frame_choose)
size_entry.grid(row=0, column=1)

frame_A = Frame(w)
frame_A.grid(row=1, column=0, padx=5, pady=5)

creat_A = Button(frame_A, text="Tạo ma trận 1", command=lambda: creat_matrix(frame_matrix_A, label_A))
creat_A.grid(row=0, column=0)

erase_A = Button(frame_A, text="Xoá ma trận 1", command=lambda: erase_matrix(frame_matrix_A, label_A, 'A', label_resutl_A))
erase_A.grid(row=0, column=1)

label_A = Label(frame_A, text="Nhập ma trận 1:")


frame_matrix_A = Frame(frame_A)
frame_matrix_A.grid(row=2, columnspan=2)

frame_B = Frame(w)
frame_B.grid(row=1, column=1, padx=5, pady=5)

creat_B = Button(frame_B, text="Tạo ma trận 2", command=lambda: creat_matrix(frame_matrix_B, label_B))
creat_B.grid(row=0, column=0)

erase_B = Button(frame_B, text="Xoá ma trận 2", command=lambda: erase_matrix(frame_matrix_B, label_B, 'B', label_resutl_B))
erase_B.grid(row=0, column=1)

label_B = Label(frame_B, text="Nhập ma trận 2:")

frame_matrix_B = Frame(frame_B)
frame_matrix_B.grid(row=2, columnspan=2)

frame_C = Frame(w)
frame_C.grid(row=1, column=2, padx=5, pady=5)

creat_C = Button(frame_C, text="Tạo vector kết quả", command=lambda: creat_matrix(frame_matrix_C, label_C))
creat_C.grid(row=0, column=0)

erase_C = Button(frame_C, text="Xoá vector kết quả", command=lambda: erase_matrix(frame_matrix_C, label_C, 'C'))
erase_C.grid(row=0, column=1)

label_C = Label(frame_C, text="Nhập vector kết quả:")

frame_matrix_C = Frame(frame_C)
frame_matrix_C.grid(row=2, columnspan=2)

frame_choose_cal = Frame(w)
frame_choose_cal.grid(row=2, columnspan=2)

button_cal_basic = Button(frame_choose_cal, text="Tính ma trận 1", command=lambda: matrix_calculation(1))
button_cal_basic.grid(row=0, column=0, padx=5, pady=5)

button_cal_basic = Button(frame_choose_cal, text="Tính ma trận 2", command=lambda: matrix_calculation(2))
button_cal_basic.grid(row=0, column=1, padx=5, pady=5)

button_cal_multiply = Button(frame_choose_cal, text="Tính tích hai ma trận", command=lambda: matrix_calculation(3))
button_cal_multiply.grid(row=0, column=2, padx=5, pady=5)

button_cal_equations1 = Button(frame_choose_cal, text="giải hệ phương trình 1", command=lambda: matrix_calculation(4))
button_cal_equations1.grid(row=0, column=3, padx=5, pady=5)

button_cal_equations2 = Button(frame_choose_cal, text="giải hệ phương trình 2", command=lambda: matrix_calculation(5))
button_cal_equations2.grid(row=0, column=4, padx=5, pady=5)

label_resutl_A = Label(w, text="", justify='left', font=('Helvetica',10, 'bold'))
label_resutl_A.grid(row=3, column=0)
label_resutl_B = Label(w, text="", justify='left', font=('Helvetica',10, 'bold'))
label_resutl_B.grid(row=3, column=1)
label_result_X = Label(w, text="", justify='left', font=('Helvetica', 10, 'bold'))
label_result_X.grid(row=3, column=2)
label_result_D = Label(w, text="", justify='left', font=('Helvetica', 10, 'bold'))
label_result_D.grid(row=4, column=0)
label_result_E = Label(w, text="", justify='left', font=('Helvetica', 10, 'bold'))
label_result_E.grid(row=6, column=0)


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

#Tính tích 2 ma trận
# # print("Tích hai ma trận: \n",np.dot(a,b))
# # print("Tích vô hướng hai ma trận: \n",np.vdot(a,b))

#Tính nghiệm của hệ phương trình 
# print("Nghiệm hệ phương trình: \n",np.linalg.solve(a,c))
# w = np.linalg.lstsq(a.T,c)[0]
# print("Nghiệm bình phương nhỏ nhất cho phương trình ma trận tuyến tính: \n",w)
# line = w[0]*a+w[1]
# plt.plot(a, line, 'r-', label='Fitted line')
# plt.plot(a, c, 'o', label='Original data')
# plt.legend()
# plt.show()
