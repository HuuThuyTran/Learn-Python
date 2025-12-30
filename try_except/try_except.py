# try-except: dùng để bắt xử lý lỗi, giúp cho chương trình ko bị crash khi gặp lỗi trong lúc chạy
# cú pháp:
# try:
#   => đoạn code có thể gây lỗi
# except:
#   => code xử lý khi có lỗi
# Nếu code trong try bị lỗi → Python nhảy sang except
# Nếu không có lỗi → except không chạy
# Ko nên dùng except trống! Nên bắt đúng loại.

# Ví dụ:
try:
    a = int(input("Enter a number: "))
    print(a)
except ValueError:
    print("Invalid input")
print('====================')

# Lỗi 1 số / 0:
try:
    a = int(input('Enter a number A: '))
    b = int(input('Enter a number B: '))
    result = a / b
    print(f'result: {result}')
except ZeroDivisionError:
    print('Error: cannot be divided by 0!')
except ValueError:
    print('Error: Invalid input!')

# try – except – else
# else chạy khi KHÔNG có lỗi
print('====================')

try:
    x = int(input("Nhập số: "))
    print(10 / x)
except ZeroDivisionError:
    print("Không chia được cho 0")
except ValueError:
    print("Nhập sai kiểu dữ liệu")
else:
    print("Chương trình chạy thành công!")

# try – except – finally
# finally luôn chạy, dù try có lỗi hay không
# Thường dùng để đóng file, đóng kết nối
print('====================')

try:
    f = open("test.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("Không tìm thấy file")
finally:
    print("Kết thúc chương trình")

# Bắt nhiều lỗi cùng lúc
print('====================')
try:
    a = int(input("a: "))
    b = int(input("b: "))
    print(a / b)
except (ValueError, ZeroDivisionError):
    print("Lỗi nhập dữ liệu hoặc chia cho 0")

# GHI NHỚ NHANH:
# - except ko nên để trống, viết lỗi cụ thể
# - else -> khi đoạn code trong try ko lỗi thì nhảy sang else
# - finally -> khi đoạn code trong try có lỗi hay ko thì vẫn luôn luôn chạy sang finally