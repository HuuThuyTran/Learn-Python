# -----------------------------------------------------
# Bai 1: Giải phương trình bậc hai ax^2 + bx + c = 0
# -----------------------------------------------------

print('==== Bai 1: giai phuong trinh bac 2:  ax^2 + bx + c = 0 ====')

# Import thu vien math
import math

# Nhap 3 so nguyen a, b, c:
a = float(input("Nhap so a: "))
b = float(input("Nhap so b: "))
c = float(input("Nhap so c: "))

# Su dung: cau lenh re nhanh:
if a != 0:
    delta = b ** 2 - (4 * a * c)
    if delta < 0:
        print("Phuong trinh vo nghiem!")
    elif delta == 0:
        x = (-b / (2 * a))
        print(f'Phuong trinh co nghiem kep: x1 = x2 = {x}')
    elif delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f'Phuong trinh co 2 nghiem phan biet: x1 = {x1} va x2 = {x2}')
else:
    print("Khong phai la phuong trinh bac 2!")

# -----------------------------------------------------
# Bai 2:
# Nhập 3 điểm trên hệ trục tọa độ Oxy
# Xác định 3 điểm có tạo thành tam giác không ?
# Nếu tạo thành tam giác:
# a. Xuất ra chu vi của tam giác
# b. Xuất ra diện tích của tam giác
# -----------------------------------------------------

print('==== Bai 2: Xac dinh 3 diem co phai tam giac, roi tinh chu vi & dien tich cua tam giac ====')

# Nhap gia tri cho cac gia tri: xA, yA, xB, yB, xC, yC
xA = float(input("Nhap so xA: "))
yA = float(input("Nhap so yA: "))
xB = float(input("Nhap so xB: "))
yB = float(input("Nhap so yB: "))
xC = float(input("Nhap so xC: "))
yC = float(input("Nhap so yC: "))

# Tinh cac canh trong tam giac
ab = math.sqrt((xB - xA) ** 2 + (yB - yA) ** 2)
bc = math.sqrt((xC - xB) ** 2 + (yC - yB) ** 2)
ac = math.sqrt((xC - xA) ** 2 + (yC - yA) ** 2)

# Kiem tra co phai tam giac ko (2 cạnh bên cộng lại lớn hơn cạnh còn lại là: hình tam giác)
condition1 = (ab + bc > ac)
condition2 = (ab + ac > bc)
condition3 = (bc + ac > ab)

if condition1 and condition2 and condition3:
    # In câu xác định đây là tam giác:
    print('Đây là hình tam giác')

    # Tinh chu vi tam giac
    perimeter = ab + bc + ac
    print(f'Chu vi tam giác: {perimeter}')

    # Tinh dien tich tam giac
    p = perimeter / 2
    area = math.sqrt(p * (p - ab) * (p - bc) * (p - ac))
    print(f'Diện tích tam giác: {area}')
else:
    print("Không tạo thành tam giác!")