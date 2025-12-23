# Bài làm:
# Tạo biến dictionary
dictionary = dict()

# Chương trình tra cứu từ điển Anh - Việt
while True:
    # Tạo menu chương trình
    print('------ CHƯƠNG TRÌNH TRA CỨU TỪ ĐIỂN ANH-VIỆT ------')
    print('1. Thêm một từ vựng mới (kèm nghĩa của từ vựng) vào từ điển')
    print('2. Tra cứu ý nghĩa của một từ vựng')
    print('3. Cập nhật nghĩa ý nghĩa cho một từ vựng')
    print('4. Cho phép người dùng xóa đi một từ vựng trong từ điển')
    print('5. Cho phép người dùng xóa toàn bộ từ vựng')
    print('6. Cho phép người dùng in ra toàn bộ từ vựng')
    print('7. Cho phép người dùng in ra toàn bộ từ điển theo cấu trúc: "TỪ VỰNG: Ý NGHĨA"')
    print('8. Kết thúc chương trình')
    print(f'Dictionary: {dictionary}')

    # Tạo biến select
    select = input("=> Vui lòng chọn chức năng bên trên: ")
    if not select.isdigit():
        print('Vui lòng nhập số từ 1 -> 8!')
        continue
    select = int(select)

    # Xử lý khi người dùng nhập chức năng
    if select == 1:
        print('CHỨC NĂNG SỐ 1')
        vocabulary = input('Nhập từ vừng mới: ').lower()
        mean = input('Nhập ý nghĩa đi kèm: ')
        if vocabulary not in dictionary:
            dictionary[vocabulary] = mean
            print('Thêm từ thành công!')
        else:
            print('Trùng từ trong từ điển. Vui lòng nhập từ mới!')
    elif select == 2:
        print('CHỨC NĂNG SỐ 2')
        search = input('Nhập từ vựng muốn tra nghĩa: ').lower()
        if search in dictionary:
            print(f'{search} có nghĩa là: {dictionary[search]}')
        else:
            print(f'Không tìm thấy từ {search}!')
    elif select == 3:
        print('CHỨC NĂNG SỐ 3')
        vocabulary = input('Nhập từ vựng muốn sửa: ').lower()
        mean = input('Nhập ý nghĩa đi kèm: ')

        if vocabulary not in dictionary:
            print(f'Không có từ {vocabulary} trong từ điển!')
        else:
            dictionary.update({vocabulary: mean})
            print('Cập nhật thành công!')
    elif select == 4:
        print('CHỨC NĂNG SỐ 4')
        vocabulary = input('Nhập từ vựng muốn xóa: ').lower()

        if vocabulary not in dictionary:
            print(f'Không có từ {vocabulary} trong từ điển')
        else:
            dictionary.pop(vocabulary)
            print('Xóa thành công!')
    elif select == 5:
        print('CHỨC NĂNG SỐ 5')
        print('Bạn có chắc muốn xóa tất cả từ trong từ điển không?')
        enter_decision = input('Nhập yes / no: ').lower()

        if enter_decision == 'yes':
            dictionary.clear()
            print('Đã xóa tất cả từ vựng!')
        elif enter_decision == 'no':
            print('Quay lại chương trình!')
        else:
            print('Vui lòng nhập lại giá trị!')
    elif select == 6:
        print('CHỨC NĂNG SỐ 6')
        if not dictionary:
            print('Chưa có danh sách!')
        else:
            print('--- Danh sách từ vựng ---')
            for i, vocab in enumerate(dictionary, start=1):
                print(f'{i}. {vocab}')
    elif select == 7:
        print('CHỨC NĂNG SỐ 7')
        if not dictionary:
            print('Chưa có danh sách!')
        else:
            print('--- Danh sách từ trong từ điển ---')
            for i, (vocab, mean) in enumerate(dictionary.items(), start=1):
                print(f'{i}. {vocab}: {mean}')
    elif select == 8:
        print('Kết thúc chương trình')
        break
    else:
        print('=> Vui lòng nhập chức năng có trong chương trình!')