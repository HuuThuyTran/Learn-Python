# OOP (Object-Oriented Programming) = Lập trình hướng đối tượng
# => Thay vì viết code lung tung bằng biến & hàm → ta mô tả thế giới bằng “đối tượng”

# Class & Object:
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self):
        print(f'{self.name} is studying!')

    def info(self):
        print(f'Student: {self.name} - age: {self.age}')

s1 = Student('John', 20)
s2 = Student('Marry', 20)

s1.study()
s1.info()
s2.study()
s2.info()

# Giải thích:
# class Student: → tạo class
# __init__ → hàm khởi tạo
# self → đại diện cho chính object đó
# s1, s2 → object
# Note: self luôn phải có trong method của class!