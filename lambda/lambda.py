# Lambda hiểu đơn giản là: hàm rút gọn - dùng khi viết code ngắn, làm nhanh 1 việc
# Cú pháp -> lambda arguments : expression
# - lambda thay cho def
# - Sau : là giá trị trả về
# - Tự return

# Hàm tính tổng
sum = lambda a, b: a+b
print(f'Sum = {sum(10, 10)}')

# In số chẵn và lẻ
number = lambda num: 'odd number' if (num % 2) != 0 else 'even number'
print(f'Number = {number(10)}')

# Lambda + map()
# 👉 Áp dụng cho từng phần tử trong list
nums = [1, 2, 3, 4, 5]
binh_phuong = list(map(lambda n: n**2, nums))
print(f'Binh phuong = {binh_phuong}')

# Lambda + filter()
loc_so_chan = list(filter(lambda n: n % 2 == 0, nums))
print(f'Loc so chan = {loc_so_chan}')

# Lambda + sort()
students = [
    {"name": "Thủy", "score": 8},
    {"name": "An", "score": 6},
    {"name": "Bình", "score": 9}
]

students.sort(key=lambda s: s["score"])
print(f'Students = {students}')