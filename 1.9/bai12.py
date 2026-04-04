# Nhập n
n = int(input("Nhập độ dài n: "))

# List cho trước
_list = ['abc', 'xyz', 'aba', '1221', 'ii', 'ii2', '5yhy5']

count = 0

for x in _list:
    if len(x) >= n and x[0] == x[-1]:
        count += 1

print("Số chuỗi thỏa mãn:", count)