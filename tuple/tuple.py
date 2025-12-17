# Kiểu tuple: giống kiểu list nhưng không thay đổi đc, không thêm đc, ...
# Tốc độ nhanh và an toàn hơn
# Dùng khi dữ liệu cố định
# Cú pháp: my_tuple = (1, 2, 3)

# Tạo tuple
genders = ('male', 'female')
numbers = (10, 20, 30)

# Truy cập phần tử
# Truy cập phần tử: 'male' của biến genders
print(f'genders[0] = {genders[0]}')
# Truy cập phần tử: 30 của biến numbers
print(f'numbers[-1] = {numbers[-1]}')
print()

# Duệt tuple
for gender in genders:
    print(gender)
for number in numbers:
    print(number)
print()

# Giải nén tuple
fruits = ('apple', 'banana', 'orange')
a, b, o = fruits
print(f'a: {a}, b: {b}, o: {o}')
print()

# Từ khóa: in
# Dùng để kiểm tra một phần tử có trong tuple hay ko?
print(f'Check apple in fruits: {"apple" in fruits}')
print(f'Check kiwi in fruits: {"kiwi" in fruits}')
print()

# Tuple lồng nhau
students = (
    ("Thuy", 20),
    ("An", 21)
)

# In tên Thuy và tuổi 20
print(f'students[0][0] = {students[0][0]}')
print(f'students[0][1] = {students[0][1]}')

# In tên An và tuổi 21
print(f'students[1][2] = {students[1][0]}')
print(f'students[1][2] = {students[1][1]}')
print()

# Sắp xếp tuple và chuyển thành list
# Dùng: sorted()
list_fruits = sorted(fruits)
print(f'list_fruits: {list_fruits}')
print(f'type: {type(list_fruits)}')