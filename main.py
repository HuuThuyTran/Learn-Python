a = int(input("Enter a number A: "))
b = int(input("Enter a number B: "))

print("====== Ví dụ về toán tử số học ======")
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b}')
print(f'{a} % {b} = {a % b}')
print(f'{a} ** {b} = {a ** b}')
print(f'{a} // {b} = {a // b}')

print("====== Ví dụ về toán tử so sánh ======")
print(f'{a} > {b}: {a > b}')
print(f'{a} < {b}: {a < b}')
print(f'{a} >= {b}: {a >= b}')
print(f'{a} <= {b}: {a <= b}')
print(f'{a} != {b}: {a != b}')
print(f'{a} == {b}: {a == b}')

print("====== Ví dụ về toán tử logic ======")
print(f'{(a > b) and (a < b)}')
print(f'{(a > b) or (a < b)}')
print(f'{not (a > b)}')

print("====== Ví dụ về toán tử is và is not ======")

x = 1000
y = 1000
print(x is not y)