# break: tác dụng để thoát khỏi vòng lặp ngay lập tức
# continue: tác dụng để bỏ qua lần lặp hiện tại khi gặp nó
# Note:
# - break và continue chỉ dùng trong vòng lặp
# có thể dùng trong vòng lặp gần nhau. (Chỉ tác động lên vòng lặp gần nhất)

# Vd cụ thể:
# Dùng break
print("==== BREAK ====")
for i in range(1, 10):
    if i == 6: break
    print(i)

# Dùng continue
print("==== CONTINUE ====")
for j in range(1, 10):
    if j == 5: continue
    print(j)

# Vd thực tế:
# Nhập mật khẩu đúng thì dừng
password = "123456"
while True:
    your_password = input("Enter your password: ")
    if your_password == password:
        print("You have entered the correct password!")
        break
    else:
        print("Incorrect password!")