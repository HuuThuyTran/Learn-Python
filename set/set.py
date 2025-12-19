# Kiểu set: dùng để lưu tập hợp phần tử không trùng lặp
# Đặc điểm:
# - Không thứ tự (unordered)
# - Không trùng lặp phần tử
# - Có thể thay đổi (mutable)
# - Không truy cập bằng index
# Cú pháp: my_set = {1, 2, 3, 4, 5}

# Tạo set:
my_set = {1, 2, 3}
subjects = {'math', 'physics', 'chemistry'}
print(f'my_set: {my_set}')
print(f'subjects: {subjects}')
print()

# Tạo set rỗng:
my_set_2 = set()
# Note: my_set_2 = {} -> Nó sai, nó sẽ hiểu là dict rỗng ko phải set rỗng

# Truy cập set:
# Dùng vòng lặp
for number in my_set:
    print(number)
print()

# Thêm phần tử:
# add(item): thêm 1 phần tử
subjects.add('biology')
print(f'subjects when use add(): {subjects}')

# update([] or {}): thêm >= 1 phần tử
subjects_child = ['english', 'history', 'math']
subjects.update(subjects_child)
print(f'subjects when use update(): {subjects}')
print()

# Xóa phần tử:
# remove(item): xóa phần tử theo item, nếu item đó ko tồn tại trong set thì sẽ báo LỖI
subjects.remove('history')
print(f'subjects when use remove(): {subjects}')

# discard(item): giống remove(item) nhưng khác là sẽ ko báo lỗi
subjects.discard('english')
print(f'First, subjects when use discard(): {subjects}')
subjects.discard('english')
print(f'Second, subjects when use discard(): {subjects}')

# pop(): xóa ngẫu nhiên
subjects.pop()
print(f'subjects when use pop(): {subjects}')

# clear(): xóa tất cả
# subjects.clear()
print()

# Các phép toán trong set:
A = {1, 2, 3}
B = {3, 4, 5, 6}
print(f'A: {A}')
print(f'B: {B}')

# Union (Hợp):
print(f'A | B: {A | B}')
# Intersection (Giao):
print(f'A & B: {A & B}')
# Difference (Hiệu):
print(f'A - B: {A - B}')
# Hiệu đối xứng
print(f'A ^ B: {A ^ B}')
print()

# Ứng dụng thực tế:
# 1. Xóa phần tử trùng lặp
nums = [10, 11, 11, 12, 13, 13, 14]
unique_nums = list(set(nums))
print(f'unique_nums: {unique_nums}')

# 2. So sánh 2 danh sách
list_a = [21, 22, 23, 24]
list_b = [22, 23, 24, 25]
common = set(list_a) & set(list_b)
print(f'common: {common}')