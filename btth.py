import math

class PhanSo:
    def __init__(self, tu_so, mau_so=1):
        if mau_so == 0:
            raise ValueError("Mẫu số không được bằng 0")
        self.tu_so = tu_so
        self.mau_so = mau_so
        self.toi_gian()

    # 🔹 Tối giản phân số
    def toi_gian(self):
        ucln = math.gcd(self.tu_so, self.mau_so)
        self.tu_so //= ucln
        self.mau_so //= ucln

        # Đưa dấu âm lên tử
        if self.mau_so < 0:
            self.tu_so *= -1
            self.mau_so *= -1

    # 🔹 Cộng
    def cong(self, other):
        tu = self.tu_so * other.mau_so + other.tu_so * self.mau_so
        mau = self.mau_so * other.mau_so
        return PhanSo(tu, mau)

    # 🔹 Trừ
    def tru(self, other):
        tu = self.tu_so * other.mau_so - other.tu_so * self.mau_so
        mau = self.mau_so * other.mau_so
        return PhanSo(tu, mau)

    # 🔹 Nhân
    def nhan(self, other):
        tu = self.tu_so * other.tu_so
        mau = self.mau_so * other.mau_so
        return PhanSo(tu, mau)

    # 🔹 Chia
    def chia(self, other):
        if other.tu_so == 0:
            raise ValueError("Không thể chia cho 0")
        tu = self.tu_so * other.mau_so
        mau = self.mau_so * other.tu_so
        return PhanSo(tu, mau)

    # 🔹 Hiển thị
    def __str__(self):
        return f"{self.tu_so}/{self.mau_so}"