# Mô tả chương trình quản lý môn học
# Chương trình quản lý môn học được thiết kế nhằm hỗ trợ người dùng thực hiện các thao tác cơ bản với danh sách môn học trong một hệ thống đào tạo.
# Mỗi môn học bao gồm các thông tin: mã môn học, tên môn học và số tín chỉ. Các chức năng chính của chương trình bao gồm:
# - Nhập danh sách môn học: Cho phép người dùng nhập vào nhiều môn học với đầy đủ thông tin
# - Hiển thị thông tin môn học: Xuất ra màn hình danh sách các môn học đã nhập
# - Thêm môn học: Bổ sung một môn học mới vào danh sách hiện có
# - Xoá môn học theo mã: Tìm và xoá môn học dựa trên mã môn học được cung cấp
# - Tìm kiếm môn học: Tìm kiếm thông tin môn học theo mã, tên hoặc số tín chỉ
# - Ghi vào tệp: Lưu danh sách môn học vào tệp văn bản có tên MonHoc.txt
# - Đọc từ tệp: Đọc dữ liệu môn học từ tệp MonHoc.txt để hiển thị hoặc xử lý tiếp

# Bài làm:
# Tạo class MonHoc
class MonHoc:
    # hàm khởi tạo
    def __init__(self, maMH, tenMH, soTinChi):
        self.maMH = maMH
        self.tenMH = tenMH
        self.soTinChi = soTinChi

    # hàm hiển thị thông tin môn học
    def hienThiMonHoc(self):
        print(f'Mã môn học: {self.maMH}')
        print(f'Tên môn học: {self.tenMH}')
        print(f'Số tín chỉ: {self.soTinChi}')

# Tạo danh sách môn học
danhSachMonHoc = []

# Hàm menu chương tình
def menu():
    print('===== MENU CHƯƠNG TRÌNH =====')
    print('1. Nhập danh sách môn học')
    print('2. Hiển thị thông tin môn học')
    print('3. Thêm môn học')
    print('4. Xóa môn học theo mã môn')
    print('5. Tìm kiếm môn học')
    print('6. Ghi vào tệp file: MonHoc.txt')
    print('7. Đọc từ tệp file: MonHoc.txt')
    print('8. Thoát chương trình')

# Hàm nhập danh sách môn học
def nhapDSMH():
    # Nhập số lượng môn học
    while True:
        try:
            n = int(input('Nhập số lượng môn học: '))
            if n <= 0:
                print('Số lượng phải > 0')
                continue
            break
        except ValueError:
            print('Phải nhập là số nguyên!')

    for i in range(n):
        # Nhập mã môn (không trùng)
        while True:
            maMH = input('Nhập mã môn học: ').strip()
            if any(mh.maMH == maMH for mh in danhSachMonHoc):
                print('Mã môn học bị trùng, nhập lại!')
            else:
                break

        tenMH = input('Nhập tên môn học: ').strip()

        # Kiểm tra nhập số tín chỉ có hợp lệ
        while True:
            try:
                soTC = int(input('Nhập số tín chỉ: '))
                if soTC <= 0:
                    print('Số tín chỉ phải > 0')
                break
            except ValueError:
                print('Số tín chỉ phải là số nguyên. Vui lòng nhập lại!')

        # Thêm môn học vào danh sách
        monHoc = MonHoc(maMH, tenMH, soTC)
        danhSachMonHoc.append(monHoc)
        print(f'=> Thêm môn học thứ {i+1} thành công!')

# Hàm in danh sách các môn học
def inDSMH():
    if not danhSachMonHoc:
        print('Chưa có danh sách môn học nào!')
        return

    # enumerate() là hàm built-in của Python
    # Dùng để lấy phần từ và lấy số thứ tự (index). Vị trí bắt đầu từ 0
    print('Danh sách các môn học:')
    for i, monHoc in enumerate(danhSachMonHoc, start=1):
        print(f'+) Thông tin môn học thứ {i}:')
        monHoc.hienThiMonHoc()

# Hàm thêm môn học
def themMH():
    print('Nhập các thông tin môn học cần thêm')

    # Kiểm tra trùng mã môn học
    while True:
        maMH = input('Nhập mã môn học: ')
        if any(mh.maMH == maMH for mh in danhSachMonHoc):
            print('Mã môn học bị trùng!')
            continue
        else:
            break

    tenMH = input('Nhập tên môn học: ')

    # Kiểm tra nhập số tín chỉ hợp lệ
    while True:
        try:
            soTC = int(input('Nhập số tín chỉ: '))
            if soTC <= 0:
                print('Số tín chỉ phải > 0!')
                continue
            break
        except ValueError:
            print('Số tín chỉ phải là số nguyên. Vui lòng nhập lại!')

    # Thêm môn học vào danh sách
    monHoc = MonHoc(maMH, tenMH, soTC)
    danhSachMonHoc.append(monHoc)
    print('Đã thêm một môn học thành công!')

# Hàm xóa môn học theo mã môn
def xoaMHTheoMa(maXoa):
    for monHoc in danhSachMonHoc:
        if maXoa == monHoc.maMH:
            danhSachMonHoc.remove(monHoc)
            print(f'Đã xoá mã {maXoa} thành công!')
            return
    print(f'Không tìm thấy mã môn học {maXoa}')

# Hàm tìm kiếm môn học
def timKiemThongTin(thongTin):
    found = False
    for monHoc in danhSachMonHoc:
        if (thongTin == monHoc.maMH or
            thongTin == monHoc.tenMH or
            thongTin == monHoc.soTinChi):
            print('---- Thông tin vừa tìm được ----')
            monHoc.hienThiMonHoc()
            found = True
    if not found:
        print('---- Không tìm thấy kết quả vừa tìm ----')

# Bắt đầu chương trình:
def main():
    while True:
        menu()
        try:
            lua_chon = int(input('=> Nhập lựa chọn chức năng trên: '))
        except ValueError:
            print('Vui lòng nhập số!')
            continue

        if lua_chon == 1:
            nhapDSMH()

        elif lua_chon == 2:
            inDSMH()

        elif lua_chon == 3:
            themMH()

        elif lua_chon == 4:
            maXoa = input('Nhập mã môn muốn xóa: ').strip().lower()
            xoaMHTheoMa(maXoa)

        elif lua_chon == 5:
            thongTin = input('Nhập thông tin muốn tìm: ').strip().lower()
            timKiemThongTin(thongTin)

        elif lua_chon == 6:
            print('Chức năng đang phát triển...')

        elif lua_chon == 7:
            print('Chức năng đang phát triển...')

        elif lua_chon == 8:
            print('Đã thoát khỏi chương trình!')
            break

        else:
            print('Lựa chọn không hợp lệ!')

if __name__ == '__main__':
    main()