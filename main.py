"""
File: main.py
Chức năng: File CHẠY CHÍNH của chương trình.
Chỉ chứa: hiển thị menu, nhận lựa chọn của người dùng, và GỌI các hàm xử lý
nghiệp vụ trong task_functions.py / file_handler.py.
Không xử lý logic nghiệp vụ trực tiếp ở đây -> giúp code rõ ràng, dễ bảo trì.
"""
import os
from cau_hinh import TEN_FILE
from file_manager import doc_file, luu_file
from quan_ly_cong_viec import them_cong_viec, cap_nhat_cong_viec, xoa_cong_viec
from hien_thi import hien_thi_danh_sach
from tim_kiem import tim_kiem
from sap_xep import menu_sap_xep
from thong_ke import menu_thong_ke

def hien_thi_menu_chinh():
    """In ra menu chinh cua chuong trinh"""
    print("\n" + "=" * 45)
    print("     QUAN LY CONG VIEC CA NHAN")
    print("=" * 45)
    print("1. Them")
    print("2. Hien thi danh sach")
    print("3. Cap nhat")
    print("4. Xoa")
    print("5. Tim kiem")
    print("6. Sap xep")
    print("7. Tinh toan/Thong ke")
    print("8. Luu du lieu")
    print("9. Doc du lieu")
    print("0. Thoat")
    print("=" * 45)


def menu(danh_sach_cv):
    """Vong lap chinh dieu huong chuong trinh theo lua chon cua nguoi dung"""
    while True:
        hien_thi_menu_chinh()
        lua_chon = input("Lua chon: ").strip()

        if lua_chon == "1":
            them_cong_viec(danh_sach_cv)
        elif lua_chon == "2":
            hien_thi_danh_sach(danh_sach_cv)
        elif lua_chon == "3":
            cap_nhat_cong_viec(danh_sach_cv)
        elif lua_chon == "4":
            xoa_cong_viec(danh_sach_cv)
        elif lua_chon == "5":
            tim_kiem(danh_sach_cv)
        elif lua_chon == "6":
            menu_sap_xep(danh_sach_cv)
        elif lua_chon == "7":
            menu_thong_ke(danh_sach_cv)
        elif lua_chon == "8":
            luu_file(danh_sach_cv)
        elif lua_chon == "9":
            danh_sach_moi = doc_file()
            if len(danh_sach_moi) > 0:
                danh_sach_cv.clear()
                danh_sach_cv.extend(danh_sach_moi)
        elif lua_chon == "0":
            print("Cam on ban da su dung chuong trinh. Tam biet!")
            break
        else:
            print(">> Lua chon khong hop le. Vui long chon lai.")


def main():
    """Ham chinh cua chuong trinh: khoi tao du lieu va chay menu"""
    danh_sach_cv = []

    if os.path.exists(TEN_FILE):
        danh_sach_cv = doc_file()
    else:
        print(">> File du lieu chua ton tai. Chuong trinh se bat dau voi danh sach rong.")

    menu(danh_sach_cv)



if __name__ == "__main__":
    main()
