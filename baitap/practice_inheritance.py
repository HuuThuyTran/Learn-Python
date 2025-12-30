# Bai tap: ve dong vat
# Xay dung class cha: Animal
# Cu phap ke thua:
# class Parent:
#     pass
# class Child(Parent):
#     pass
#--------------------------------------------------
# Create class Animal
class Animal:
    # constructor
    def __init__(self, type, name, width, height, weight):
        self.type = type
        self.name = name
        self.width = width
        self.height = height
        self.weight = weight

    # method 1
    def makeVoice(self):
        print('Unknow voice')

    # method 2
    def printInfo(self):
        print(f'Type: {self.type}, Name: {self.name}, Width: {self.width}, Height: {self.height}, Weight: {self.weight}')

# 1. Co ban
class Dog(Animal):
    # 1. Ke thua __init__()
    def __init__(self, type, name, width, height, weight, nationality):
        super().__init__(type, name, width, height, weight)
        self.nationality = nationality
    # 2. Them phuong thuc rieng cho class
    def eat(self):
        print(f'2. {self.type} eating!')
    # 3. Ghi de phuong thuc
    def makeVoice(self):
        print(f'3. {self.type} voice!')
    # 4. Dung tu khoa super()
    def printInfo(self):
        print(f'4. {self.type} info!')
        super().printInfo()
        print(f'Nationality: {self.nationality}!')

class Cat(Animal):
    def __init__(self, type, name, width, height, weight, nationality):
        super().__init__(type, name, width, height, weight)
        self.nationality = nationality
    def eat(self):
        print(f'a. {self.type} eating!')
    def makeVoice(self):
        print(f'b. {self.type} meow meow!')
    def printInfo(self):
        print(f'c. {self.type} info!')
        super().printInfo()
        print(f'Nationality: {self.nationality}!')

dog = Dog('dog', 'Goofy', 100, 100, 100, 'argentina')
dog.eat()
dog.makeVoice()
dog.printInfo()
print('============================')
cat = Cat('cat', 'Carry', 60, 80, 30, 'portugal')
cat.eat()
cat.makeVoice()
cat.printInfo()