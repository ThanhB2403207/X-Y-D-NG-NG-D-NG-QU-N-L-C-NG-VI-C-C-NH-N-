from kiem_tra import *
from hien_thi import hien_thi_chi_tiet

def tim_theo_ma(danh_sach_cv, ma):
    """Tim va tra ve 1 cong viec theo ma (tra ve None neu khong co)"""
    for cv in danh_sach_cv:
        if cv["ma"].lower() == ma.lower():
            return cv
    return None


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

