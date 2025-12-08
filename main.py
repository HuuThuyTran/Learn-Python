print("==== Su dung toan tu 3 ngoi ====")
n = int(input("Enter a number n: "))
number = "even" if (n % 2) == 0 else "odd"
print(f'Number: {number}')

print("==== Cau lenh re nhanh ====")
x = float(input("Enter a number x: "))
if (x % 2) == 0:
    print(x, "is positive integers")
else:
    print(x, "is negative integers")

if x >= 9:
    print("Rank: A")
elif x >= 8:
    print("Rank: B")
elif x >= 6.0 or x >= 7.0:
    print("Rank: C")
else:
    print("Rank: D")