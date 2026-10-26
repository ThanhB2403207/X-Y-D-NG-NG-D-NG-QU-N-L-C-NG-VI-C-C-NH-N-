from datetime import date
from cau_hinh import DANH_SACH_TRANG_THAI
from tim_kiem import tim_theo_trang_thai, tim_theo_uu_tien
from hien_thi import hien_thi_bang

def ty_le_hoan_thanh(danh_sach_cv):
    """Tinh va in ty le % so cong viec co trang thai Hoan thanh tren tong so cong viec"""
    print("\n===== TY LE HOAN THANH =====")
    if len(danh_sach_cv) == 0:
        print("Danh sach cong viec dang trong.")
        return

    so_hoan_thanh = 0
    for cv in danh_sach_cv:
        if cv["trang_thai"] == "Hoan thanh":
            so_hoan_thanh += 1

    ty_le = so_hoan_thanh / len(danh_sach_cv) * 100
    print("So cong viec hoan thanh: " + str(so_hoan_thanh) + "/" + str(len(danh_sach_cv)))
    print("Ty le hoan thanh: " + format(ty_le, ".2f") + "%")


def thong_ke_hoan_thanh_chua_hoan_thanh(danh_sach_cv):
    """Dem so cong viec da Hoan thanh va chua Hoan thanh"""
    print("\n===== SO CONG VIEC HOAN THANH / CHUA HOAN THANH =====")
    if len(danh_sach_cv) == 0:
        print("Danh sach cong viec dang trong.")
        return

    so_hoan_thanh = 0
    so_chua_hoan_thanh = 0
    for cv in danh_sach_cv:
        if cv["trang_thai"] == "Hoan thanh":
            so_hoan_thanh += 1
        else:
            so_chua_hoan_thanh += 1

    print("Da hoan thanh    : " + str(so_hoan_thanh))
    print("Chua hoan thanh  : " + str(so_chua_hoan_thanh))


def thong_ke_qua_han(danh_sach_cv):
    """Liet ke cong viec da qua han hoan thanh nhung van chua Hoan thanh"""
    print("\n===== CONG VIEC QUA HAN =====")
    if len(danh_sach_cv) == 0:
        print("Danh sach cong viec dang trong.")
        return

    hom_nay = date.today()
    ket_qua = []
    for cv in danh_sach_cv:
        if cv["han_hoan_thanh"] < hom_nay and cv["trang_thai"] != "Hoan thanh":
            ket_qua.append(cv)

    if len(ket_qua) == 0:
        print(">> Khong co cong viec nao qua han.")
        return

    print(">> Danh sach cong viec da qua han (chua hoan thanh):")
    for cv in ket_qua:
        so_ngay_qua_han = (hom_nay - cv["han_hoan_thanh"]).days
        print(cv["ma"] + " - " + cv["ten"] + " | Han HT: " +
              cv["han_hoan_thanh"].strftime(DINH_DANG_NGAY) +
              " | Da qua han " + str(so_ngay_qua_han) + " ngay" +
              " | Trang thai: " + cv["trang_thai"])


def thong_ke_uu_tien_cao(danh_sach_cv):
    """Liet ke cong viec co muc do uu tien Cao"""
    print("\n===== CONG VIEC UU TIEN CAO =====")
    if len(danh_sach_cv) == 0:
        print("Danh sach cong viec dang trong.")
        return

    ket_qua = tim_theo_uu_tien(danh_sach_cv, "Cao")
    if len(ket_qua) == 0:
        print(">> Khong co cong viec nao co muc do uu tien Cao.")
    else:
        hien_thi_bang(ket_qua)


def thong_ke_theo_trang_thai(danh_sach_cv):
    """Dem so luong cong viec theo tung trang thai"""
    print("\n===== SO CONG VIEC THEO TRANG THAI =====")
    if len(danh_sach_cv) == 0:
        print("Danh sach cong viec dang trong.")
        return

    for trang_thai in DANH_SACH_TRANG_THAI:
        so_luong = len(tim_theo_trang_thai(danh_sach_cv, trang_thai))
        print(trang_thai + ": " + str(so_luong) + " cong viec")


def menu_thong_ke(danh_sach_cv):
    """Menu con cho chuc nang tinh toan / thong ke"""
    while True:
        print("\n----- MENU TINH TOAN / THONG KE -----")
        print("1. Ty le hoan thanh")
        print("2. So cong viec hoan thanh/chua hoan thanh")
        print("3. Cong viec qua han")
        print("4. Cong viec uu tien cao")
        print("5. So cong viec theo trang thai")
        print("6. Quay lai")
        lua_chon = input("Lua chon: ").strip()

        if lua_chon == "1":
            ty_le_hoan_thanh(danh_sach_cv)
        elif lua_chon == "2":
            thong_ke_hoan_thanh_chua_hoan_thanh(danh_sach_cv)
        elif lua_chon == "3":
            thong_ke_qua_han(danh_sach_cv)
        elif lua_chon == "4":
            thong_ke_uu_tien_cao(danh_sach_cv)
        elif lua_chon == "5":
            thong_ke_theo_trang_thai(danh_sach_cv)
        elif lua_chon == "6":
            break
        else:
            print(">> Lua chon khong hop le. Vui long chon lai.")

