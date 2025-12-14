# Kiểu list này giống kiểu mảng trong mấy ngôn ngữ khác
# Có thể lưu nhiều giá trị thuộc nhiều kiểu dũ liệu khác nhau trong cùng một biến danh sách
# Có thứ tự, có thể thay đổi (Bạn có thể thêm, xóa, sửa đổi các phần tử sau khi tạo list.), định nghĩa bằng dấu []
# Đặt tên biến và hàm là: snake-case
# Đặt tên class là: pascal-case

# ---------------------------------------------

# Tạo list rỗng
print("==== List rỗng ====")
empty_list = [] # Cách 1
empty_list2 = list() # Cách 2
print(f'empty_list: {empty_list}')
print(f'empty_list2: {empty_list2}')

# Tạo list có giá trị
print("==== List có giá trị ====")
my_list = ['football', 10, True]
numbers = [1, 2, 3, 4, 5]
colors = ['red', 'blue', 'green', 'yellow']
print(f'my_list: {my_list}')
print(f'numbers: {numbers}')
print(f'colors: {colors}')

# In câu danh sách sinh viên
print("==== Danh sách sinh viên ====")

# Tạo danh sách sinh viên
students = ["An", "Bình", "Cảnh", "Duy"]

# Lấy tất cả các bạn sinh viên
print(f'Danh sách tất cả sinh viên: {students}') # Cách 1
print(f'Danh sách tất cả sinh viên: {students[:]}')# Cách 2

# Lấy các sinh viên theo vị trí từ x đến y
# Cú pháp: students[x:y] => có nghĩa là nó sẽ lấy phần tử từ [x:y)

# a. Lấy sinh viên: Cảnh, Duy
print(f'Sinh viên vị trí 2 với 3: {students[2:4]}')
# b. Lấy sinh viên: Bình, Cảnh
print(f'Sinh viên vị trí 1, 2: {students[1:3]}')
# c. Lấy sinh viên: An, Cảnh
print(f'Sinh viên vị trí 0, 2: {students[0:3]}')

# Các thao tác cơ bản trong list:
print("==== Thao tác cơ bản với list ====")

# I. Truy cập phần tử
print("I. Truy cập phần tử")
print(f'students[0] = {students[0]}')
print(f'students[1] = {students[1]}')
print(f'students[-1] = {students[-1]}') # có thể dùng chỉ mục số âm để gọi tới giá trị cuối cùng

# II. Sửa đổi phần tử
print("II. Sửa đổi phần tử")
# Thay sinh viên vị trí thứ nhất -> Huy
students[0] = 'Huy'
# Thay sinh viên vị trí thứ hai -> Giang
students[1] = 'Giang'
# Thay sinh viên vị trí thứ ba -> Sinh
students[2] = 'Sinh'
# Thay sinh viên vị trí thứ tư -> Khánh
students[3] = 'Khanh'
print(f'students = {students}')

# III. Thêm phần tử
print("III. Thêm phần tử")
# append(): thêm phần tử vào cuối vị trí
students.append("Tung")
students[len(students):] = ["Trang"]

# insert(): thêm phần tử vào vị trí mong muốn cụ thể
# Thêm sinh viên tên Khanh vào vị trí số 2 trong danh sách
students.insert(2, 'Khanh')
# Thêm sinh viên tên Trung vào vị trí số 1 trong danh sách
students.insert(0, 'Trung')

# In danh sách sau khi thêm sinh viên
print(f'Danh sach sinh vien khi duoc them: {students}')

# IV. Xóa phần tử
print("IV. Xóa phần tử")
# remove(): xóa phần tử đầu tiên băng giá trị khớp
# Xóa bạn Sinh trong danh sách
students.remove("Sinh")
# Xóa bạn Khanh trong danh sách
students.remove("Khanh")

# pop(): xóa phần tử trong danh sách bằng vị trí
# Xóa sinh viên Giang trong danh sách
students.pop(2)
# Xóa sinh viên Trang trong danh sách
students.pop(len(students) - 1)

# clear(): xóa tất cả phần tử trong danh sách
# students.clear()

# In danh sách sau xóa
print(f'Danh sách sau khi xóa: {students}')

# V. Kiểm tra số lượng phần tử và đếm số lượng phần tử trong danh sách
print('V. Kiểm tra số lượng phần tử và đếm số lượng phần tử')

# -> Kiểm tra số lượng ptử: len()
print(f'Kiểm tra số lượng phần tử: {len(students)}')

# -> Đếm số lượng ptử phải thỏa điều kiện: count()
# Đếm tên Tung trong danh sách
print(f'Đếm tên Tung: {students.count('Tung')}')
# Đếm tên Khanh trong danh sách
print(f'Đếm tên Khanh: {students.count('Khanh')}')

# VI. Đảo ngược phần tử
# reverse(): đảo ngược phần tử trong danh sách
print("VI. Đảo ngược phần tử")
students.reverse()
print(f'Danh sách sau khi đảo ngươc: {students}')

# VII. Sắp xếp phần tử
# sort(): sắp xếp các phần tử
# Nếu là kiểu str: thì nó sẽ sắp xếp alpha bet
# Nếu lả kiểu number: nó có thể sắp xếp tăng dần, giảm dần

print("VII. Sắp xếp phần tử")
students.reverse()
print(f'Danh sách sinh vien khi sắp xếp: {students}')

# Tạo danh sách numbers
numbers = [0, 9, 5, 3, 10, 1, 20]

# Danh sách numbers tăng dần
numbers.sort(reverse=False)
print(f'Danh sách numbers tăng dần: {numbers}')

# Danh sách numbers giảm dần
numbers.sort(reverse=True)
print(f'Danh sách numbers giảm dần: {numbers}')