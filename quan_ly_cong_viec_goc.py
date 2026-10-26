"""
=====================================================================
    CHUONG TRINH QUAN LY CONG VIEC CA NHAN
    De tai so 29
    Ngon ngu: Python 3
    Muc dich: Bai tap lon mon lap trinh Python
=====================================================================
"""

# =====================================================================
# 1. IMPORT THU VIEN
# =====================================================================
import os
from datetime import datetime, date


# =====================================================================
# 2. KHAI BAO HANG SO
# =====================================================================
TEN_FILE = "congviec.txt"       # ten file du lieu mac dinh
DINH_DANG_NGAY = "%d/%m/%Y"     # dinh dang ngay: dd/mm/yyyy
KY_TU_PHAN_CACH = "|"           # ky tu phan cach trong file txt

DANH_SACH_UU_TIEN = ["Thap", "Trung binh", "Cao"]
DANH_SACH_TRANG_THAI = ["Chua bat dau", "Dang thuc hien", "Hoan thanh"]

# Dung de sap xep muc do uu tien theo thu tu logic (khong phai theo bang chu cai)
THU_TU_UU_TIEN = {"Thap": 1, "Trung binh": 2, "Cao": 3}


# =====================================================================
# 3. CAC HAM KIEM TRA DU LIEU (VALIDATION)
# =====================================================================
def chuoi_rong(chuoi):
    """Kiem tra 1 chuoi co rong (hoac chi toan khoang trang) hay khong"""
    return chuoi is None or chuoi.strip() == ""


def chuyen_doi_ngay(chuoi_ngay):
    """
    Chuyen chuoi dang dd/mm/yyyy thanh doi tuong date.
    Neu sai dinh dang hoac ngay khong ton tai -> tra ve None
    """
    try:
        ngay = datetime.strptime(chuoi_ngay.strip(), DINH_DANG_NGAY).date()
        return ngay
    except (ValueError, AttributeError):
        return None


def ma_cong_viec_da_ton_tai(danh_sach_cv, ma, ma_bo_qua=None):
    """
    Kiem tra ma cong viec da co trong danh sach chua.
    ma_bo_qua: dung khi cap nhat, bo qua chinh ban ghi dang sua
    """
    for cv in danh_sach_cv:
        if cv["ma"].lower() == ma.lower():
            if ma_bo_qua is not None and cv["ma"].lower() == ma_bo_qua.lower():
                continue
            return True
    return False


# =====================================================================
# 4. CAC HAM NHAP DU LIEU (NHAP CO KIEM TRA, KHONG LAM CRASH CHUONG TRINH)
# =====================================================================
def nhap_chuoi_khong_rong(nhan):
    """Nhap 1 chuoi, bat buoc khong duoc de trong"""
    while True:
        gia_tri = input(nhan)
        if chuoi_rong(gia_tri):
            print(">> Loi: Thong tin nay khong duoc de trong. Vui long nhap lai.")
        else:
            return gia_tri.strip()


def nhap_chuoi_co_the_giu_nguyen(nhan, gia_tri_cu):
    """Dung khi cap nhat: Enter thi giu nguyen gia tri cu, nhap gi do thi khong duoc rong"""
    while True:
        gia_tri = input(nhan + " (Enter de giu nguyen: '" + str(gia_tri_cu) + "'): ")
        if gia_tri.strip() == "":
            return gia_tri_cu
        if chuoi_rong(gia_tri):
            print(">> Loi: Thong tin khong duoc de trong. Vui long nhap lai.")
        else:
            return gia_tri.strip()


def nhap_chuoi_tuy_chon(nhan, gia_tri_cu=""):
    """Nhap chuoi khong bat buoc (VD: ghi chu). Enter -> giu nguyen / de trong."""
    gia_tri = input(nhan + " (Enter de bo qua, gia tri hien tai: '" + str(gia_tri_cu) + "'): ")
    if gia_tri.strip() == "":
        return gia_tri_cu
    return gia_tri.strip()


def nhap_ngay(nhan):
    """Nhap ngay dung dinh dang dd/mm/yyyy, khong cho ngay khong hop le"""
    while True:
        chuoi = input(nhan)
        if chuoi_rong(chuoi):
            print(">> Loi: Ngay khong duoc de trong. Vui long nhap lai.")
            continue
        ngay = chuyen_doi_ngay(chuoi)
        if ngay is None:
            print(">> Loi: Ngay khong hop le (dung dinh dang dd/mm/yyyy). Vui long nhap lai.")
        else:
            return ngay


def nhap_ngay_co_the_giu_nguyen(nhan, ngay_cu):
    """Nhap ngay khi cap nhat, Enter de giu nguyen"""
    while True:
        chuoi = input(nhan + " (Enter de giu nguyen: " + ngay_cu.strftime(DINH_DANG_NGAY) + "): ")
        if chuoi.strip() == "":
            return ngay_cu
        ngay = chuyen_doi_ngay(chuoi)
        if ngay is None:
            print(">> Loi: Ngay khong hop le (dung dinh dang dd/mm/yyyy). Vui long nhap lai.")
        else:
            return ngay


def nhap_muc_do_uu_tien(nhan):
    """Cho nguoi dung chon muc do uu tien tu danh sach co san (tranh nhap sai/typo)"""
    while True:
        print(nhan.rstrip(": ") + ":")
        for i in range(len(DANH_SACH_UU_TIEN)):
            print("  " + str(i + 1) + ". " + DANH_SACH_UU_TIEN[i])
        chuoi = input("Chon so (1-" + str(len(DANH_SACH_UU_TIEN)) + "): ")
        try:
            so = int(chuoi)
            if 1 <= so <= len(DANH_SACH_UU_TIEN):
                return DANH_SACH_UU_TIEN[so - 1]
            else:
                print(">> Loi: Vui long chon so trong khoang cho phep.")
        except ValueError:
            print(">> Loi: Vui long nhap dung dinh dang so nguyen.")


def nhap_muc_do_uu_tien_giu_nguyen(gia_tri_cu):
    """Chon lai muc do uu tien khi cap nhat, nhan 0 de giu nguyen"""
    while True:
        print("Muc do uu tien (dang la: " + gia_tri_cu + "):")
        for i in range(len(DANH_SACH_UU_TIEN)):
            print("  " + str(i + 1) + ". " + DANH_SACH_UU_TIEN[i])
        print("  0. Giu nguyen")
        chuoi = input("Chon so: ")
        try:
            so = int(chuoi)
            if so == 0:
                return gia_tri_cu
            if 1 <= so <= len(DANH_SACH_UU_TIEN):
                return DANH_SACH_UU_TIEN[so - 1]
            print(">> Loi: Vui long chon so trong khoang cho phep.")
        except ValueError:
            print(">> Loi: Vui long nhap dung dinh dang so nguyen.")


def nhap_trang_thai(nhan):
    """Cho nguoi dung chon trang thai tu danh sach co san"""
    while True:
        print(nhan.rstrip(": ") + ":")
        for i in range(len(DANH_SACH_TRANG_THAI)):
            print("  " + str(i + 1) + ". " + DANH_SACH_TRANG_THAI[i])
        chuoi = input("Chon so (1-" + str(len(DANH_SACH_TRANG_THAI)) + "): ")
        try:
            so = int(chuoi)
            if 1 <= so <= len(DANH_SACH_TRANG_THAI):
                return DANH_SACH_TRANG_THAI[so - 1]
            else:
                print(">> Loi: Vui long chon so trong khoang cho phep.")
        except ValueError:
            print(">> Loi: Vui long nhap dung dinh dang so nguyen.")


def nhap_trang_thai_giu_nguyen(gia_tri_cu):
    """Chon lai trang thai khi cap nhat, nhan 0 de giu nguyen"""
    while True:
        print("Trang thai (dang la: " + gia_tri_cu + "):")
        for i in range(len(DANH_SACH_TRANG_THAI)):
            print("  " + str(i + 1) + ". " + DANH_SACH_TRANG_THAI[i])
        print("  0. Giu nguyen")
        chuoi = input("Chon so: ")
        try:
            so = int(chuoi)
            if so == 0:
                return gia_tri_cu
            if 1 <= so <= len(DANH_SACH_TRANG_THAI):
                return DANH_SACH_TRANG_THAI[so - 1]
            print(">> Loi: Vui long chon so trong khoang cho phep.")
        except ValueError:
            print(">> Loi: Vui long nhap dung dinh dang so nguyen.")


def nhap_phan_tram_hoan_thanh(nhan):
    """Nhap phan tram hoan thanh, bat buoc trong khoang 0-100"""
    while True:
        chuoi = input(nhan)
        try:
            so = int(chuoi)
            if so < 0 or so > 100:
                print(">> Loi: Phan tram hoan thanh phai trong khoang 0-100. Vui long nhap lai.")
                continue
            return so
        except ValueError:
            print(">> Loi: Vui long nhap dung dinh dang so nguyen. Vui long nhap lai.")


def nhap_phan_tram_hoan_thanh_giu_nguyen(nhan, gia_tri_cu):
    """Nhap phan tram hoan thanh khi cap nhat, Enter de giu nguyen"""
    while True:
        chuoi = input(nhan + " (Enter de giu nguyen: " + str(gia_tri_cu) + "): ")
        if chuoi.strip() == "":
            return gia_tri_cu
        try:
            so = int(chuoi)
            if so < 0 or so > 100:
                print(">> Loi: Phan tram hoan thanh phai trong khoang 0-100. Vui long nhap lai.")
                continue
            return so
        except ValueError:
            print(">> Loi: Vui long nhap dung dinh dang so nguyen. Vui long nhap lai.")


def dong_y(nhan):
    """Nhan cau tra loi Y/N cua nguoi dung"""
    while True:
        chuoi = input(nhan).strip().lower()
        if chuoi == "y":
            return True
        elif chuoi == "n":
            return False
        else:
            print(">> Vui long nhap Y hoac N.")


# =====================================================================
# 5. CAC HAM HIEN THI
# =====================================================================
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


# =====================================================================
# 6. CAC HAM QUAN LY (THEM / CAP NHAT / XOA)
# =====================================================================
def them_cong_viec(danh_sach_cv):
    """Them 1 cong viec moi vao danh sach, co kiem tra du lieu day du"""
    print("\n===== THEM CONG VIEC MOI =====")

    while True:
        ma = nhap_chuoi_khong_rong("Ma cong viec: ")
        if ma_cong_viec_da_ton_tai(danh_sach_cv, ma):
            print(">> Loi: Ma cong viec '" + ma + "' da ton tai. Vui long nhap ma khac.")
        else:
            break

    ten = nhap_chuoi_khong_rong("Ten cong viec: ")
    mo_ta = nhap_chuoi_khong_rong("Mo ta: ")

    ngay_bat_dau = nhap_ngay("Ngay bat dau (dd/mm/yyyy): ")

    # Han hoan thanh bat buoc phai sau hoac bang ngay bat dau
    while True:
        han_hoan_thanh = nhap_ngay("Han hoan thanh (dd/mm/yyyy): ")
        if han_hoan_thanh < ngay_bat_dau:
            print(">> Loi: Han hoan thanh phai sau hoac bang ngay bat dau. Vui long nhap lai.")
        else:
            break

    muc_do_uu_tien = nhap_muc_do_uu_tien("Muc do uu tien: ")
    trang_thai = nhap_trang_thai("Trang thai: ")

    # Neu chon trang thai da Hoan thanh, ep phan tram hoan thanh = 100 (logic nghiep vu)
    if trang_thai == "Hoan thanh":
        print(">> Trang thai la 'Hoan thanh' nen phan tram hoan thanh se tu dong la 100%.")
        phan_tram = 100
    else:
        phan_tram = nhap_phan_tram_hoan_thanh("Phan tram hoan thanh (0-100): ")

    ghi_chu = nhap_chuoi_tuy_chon("Ghi chu: ")

    cong_viec_moi = {
        "ma": ma,
        "ten": ten,
        "mo_ta": mo_ta,
        "ngay_bat_dau": ngay_bat_dau,
        "han_hoan_thanh": han_hoan_thanh,
        "muc_do_uu_tien": muc_do_uu_tien,
        "trang_thai": trang_thai,
        "phan_tram": phan_tram,
        "ghi_chu": ghi_chu
    }

    danh_sach_cv.append(cong_viec_moi)
    print(">> Them cong viec thanh cong!")


def tim_theo_ma(danh_sach_cv, ma):
    """Tim va tra ve 1 cong viec theo ma (tra ve None neu khong co)"""
    for cv in danh_sach_cv:
        if cv["ma"].lower() == ma.lower():
            return cv
    return None


def cap_nhat_cong_viec(danh_sach_cv):
    """Cap nhat thong tin 1 cong viec theo ma"""
    print("\n===== CAP NHAT CONG VIEC =====")
    ma = nhap_chuoi_khong_rong("Nhap ma cong viec can cap nhat: ")
    cv = tim_theo_ma(danh_sach_cv, ma)

    if cv is None:
        print(">> Khong tim thay cong viec co ma '" + ma + "'.")
        return

    print(">> Da tim thay cong viec. Nhan Enter neu muon giu nguyen gia tri cu.")
    hien_thi_chi_tiet(cv)

    # Ma cong viec: cho phep giu nguyen, neu doi thi khong duoc trung
    while True:
        ma_moi = input("Ma cong viec (Enter de giu nguyen: '" + cv["ma"] + "'): ").strip()
        if ma_moi == "":
            ma_moi = cv["ma"]
            break
        if ma_cong_viec_da_ton_tai(danh_sach_cv, ma_moi, ma_bo_qua=cv["ma"]):
            print(">> Loi: Ma cong viec '" + ma_moi + "' da ton tai cho cong viec khac. Vui long nhap lai.")
        else:
            break

    ten_moi = nhap_chuoi_co_the_giu_nguyen("Ten cong viec", cv["ten"])
    mo_ta_moi = nhap_chuoi_co_the_giu_nguyen("Mo ta", cv["mo_ta"])

    ngay_bat_dau_moi = nhap_ngay_co_the_giu_nguyen("Ngay bat dau", cv["ngay_bat_dau"])

    while True:
        han_hoan_thanh_moi = nhap_ngay_co_the_giu_nguyen("Han hoan thanh", cv["han_hoan_thanh"])
        if han_hoan_thanh_moi < ngay_bat_dau_moi:
            print(">> Loi: Han hoan thanh phai sau hoac bang ngay bat dau. Vui long nhap lai.")
        else:
            break

    muc_do_uu_tien_moi = nhap_muc_do_uu_tien_giu_nguyen(cv["muc_do_uu_tien"])
    trang_thai_moi = nhap_trang_thai_giu_nguyen(cv["trang_thai"])

    if trang_thai_moi == "Hoan thanh":
        print(">> Trang thai la 'Hoan thanh' nen phan tram hoan thanh se tu dong la 100%.")
        phan_tram_moi = 100
    else:
        phan_tram_moi = nhap_phan_tram_hoan_thanh_giu_nguyen("Phan tram hoan thanh (0-100)", cv["phan_tram"])

    ghi_chu_moi = nhap_chuoi_tuy_chon("Ghi chu", cv["ghi_chu"])

    cv["ma"] = ma_moi
    cv["ten"] = ten_moi
    cv["mo_ta"] = mo_ta_moi
    cv["ngay_bat_dau"] = ngay_bat_dau_moi
    cv["han_hoan_thanh"] = han_hoan_thanh_moi
    cv["muc_do_uu_tien"] = muc_do_uu_tien_moi
    cv["trang_thai"] = trang_thai_moi
    cv["phan_tram"] = phan_tram_moi
    cv["ghi_chu"] = ghi_chu_moi

    print(">> Cap nhat cong viec thanh cong!")


def xoa_cong_viec(danh_sach_cv):
    """Xoa 1 cong viec theo ma, co xac nhan truoc khi xoa"""
    print("\n===== XOA CONG VIEC =====")
    ma = nhap_chuoi_khong_rong("Nhap ma cong viec can xoa: ")
    cv = tim_theo_ma(danh_sach_cv, ma)

    if cv is None:
        print(">> Khong tim thay cong viec can xoa.")
        return

    print("Thong tin cong viec:")
    hien_thi_chi_tiet(cv)

    if dong_y("Ban co chac chan muon xoa? (Y/N): "):
        danh_sach_cv.remove(cv)
        print(">> Xoa cong viec thanh cong!")
    else:
        print(">> Da huy thao tac xoa.")


# =====================================================================
# 7. CAC HAM TIM KIEM
# =====================================================================
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


# =====================================================================
# 8. CAC HAM SAP XEP
# =====================================================================
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


# =====================================================================
# 9. CAC HAM TINH TOAN VA THONG KE
# =====================================================================
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


# =====================================================================
# 10. CAC HAM DOC / GHI FILE TXT
# =====================================================================
def luu_file(danh_sach_cv, ten_file=TEN_FILE):
    """Ghi toan bo danh sach cong viec xuong file TXT, moi cong viec 1 dong"""
    try:
        file = open(ten_file, "w", encoding="utf-8")
        for cv in danh_sach_cv:
            dong = KY_TU_PHAN_CACH.join([
                cv["ma"],
                cv["ten"],
                cv["mo_ta"],
                cv["ngay_bat_dau"].strftime(DINH_DANG_NGAY),
                cv["han_hoan_thanh"].strftime(DINH_DANG_NGAY),
                cv["muc_do_uu_tien"],
                cv["trang_thai"],
                str(cv["phan_tram"]),
                cv["ghi_chu"]
            ])
            file.write(dong + "\n")
        file.close()
        print(">> Luu du lieu thanh cong.")
    except Exception as loi:
        print(">> Khong the ghi file. Chi tiet loi: " + str(loi))


def doc_file(ten_file=TEN_FILE):
    """
    Doc du lieu cong viec tu file TXT, chuyen doi dung kieu du lieu.
    Tra ve danh sach cong viec (list). Neu file khong ton tai tra ve list rong.
    """
    danh_sach_cv = []
    try:
        file = open(ten_file, "r", encoding="utf-8")
        so_dong_loi = 0

        for dong in file:
            dong = dong.strip("\n")
            if dong.strip() == "":
                continue

            phan = dong.split(KY_TU_PHAN_CACH)
            if len(phan) != 9:
                so_dong_loi += 1
                continue

            try:
                cv = {
                    "ma": phan[0],
                    "ten": phan[1],
                    "mo_ta": phan[2],
                    "ngay_bat_dau": datetime.strptime(phan[3], DINH_DANG_NGAY).date(),
                    "han_hoan_thanh": datetime.strptime(phan[4], DINH_DANG_NGAY).date(),
                    "muc_do_uu_tien": phan[5],
                    "trang_thai": phan[6],
                    "phan_tram": int(phan[7]),
                    "ghi_chu": phan[8]
                }
                danh_sach_cv.append(cv)
            except ValueError:
                so_dong_loi += 1
                continue

        file.close()

        if so_dong_loi > 0:
            print(">> Canh bao: co " + str(so_dong_loi) + " dong du lieu bi loi va da bi bo qua.")

        print(">> Doc du lieu thanh cong. Tong so ban ghi: " + str(len(danh_sach_cv)))
        return danh_sach_cv

    except FileNotFoundError:
        print(">> File du lieu chua ton tai.")
        return danh_sach_cv
    except Exception as loi:
        print(">> Khong the doc file. Chi tiet loi: " + str(loi))
        return danh_sach_cv


# =====================================================================
# 11. MENU
# =====================================================================
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


# =====================================================================
# 12. HAM MAIN
# =====================================================================
def main():
    """Ham chinh cua chuong trinh: khoi tao du lieu va chay menu"""
    danh_sach_cv = []

    if os.path.exists(TEN_FILE):
        danh_sach_cv = doc_file()
    else:
        print(">> File du lieu chua ton tai. Chuong trinh se bat dau voi danh sach rong.")

    menu(danh_sach_cv)


# =====================================================================
# 13. DIEM BAT DAU CHUONG TRINH
# =====================================================================
if __name__ == "__main__":
    main()
