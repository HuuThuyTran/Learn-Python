# Vòng lặp: dùng để lặp một khối mã khi điều kiện nó đúng
# While(condition): dùng để lặp mà KHÔNG BIẾT SỐ LẦN LẶP

# Bài tập: Tính tổng từ 1 đền n
# n = int(input("Enter a number: "))
# value = 1
# sum = 0
#
# while value <= n:
#     sum += value  # sum = sum + value
#     value += 1    # value = value + 1
# print(f'Sum = {sum}')

# Bài tập: Chuyển đổi số thập phân sang nhị phân

# B1: Cho người dùng: nhập số x > 0, nhập sai bắt nhập lại
x = -1
while x <= 0:
    x = int(input("Enter a number (x > 0): "))
    message = "=> Invalid input! Please try again." if x < 0 else "=> Valid input. Ok"
    print(message)

# B2: Chuyển số thập phân sang số nhị phân
result = ""
while x > 0:
    result = str(x % 2) + result
    x //= 2

# B3: In ra kết quả
print(f'Result = {result}')