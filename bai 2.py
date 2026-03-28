a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))

if a + b > c and a + c > b and b + c > a:
    print("Đây là độ dài ba cạnh tam giác")
else:
    print("Đây không phải độ dài ba cạnh tam giác")