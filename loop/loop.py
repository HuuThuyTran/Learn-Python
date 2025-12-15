# Cú pháp vòng lặp: for __ in __
# Duyệt qua một danh sách
print("==== VÒNG LẶP DUYỆT QUA LIST ====")
animals = ["lion", "tiger", "dog", "fish", "giraffe"]
for animal in animals:
    print(animal)

# Duyệt qua một chuỗi
print("==== VÒNG LẶP DUYỆT QUA CHUỖI ====")
name = "Kim-Sang-Sik"
for n in name:
    print(n)

# Sử dụng hàm range(x, y)
# In bảng cửu chương
print("==== BẢNG CỬU CHƯƠNG ====")
for x in range(2, 10):
    for y in range(1, 11):
        print(f'{x} x {y} = {x * y}')
    print("")