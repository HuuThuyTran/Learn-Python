# Hàm là một khối mã chỉ chạy khi được gọi
# Sử dụng từ khóa: def -> để khai báo hàm
# 3 cái quan trọng của hàm: tham số, return, gọi hàm
# Cú pháp:
# def ten_ham(tham_so):
#     code
#     return ket_qua
# Tham số là: biến
# Đối số là: giá trị truyền vào tham số

# Thực hành:
# Khai báo hàm (ko có tham số)
def sayHello():
    print('Hello world!')
    print()
sayHello()

# Khai báo hàm (có tham số)
def sayName(name):
    print(f'Say: {name}')
    print()
sayName('John')

# Hàm có return 1 giá trị
def tinhTich(*giaTri):
    tich = 1
    for x in giaTri:
        tich *= x
    return tich
tich1 = tinhTich(1, 2, 3)
tich2 = tinhTich(6, 7, 8)
print(f'Tich1 = {tich1} | Tich2 = {tich2}')
print()

# Hàm có return nhiều giá trị
def tinh(a, b):
    return a + b, a - b

tong, hieu = tinh(10, 5)
print(f'Tong = {tong} | Hieu = {hieu}')
print()

# Hàm có tham số mặc định
def hpbd(birthday = '30/04/2003'):
    return f'Birthday: {birthday}'
print(hpbd())
print()

# Khi không xác định số đối số, dùng dấu *
def thoiKhoaBieu(*monHoc):
    print(type(monHoc)) # -> type tuple
    print(f'Danh sách môn học: {monHoc}')
    print(f'Môn 1: {monHoc[0]}')
    print(f'Môn 2: {monHoc[1]}')
    print(f'Môn 3: {monHoc[2]}')
    print()
thoiKhoaBieu('Toan', 'Ly', 'Hoa')

# Truyền nhiều đối số vào hàm, dùng dấu **
def helloFullname(**fullname):
    print(type(fullname)) # -> type dict
    print(f'Hello {fullname['name']}, your age: {fullname['age']}, nationality: {fullname['nationality']}')
helloFullname(name='Trung', age=20, nationality='thailand')