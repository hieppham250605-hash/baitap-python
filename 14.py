import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
import re

# ================= DATABASE =================
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ho TEXT,
    ten TEXT,
    email TEXT,
    password TEXT,
    gender TEXT,
    dob TEXT
)
""")
conn.commit()

# ================= VALIDATION =================
def is_valid_password(pw):
    if len(pw) < 8:
        return False
    if not re.search("[a-z]", pw):
        return False
    if not re.search("[A-Z]", pw):
        return False
    if not re.search("[0-9]", pw):
        return False
    if not re.search("[!@#$%^&*]", pw):
        return False
    return True

# ================= MAIN APP =================
root = tk.Tk()
root.title("Quản lý thành viên")
root.geometry("600x500")

# ================= FRAME SWITCH =================
def clear_frame():
    for widget in root.winfo_children():
        widget.destroy()

# ================= REGISTER SCREEN =================
def show_register():
    clear_frame()

    tk.Label(root, text="Đăng ký", font=("Arial", 18)).pack(pady=10)

    ho = tk.Entry(root)
    ho.insert(0, "Họ")
    ho.pack()

    ten = tk.Entry(root)
    ten.insert(0, "Tên")
    ten.pack()

    email = tk.Entry(root)
    email.insert(0, "Email hoặc SĐT")
    email.pack()

    password = tk.Entry(root, show="*")
    password.insert(0, "")
    password.pack()

    gender = tk.StringVar()
    tk.Radiobutton(root, text="Nam", variable=gender, value="Nam").pack()
    tk.Radiobutton(root, text="Nữ", variable=gender, value="Nữ").pack()

    dob = tk.Entry(root)
    dob.insert(0, "Ngày sinh (dd/mm/yyyy)")
    dob.pack()

    agree = tk.IntVar()
    tk.Checkbutton(root, text="Tôi đồng ý điều khoản", variable=agree).pack()

    def register():
        if not ho.get() or not ten.get() or not email.get() or not password.get():
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ")
            return

        if not is_valid_password(password.get()):
            messagebox.showerror("Lỗi", "Mật khẩu yếu")
            return

        if agree.get() == 0:
            messagebox.showerror("Lỗi", "Bạn chưa đồng ý điều khoản")
            return

        cursor.execute("INSERT INTO users (ho, ten, email, password, gender, dob) VALUES (?, ?, ?, ?, ?, ?)",
                       (ho.get(), ten.get(), email.get(), password.get(), gender.get(), dob.get()))
        conn.commit()

        messagebox.showinfo("OK", "Đăng ký thành công")
        show_list()

    tk.Button(root, text="Đăng ký", command=register).pack(pady=10)

# ================= LIST SCREEN =================
def show_list():
    clear_frame()

    tk.Label(root, text="Danh sách thành viên", font=("Arial", 16)).pack()

    tree = ttk.Treeview(root, columns=("ID", "Họ", "Tên", "Email"), show="headings")
    tree.pack(fill="both", expand=True)

    for col in ("ID", "Họ", "Tên", "Email"):
        tree.heading(col, text=col)

    def load_data():
        for row in tree.get_children():
            tree.delete(row)
        for row in cursor.execute("SELECT id, ho, ten, email FROM users"):
            tree.insert("", "end", values=row)

    load_data()

    def delete_user():
        selected = tree.selection()
        if not selected:
            return
        user_id = tree.item(selected[0])["values"][0]
        cursor.execute("DELETE FROM users WHERE id=?", (user_id,))
        conn.commit()
        load_data()

    def edit_user():
        selected = tree.selection()
        if not selected:
            return

        user_id = tree.item(selected[0])["values"][0]

        edit_win = tk.Toplevel(root)
        edit_win.title("Sửa")

        tk.Label(edit_win, text="Tên mới").pack()
        new_name = tk.Entry(edit_win)
        new_name.pack()

        def save():
            cursor.execute("UPDATE users SET ten=? WHERE id=?", (new_name.get(), user_id))
            conn.commit()
            load_data()
            edit_win.destroy()

        tk.Button(edit_win, text="Lưu", command=save).pack()

    tk.Button(root, text="Xóa", command=delete_user).pack(side="left", padx=10, pady=10)
    tk.Button(root, text="Sửa", command=edit_user).pack(side="left", padx=10)
    tk.Button(root, text="Đăng ký mới", command=show_register).pack(side="right", padx=10)

# ================= START =================
show_register()
root.mainloop()