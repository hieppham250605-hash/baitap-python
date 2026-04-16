import sqlite3

conn = sqlite3.connect("qlbh.db")
cursor = conn.cursor()

# ================= TABLE =================
cursor.execute("""
CREATE TABLE IF NOT EXISTS mathang (
    ma TEXT PRIMARY KEY,
    ten TEXT,
    nguongoc TEXT,
    gia REAL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS khachhang (
    ma TEXT PRIMARY KEY,
    ten TEXT,
    diachi TEXT,
    sdt TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS hoadon (
    ma TEXT PRIMARY KEY,
    makh TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS chitiethoadon (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    mahd TEXT,
    mamh TEXT,
    soluong INTEGER,
    dongia REAL
)
""")

conn.commit()

# ================= MẶT HÀNG =================
def them_mathang():
    ma = input("Mã: ")
    ten = input("Tên: ")
    nguongoc = input("Nguồn gốc: ")
    gia = float(input("Giá: "))
    cursor.execute("INSERT INTO mathang VALUES (?, ?, ?, ?)", (ma, ten, nguongoc, gia))
    conn.commit()

def hien_mathang():
    for r in cursor.execute("SELECT * FROM mathang"):
        print(r)

def tim_mathang():
    k = input("Tìm: ")
    for r in cursor.execute("SELECT * FROM mathang WHERE ma LIKE ? OR ten LIKE ? OR nguongoc LIKE ?", 
                            ('%'+k+'%', '%'+k+'%', '%'+k+'%')):
        print(r)

# ================= KHÁCH HÀNG =================
def them_kh():
    ma = input("Mã: ")
    ten = input("Tên: ")
    diachi = input("Địa chỉ: ")
    sdt = input("SĐT: ")
    cursor.execute("INSERT INTO khachhang VALUES (?, ?, ?, ?)", (ma, ten, diachi, sdt))
    conn.commit()

def hien_kh():
    for r in cursor.execute("SELECT * FROM khachhang"):
        print(r)

# ================= HÓA ĐƠN =================
def them_hd():
    ma = input("Mã HĐ: ")
    makh = input("Mã KH: ")
    cursor.execute("INSERT INTO hoadon VALUES (?, ?)", (ma, makh))
    conn.commit()

def them_cthd():
    mahd = input("Mã HĐ: ")
    mamh = input("Mã MH: ")
    soluong = int(input("Số lượng: "))
    dongia = float(input("Đơn giá: "))
    cursor.execute("INSERT INTO chitiethoadon (mahd, mamh, soluong, dongia) VALUES (?, ?, ?, ?)",
                   (mahd, mamh, soluong, dongia))
    conn.commit()

def hien_hd():
    rows = cursor.execute("SELECT * FROM hoadon").fetchall()
    print("\n--- DANH SÁCH HÓA ĐƠN ---")
    for r in rows:
        mahd = r[0]
        tong = cursor.execute("""
        SELECT SUM(soluong * dongia) FROM chitiethoadon WHERE mahd=?
        """, (mahd,)).fetchone()[0]
        print(r, "Tổng tiền:", tong if tong else 0)

def xem_chitiet():
    mahd = input("Nhập mã HĐ: ")
    rows = cursor.execute("""
    SELECT mamh, soluong, dongia, (soluong * dongia) 
    FROM chitiethoadon WHERE mahd=?
    """, (mahd,))
    print("\n--- CHI TIẾT ---")
    for r in rows:
        print("Mã MH:", r[0], "| SL:", r[1], "| Giá:", r[2], "| Thành tiền:", r[3])

# ================= MENU =================
def menu():
    while True:
        print("""
========= QUẢN LÝ =========
1. Thêm mặt hàng
2. Hiện mặt hàng
3. Tìm mặt hàng
4. Thêm khách hàng
5. Hiện khách hàng
6. Tạo hóa đơn
7. Thêm chi tiết hóa đơn
8. Hiện hóa đơn
9. Xem chi tiết hóa đơn
0. Thoát
""")
        chon = input("Chọn: ")

        if chon == "1": them_mathang()
        elif chon == "2": hien_mathang()
        elif chon == "3": tim_mathang()
        elif chon == "4": them_kh()
        elif chon == "5": hien_kh()
        elif chon == "6": them_hd()
        elif chon == "7": them_cthd()
        elif chon == "8": hien_hd()
        elif chon == "9": xem_chitiet()
        elif chon == "0": break
        else: print("Sai!")

menu()
conn.close()