from datetime import datetime
from cau_hinh import TEN_FILE, DINH_DANG_NGAY, KY_TU_PHAN_CACH

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

