# Kiểu dict: là 1 kiểu dữ liệu lưu trữ theo key-value
# Đặc điểm:
# - Có thứ tự
# - Có thể thay đổi
# - Key là duy nhất
# - Key phải bất biến: Key thường là chuỗi (str), số (int) hoặc tuple. Value có thể là bất cứ kiểu dữ liệu nào.

# Cách khởi tạo:
print('---- PART 1 ----')
# C1: dùng dấu {}
student = {
    "name": "Alex",
    "birthday": "12/01/2001",
    "nationally": "Thailand"
}
# C2: dùng hàm dict()
animal = dict({"name": "Dog", "age": 10})

# Truy key của dict
print(f'student name: {student["name"]}')
print(f'animal name: {animal["name"]}')
print()

# Thay đổi giá trị
print('---- PART 2 ----')
# C1: truy cập key và gán giá trị
student['name'] = 'Bobb'
student['birthday'] = '23/03/2003'
print(f'student: {student}')

# C2: dùng hàm update(dict) -> chọn cách này
animal.update({"age": 21})
print(f'animal: {animal}')
print()

# Thêm các key mới trong dict
print('---- PART 3 ----')
# C1
student['gender'] = 'male'
print(f'student: {student}')

# C2: dùng hàm update()
animal.update({'gender': 'female', 'nick_name': 'Julia'})
print(f'animal: {animal}')
print()

# Loại bỏ key trong dict
print('---- PART 4 ----')

# C1: dùng hàm pop(key) -> xóa theo key chỉ định
animal.pop('nick_name')
print(f'animal: {animal}')

# C2: dùng hàm popitem() -> xóa key được chèn ở cuối
animal.popitem()
print(f'animal: {animal}')

# C3: dùng từ khóa del -> xóa theo key chỉ định hoặc toàn bộ từ điển
del animal['name']
print(f'animal: {animal}')
print()

# Duyệt các key-value trong dict
print('---- PART 5 ----')

# Duyệt theo key
for x in student:
    print(x)
print()

# Duyệt các key: dùng hàm keys()
for x in student.keys():
    print(x)
print()

# Duyệt các value: dùng hàm values()
for x in student.values():
    print(x)
print()

# Duyệt cặp key-value: dùng hàm items
for x, y in student.items():
    print(f'{x}: {y}')