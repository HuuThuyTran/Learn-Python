# import random
import random

# Tạo set
thung_phieu = set()

# Tạo Chương trình bốc thăm trúng thưởng
while True:
    # Danh sách chức năng của chương trình
    print('----------- CHƯƠNG TRÌNH BỐC THĂM TRÚNG THƯỞNG -----------')
    print('Vui lòng chọn các chức năng bên dưới')
    print('1. Thêm một sđt bất kỳ vào thùng phiếu dự thưởng')
    print('2. Xóa một sđt từ thùng phiếu dự thưởng')
    print('3. Quay sđt ngẫu nhiên để lấy trúng thưởng')
    print('4. Thoát chương trình!')
    print(f'Thùng phiếu hiện tại: {thung_phieu}')

    # Khai báo biến lua_chon
    lua_chon = int(input('=> Nhập chức năng bạn muốn (1-4): '))

    # Xử lý khi người dùng khi nhập chức năng vào
    if lua_chon == 1:
        sdt = input('Nhập sđt của bạn vào thùng phiếu: ')
        thung_phieu.add(sdt)
    elif lua_chon == 2:
        sdt = input('Nhập sđt cần xóa: ')
        thung_phieu.discard(sdt)
    elif lua_chon == 3:
        danh_sach_sdt = list(thung_phieu)
        i = random.randint(0, len(thung_phieu) - 1)
        print(f'SĐT trúng thưởng ngẫu nhiên là: {danh_sach_sdt[i]}')
        thung_phieu.discard(danh_sach_sdt[i])
    else:
        print('Đã thoát khỏi chương trình!')
        break

    # Khai báo biến x để nhập giá trị bất kỳ
    x = input("Nhập phím bất kỳ để tiếp tục chạy chương trình: ")