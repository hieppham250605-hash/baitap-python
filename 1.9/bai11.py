# Nhập n
n = int(input("Nhập n: "))

# List cho trước
_list = ['abc', 'hello', 'hi', 'python', 'code']

# Lọc các từ có độ dài > n
result = []
for x in _list:
    if len(x) > n:
        result.append(x)

print("Các từ có độ dài >", n, "là:", result)