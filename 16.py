import sqlite3

# ================= DATABASE =================
conn = sqlite3.connect("nhansu.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS nhansu (
    cccd TEXT PRIMARY KEY,
    hoten TEXT,
    ngaysinh TEXT,
    gioitinh TEXT,
    diachi TEXT
)
""")
conn.commit()

# ================= CHỨC NĂNG =================

# ➕ Thêm nhân sự
def them():
    cccd = input("Nhập CCCD: ")
    hoten = input("Nhập họ tên: ")
    ngaysinh = input("Nhập ngày sinh: ")
    gioitinh = input("Nhập giới tính: ")
    diachi = input("Nhập địa chỉ: ")

    try:
        cursor.execute("INSERT INTO nhansu VALUES (?, ?, ?, ?, ?)",
                       (cccd, hoten, ngaysinh, gioitinh, diachi))
        conn.commit()
        print("✔ Thêm thành công")
    except:
        print("❌ CCCD đã tồn tại")

# 📋 Hiển thị
def hienthi():
    rows = cursor.execute("SELECT * FROM nhansu").fetchall()
    print("\n--- DANH SÁCH NHÂN SỰ ---")
    for r in rows:
        print(r)

# ❌ Xóa
def xoa():
    cccd = input("Nhập CCCD cần xóa: ")
    cursor.execute("DELETE FROM nhansu WHERE cccd=?", (cccd,))
    conn.commit()
    print("✔ Đã xóa")

# ✏ Sửa
def sua():
    cccd = input("Nhập CCCD cần sửa: ")

    hoten = input("Tên mới: ")
    ngaysinh = input("Ngày sinh mới: ")
    gioitinh = input("Giới tính mới: ")
    diachi = input("Địa chỉ mới: ")

    cursor.execute("""
    UPDATE nhansu 
    SET hoten=?, ngaysinh=?, gioitinh=?, diachi=?
    WHERE cccd=?
    """, (hoten, ngaysinh, gioitinh, diachi, cccd))

    conn.commit()
    print("✔ Cập nhật thành công")

# 🔍 Tìm kiếm
def timkiem():
    keyword = input("Nhập từ khóa (CCCD / tên / địa chỉ): ")

    rows = cursor.execute("""
    SELECT * FROM nhansu
    WHERE cccd LIKE ? OR hoten LIKE ? OR diachi LIKE ?
    """, ('%'+keyword+'%', '%'+keyword+'%', '%'+keyword+'%')).fetchall()

    print("\n--- KẾT QUẢ ---")
    for r in rows:
        print(r)

# ================= MENU =================
def menu():
    while True:
        print("""
========= QUẢN LÝ NHÂN SỰ =========
1. Thêm nhân sự
2. Hiển thị danh sách
3. Xóa nhân sự
4. Sửa nhân sự
5. Tìm kiếm
0. Thoát
""")
        chon = input("Chọn: ")

        if chon == "1":
            them()
        elif chon == "2":
            hienthi()
        elif chon == "3":
            xoa()
        elif chon == "4":
            sua()
        elif chon == "5":
            timkiem()
        elif chon == "0":
            break
        else:
            print("Sai lựa chọn!")

# ================= RUN =================
menu()
conn.close()