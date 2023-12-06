import numpy as np
import tkinter as tk
from tkinter import ttk

def get_matrix_size():
    try:
        rows = int(rows_entry.get())
        cols = int(cols_entry.get())

        if rows <= 0 or cols <= 0:
            raise ValueError("Số hàng và số cột phải là số nguyên dương.")
        
        return rows, cols
    except ValueError:
        return None, None

def create_matrix_inputs():
    rows, cols = get_matrix_size()

    if rows is None or cols is None:
        return
    
    # Xóa widget cũ nếu có
    for widget in matrix_input_frame.winfo_children():
        widget.destroy()

    # Tạo lại widget cho ma trận A và vectơ c
    global entry_a, entry_c
    entry_a = [[tk.Entry(matrix_input_frame) for _ in range(cols)] for _ in range(rows)]
    entry_c = [tk.Entry(matrix_input_frame) for _ in range(rows)]

    # Sắp xếp lại widget trên giao diện
    for row in range(rows):
        for col in range(cols):
            entry_a[row][col].grid(row=row, column=col, padx=5, pady=5)
        entry_c[row].grid(row=row, column=cols, padx=5, pady=5)

def calculate():
    rows, cols = get_matrix_size()

    if rows is None or cols is None:
        return

    # Lấy giá trị từ các ô nhập liệu
    matrix_a = [[int(entry_a[row][col].get()) for col in range(cols)] for row in range(rows)]
    vector_c = [int(entry_c[row].get()) for row in range(rows)]

    # Gọi các hàm tính toán
    result_product = matrix_product(matrix_a, matrix_a)  # Tích hai ma trận
    result_dot_product = vector_dot_product(matrix_a, matrix_a)  # Tích vô hướng hai vector
    result_determinant = matrix_determinant(matrix_a)  # Định thức
    result_inverse = matrix_inverse(matrix_a)  # Ma trận nghịch đảo
    result_solve = solve_linear_system(matrix_a, vector_c)  # Giải hệ phương trình

    print("Tích hai ma trận:\n", result_product)
    print("Tích vô hướng hai vector:\n", result_dot_product)
    print("Định thức:\n", result_determinant)
    print("Ma trận nghịch đảo:\n", result_inverse)
    print("Giải hệ phương trình:\n", result_solve)
    
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


# Tạo cửa sổ Tkinter
root = tk.Tk()
root.title("Matrix Calculator")

# Tạo các ô nhập liệu cho số hàng và số cột của ma trận
rows_label = ttk.Label(root, text="Nhập số hàng :")
rows_label.grid(row=0, column=0, padx=5, pady=5)
rows_entry = ttk.Entry(root)
rows_entry.grid(row=0, column=1, padx=5, pady=5)

cols_label = ttk.Label(root, text="Nhập số cột:")
cols_label.grid(row=1, column=0, padx=5, pady=5)
cols_entry = ttk.Entry(root)
cols_entry.grid(row=1, column=1, padx=5, pady=5)

# Tạo nút xác nhận số hàng và số cột
confirm_button = ttk.Button(root, text="Xác nhận", command=create_matrix_inputs)
confirm_button.grid(row=2, columnspan=2, pady=10)

# Tạo frame để chứa widget nhập liệu cho ma trận A và vectơ c
matrix_input_frame = ttk.Frame(root)
matrix_input_frame.grid(row=3, columnspan=2, pady=10)

# Tạo nút tính toán và liên kết với hàm calculate
calculate_button = ttk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=4, columnspan=2, pady=10)

# Khởi chạy giao diện
root.mainloop()
