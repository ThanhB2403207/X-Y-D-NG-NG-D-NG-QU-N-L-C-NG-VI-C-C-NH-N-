from kiem_tra import nhap_trang_thai, nhap_muc_do_uu_tien, nhap_ngay
from hien_thi import hien_thi_bang

def tim_theo_ten(danh_sach_cv, tu_khoa):
    """Tim cong viec co ten CHUA tu khoa, khong phan biet chu hoa/thuong"""
    ket_qua = []
    for cv in danh_sach_cv:
        if tu_khoa.lower() in cv["ten"].lower():
            ket_qua.append(cv)
    return ket_qua


def tim_theo_trang_thai(danh_sach_cv, trang_thai):
    """Tim cong viec theo trang thai, khong phan biet chu hoa/thuong"""
    ket_qua = []
    for cv in danh_sach_cv:
        if cv["trang_thai"].lower() == trang_thai.lower():
            ket_qua.append(cv)
    return ket_qua


def tim_theo_uu_tien(danh_sach_cv, muc_do_uu_tien):
    """Tim cong viec theo muc do uu tien, khong phan biet chu hoa/thuong"""
    ket_qua = []
    for cv in danh_sach_cv:
        if cv["muc_do_uu_tien"].lower() == muc_do_uu_tien.lower():
            ket_qua.append(cv)
    return ket_qua


def tim_theo_han_hoan_thanh(danh_sach_cv, ngay_can_tim):
    """Tim cong viec co han hoan thanh dung bang ngay nguoi dung nhap"""
    ket_qua = []
    for cv in danh_sach_cv:
        if cv["han_hoan_thanh"] == ngay_can_tim:
            ket_qua.append(cv)
    return ket_qua


def tim_kiem(danh_sach_cv):
    """Menu con cho chuc nang tim kiem"""
    while True:
        print("\n----- MENU TIM KIEM -----")
        print("1. Tim theo ten cong viec")
        print("2. Tim theo trang thai")
        print("3. Tim theo muc do uu tien")
        print("4. Tim theo han hoan thanh")
        print("5. Quay lai")
        lua_chon = input("Lua chon: ").strip()

        if lua_chon == "1":
            tu_khoa = input("Nhap ten cong viec can tim: ").strip()
            ket_qua = tim_theo_ten(danh_sach_cv, tu_khoa)
            if len(ket_qua) == 0:
                print(">> Khong tim thay cong viec phu hop.")
            else:
                hien_thi_bang(ket_qua)

        elif lua_chon == "2":
            trang_thai = nhap_trang_thai("Chon trang thai can tim: ")
            ket_qua = tim_theo_trang_thai(danh_sach_cv, trang_thai)
            if len(ket_qua) == 0:
                print(">> Khong tim thay cong viec phu hop.")
            else:
                hien_thi_bang(ket_qua)

        elif lua_chon == "3":
            muc_do = nhap_muc_do_uu_tien("Chon muc do uu tien can tim: ")
            ket_qua = tim_theo_uu_tien(danh_sach_cv, muc_do)
            if len(ket_qua) == 0:
                print(">> Khong tim thay cong viec phu hop.")
            else:
                hien_thi_bang(ket_qua)

        elif lua_chon == "4":
            ngay_can_tim = nhap_ngay("Nhap han hoan thanh can tim (dd/mm/yyyy): ")
            ket_qua = tim_theo_han_hoan_thanh(danh_sach_cv, ngay_can_tim)
            if len(ket_qua) == 0:
                print(">> Khong tim thay cong viec phu hop.")
            else:
                hien_thi_bang(ket_qua)

        elif lua_chon == "5":
            break
        else:
            print(">> Lua chon khong hop le. Vui long chon lai.")

