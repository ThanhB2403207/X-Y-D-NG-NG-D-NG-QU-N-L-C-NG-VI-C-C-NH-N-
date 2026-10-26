from datetime import datetime
from cau_hinh import DINH_DANG_NGAY, DANH_SACH_UU_TIEN, DANH_SACH_TRANG_THAI

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

