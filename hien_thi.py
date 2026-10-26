from cau_hinh import DINH_DANG_NGAY

def hien_thi_dong_ke(cv):
    """In 1 dong thong tin cong viec theo dang bang"""
    print("{:<6}{:<20}{:<12}{:<12}{:<12}{:<16}{:>6}".format(
        cv["ma"],
        cv["ten"][:19],
        cv["ngay_bat_dau"].strftime(DINH_DANG_NGAY),
        cv["han_hoan_thanh"].strftime(DINH_DANG_NGAY),
        cv["muc_do_uu_tien"][:11],
        cv["trang_thai"][:15],
        str(cv["phan_tram"]) + "%"
    ))


def hien_thi_bang(danh_sach_cv):
    """Hien thi 1 danh sach cong viec (dung chung cho hien thi tat ca va ket qua tim kiem)"""
    if len(danh_sach_cv) == 0:
        print("Danh sach cong viec dang trong.")
        return
    print("-" * 100)
    print("{:<6}{:<20}{:<12}{:<12}{:<12}{:<16}{:>6}".format(
        "Ma", "Ten cong viec", "Bat dau", "Han HT", "Uu tien", "Trang thai", "PT HT"
    ))
    print("-" * 100)
    for cv in danh_sach_cv:
        hien_thi_dong_ke(cv)
    print("-" * 100)
    print("Tong so ban ghi:", len(danh_sach_cv))


def hien_thi_chi_tiet(cv):
    """Hien thi day du thong tin (bao gom mo ta, ghi chu) cua 1 cong viec"""
    print("-" * 60)
    print("Ma cong viec     : " + cv["ma"])
    print("Ten cong viec    : " + cv["ten"])
    print("Mo ta            : " + cv["mo_ta"])
    print("Ngay bat dau     : " + cv["ngay_bat_dau"].strftime(DINH_DANG_NGAY))
    print("Han hoan thanh   : " + cv["han_hoan_thanh"].strftime(DINH_DANG_NGAY))
    print("Muc do uu tien   : " + cv["muc_do_uu_tien"])
    print("Trang thai       : " + cv["trang_thai"])
    print("Phan tram HT     : " + str(cv["phan_tram"]) + "%")
    print("Ghi chu          : " + (cv["ghi_chu"] if cv["ghi_chu"] != "" else "(khong co)"))
    print("-" * 60)


def hien_thi_danh_sach(danh_sach_cv):
    """Hien thi toan bo danh sach cong viec hien co"""
    print("\n===== DANH SACH TOAN BO CONG VIEC =====")
    hien_thi_bang(danh_sach_cv)

