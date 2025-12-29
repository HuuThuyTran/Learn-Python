# Declare class: SimpleClass
class SimpleClass:
    # Attributes
    i = 3

    # Constructor
    def __init__(self):
        print('--Called--')
        self.j = 7

    # Methods
    def printMe(self, name):
        print(f'Hello, my name is {name}')

    def printMe2(self, letter):
        print(f'== {letter} ==')
        print(self.i)
        print(self.j)

# Declare variable object
objA, objB = SimpleClass(), SimpleClass()
# objA.printMe('A')
# objB.printMe('B')
objA.i = 100
objB.j = 300
objA.printMe2('A')
objB.printMe2('B')

# Declare class: SimpleClass2
class SimpleClass2:
    # constructor
    def __init__(self):
        self.name = 'John'
        self.age = 32
        self.nationality = 'China'

    # methods
    def hello(self):
        print(f'Hello, {self.name}!')

    # static methods
    @staticmethod
    def hi(name):
        print(f'Hi, {name}')

# Declare objC, objD
print('-------SimpleClass2-------')
objC = SimpleClass2()
objD = SimpleClass2()

objC.hello()
objD.hello()

objC.hi('Pan')
SimpleClass2.hi('Vivi')

# Bai tap:
# Xay dung class Ngay, co cac thuoc tinh: ngay, thang, nam
# Xay dung phuong thuc co:
# - Cho biet ngay thu bao nhieu trong nam
# - Cho biet thang do co bao nhieu ngay (statiic_method)


print('-------CLASS NGAY--------')

# class Ngay
class Ngay:
    # constructor
    def __init__(self, ngay, thang, nam):
        self.ngay = ngay
        self.thang = thang
        self.nam = nam

    # static method
    @staticmethod
    def xacDinhSoNgayTrongThang(thang, nam):
        if thang in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif thang in [4, 6, 9, 11]:
            return 30
        else:
            condition = (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0)
            return 29 if condition else 28

    # methods
    def ngayTrongNam(self):
        # Khai bao bien
        giaTriNgayTrongNam = 0

        # Tinh tong so luong ngay cua nhung thang truoc
        for x in range(1, self.thang):
            giaTriNgayTrongNam += self.xacDinhSoNgayTrongThang(x, self.nam)

        # Cong them so ngay cua thang hien tai
        giaTriNgayTrongNam += self.ngay

        # Tra ve ket qua soNgayTrongNam
        return giaTriNgayTrongNam

# khai bao doi tuong
ngayA = Ngay(24, 4, 2025)
ngayB = Ngay(31, 8, 2025)

# in ngay trong nam
print(f'Ket qua cua ngay A ({ngayA.ngay}/{ngayA.thang}/{ngayA.nam}): {ngayA.ngayTrongNam()} ngay')
print(f'Ket qua cua ngay B ({ngayB.ngay}/{ngayB.thang}/{ngayB.nam}): {ngayB.ngayTrongNam()} ngay')