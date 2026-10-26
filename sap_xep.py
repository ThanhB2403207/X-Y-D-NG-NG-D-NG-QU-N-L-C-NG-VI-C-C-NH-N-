from cau_hinh import THU_TU_UU_TIEN
from hien_thi import hien_thi_bang

def hoi_tang_giam():
    """Hoi nguoi dung muon sap xep tang dan hay giam dan"""
    while True:
        print("1. Tang dan")
        print("2. Giam dan")
        print("3. Quay lai")
        lua_chon = input("Lua chon: ").strip()
        if lua_chon in ("1", "2", "3"):
            return lua_chon
        print(">> Lua chon khong hop le.")


def sap_xep_theo_han(danh_sach_cv):
    """Sap xep danh sach cong viec theo han hoan thanh"""
    print("\n----- SAP XEP THEO HAN HOAN THANH -----")
    if len(danh_sach_cv) == 0:
        print("Danh sach cong viec dang trong.")
        return
    lua_chon = hoi_tang_giam()
    if lua_chon == "3":
        return
    dao_nguoc = (lua_chon == "2")
    ket_qua = sorted(danh_sach_cv, key=lambda cv: cv["han_hoan_thanh"], reverse=dao_nguoc)
    hien_thi_bang(ket_qua)


def sap_xep_theo_uu_tien(danh_sach_cv):
    """Sap xep danh sach cong viec theo muc do uu tien (Thap < Trung binh < Cao)"""
    print("\n----- SAP XEP THEO MUC DO UU TIEN -----")
    if len(danh_sach_cv) == 0:
        print("Danh sach cong viec dang trong.")
        return
    lua_chon = hoi_tang_giam()
    if lua_chon == "3":
        return
    dao_nguoc = (lua_chon == "2")
    ket_qua = sorted(danh_sach_cv, key=lambda cv: THU_TU_UU_TIEN[cv["muc_do_uu_tien"]], reverse=dao_nguoc)
    hien_thi_bang(ket_qua)


def sap_xep_theo_phan_tram(danh_sach_cv):
    """Sap xep danh sach cong viec theo phan tram hoan thanh"""
    print("\n----- SAP XEP THEO PHAN TRAM HOAN THANH -----")
    if len(danh_sach_cv) == 0:
        print("Danh sach cong viec dang trong.")
        return
    lua_chon = hoi_tang_giam()
    if lua_chon == "3":
        return
    dao_nguoc = (lua_chon == "2")
    ket_qua = sorted(danh_sach_cv, key=lambda cv: cv["phan_tram"], reverse=dao_nguoc)
    hien_thi_bang(ket_qua)


def menu_sap_xep(danh_sach_cv):
    """Menu con cho chuc nang sap xep"""
    while True:
        print("\n----- MENU SAP XEP -----")
        print("1. Theo han hoan thanh")
        print("2. Theo muc do uu tien")
        print("3. Theo phan tram hoan thanh")
        print("4. Quay lai")
        lua_chon = input("Lua chon: ").strip()

        if lua_chon == "1":
            sap_xep_theo_han(danh_sach_cv)
        elif lua_chon == "2":
            sap_xep_theo_uu_tien(danh_sach_cv)
        elif lua_chon == "3":
            sap_xep_theo_phan_tram(danh_sach_cv)
        elif lua_chon == "4":
            break
        else:
            print(">> Lua chon khong hop le. Vui long chon lai.")

