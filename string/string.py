# 1. Tạo và Truy cập chuỗi
print("1. Tạo và Truy cập chuỗi (str)")

# Tạo biến với giá trị thuộc kiểu string
s = " Alan Walker  "
s1 = "Hello World"
s2 = "python"
s3 = """ 
Line 1 
Line 2 
Line 3
""" # => Đây là chuỗi nhiều dòng

# Truy cập chuỗi (tương dương như truy cập phần tử bên list)
print(s1[0]) # => Kết quả: "H"
print(s2[0]) # => Kết quả: "P"
print(s3[2]) # => Kết quả: "L"

# Lấy chuỗi con
print(f's[1:5] = {s[1:5]}')
print(f's1[6:] = {s1[6:]}')
print(f's2[0:2] = {s2[0:2]}')
print()

# 2. Chuỗi làm việc với toán tử
print("2. Chuỗi làm việc với toán tử")

# a. Chuỗi với toán tử +
print(f's1 + s2 = {s1 + s2}') # Note: Trong python chỉ cho phép nối chuỗi với chuỗi
print()

# b. Chuỗi với toán tử *
chep_phat = "Em xin hứa sẽ làm bài tập đầy đủ!\n"
chep_phat_10 = chep_phat * 10
print(chep_phat_10)

# 3. Kiểm tra chuỗi con trong chuối cha
print("3. Kiểm tra chuỗi con trong chuối cha")
str1 = "Junior Dev"
str2 = "Junior"
str3 = "Master"

if str2 in str1:
    print("str2 inside str1")
else:
    print("str2 is not inside str1!")

if str3 in str1:
    print("str3 inside str1")
else:
    print("str3 is not inside str1!")
print()

# 4. Các phương thức phổ biến khi làm việc với chuỗi (str)
print("4. Các phương thức phổ biến khi làm việc với chuỗi (str)")

# a. upper() / lower() / capitalize(): hàm dùng để in hoa / thường chuỗi / in hoa chữ cái đầu
print(f's1.upper(): {s1.upper()}')
print(f's1.lower(): {s1.lower()}')
print(f's2.capitalize(): {s2.capitalize()}')
print()

# b. strip(): hàm dùng để xóa khoảng trắng đầu và cuối của chuỗi
print(f's.strip(): {s.strip()}')
print()

# c. find(item): tìm chuỗi con trong chuỗi cha, trả về con số vị trí đầu tiên theo item truyền vào, ngược lại trả về -1
#    count(item): đếm chuỗi con trong chuỗi cha
str4 = "This is high-level programing language. Python is a widely used, high-level programming language known for its simple, English-like syntax and high readability. Python is good!"
print(f'str4.find("Python"): {str4.find("Python3")}')
print(f'str4.count("Python"): {str4.count("Python")}')
print()

# d. replace(__odd, __new): hàm dùng để thay thế cái __odd thành cái __new
str5 = "Xin chào , tôi tên là Seven"
print(f'str5 ban đầu: {str5}')
print(f'str5.replace("Seven", "Thuy"): {str5.replace("Seven", "Thủy")}')
print()

# e. split(item): hàm dùng để cắt chuối thành một list
print(f'str5.split(): {str5.split(" ")}')