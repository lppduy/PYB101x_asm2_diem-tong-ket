def xeploai_hocsinh(diem_trungbinh_file):
    xeploai = {}
    
    # Đọc file điểm trung bình
    with open(diem_trungbinh_file, 'r') as file:
        lines = file.readlines()
        for line in lines[1:]:
            fields = line.strip().split(',')
            ma_hs = fields[0]
            dtb_chuan = (float(fields[1]) + float(fields[2]) + float(fields[5])) * 2.0 + \
                         (float(fields[3]) + float(fields[4]) + float(fields[6]) + float(fields[7]) + float(fields[8])) * 1.0
            dtb_chuan /= 11.0
            
            if dtb_chuan >= 9.0 and all(float(diem) >= 8.0 for diem in fields[1:]):
                xeploai[ma_hs] = "Xuat sac"
            elif dtb_chuan >= 8.0 and all(float(diem) >= 6.5 for diem in fields[1:]):
                xeploai[ma_hs] = "Gioi"
            elif dtb_chuan >= 6.5 and all(float(diem) >= 5.0 for diem in fields[1:]):
                xeploai[ma_hs] = "Kha"
            elif dtb_chuan >= 6.0 and all(float(diem) >= 4.5 for diem in fields[1:]):
                xeploai[ma_hs] = "TB kha"
            else:
                xeploai[ma_hs] = "TB"
    
    return xeploai


def xeploai_thidaihoc_hocsinh(diem_trungbinh_folder):
    xeploai_thidaihoc = {}
    
    # Đọc file điểm trung bình cho từng học sinh
    with open(diem_trungbinh_folder + "/diem_trungbinh.txt", 'r') as file:
        lines = file.readlines()
        for line in lines[1:]:
            fields = line.strip().split(',')
            ma_hs = fields[0]
            dtb_toan = float(fields[1])
            dtb_ly = float(fields[2])
            dtb_hoa = float(fields[3])
            dtb_anh = float(fields[6])
            
            # Phân loại năng lực theo khối
            if dtb_toan + dtb_ly + dtb_hoa >= 24:
                xeploai_thidaihoc[ma_hs] = [1, 1, 1, 3, 2]
            elif dtb_toan + dtb_ly + dtb_hoa >= 18:
                xeploai_thidaihoc[ma_hs] = [2, 2, 2, 3, 3]
            elif dtb_toan + dtb_ly + dtb_hoa >= 12:
                xeploai_thidaihoc[ma_hs] = [3, 3, 3, 4, 4]
            else:
                xeploai_thidaihoc[ma_hs] = [4, 4, 4, 4, 4]
            
            # Xử lý khối xã hội (C)
            if dtb_anh >= 21:
                xeploai_thidaihoc[ma_hs][3] = 1
            elif dtb_anh >= 15:
                xeploai_thidaihoc[ma_hs][3] = 2
            elif dtb_anh >= 12:
                xeploai_thidaihoc[ma_hs][3] = 3
            else:
                xeploai_thidaihoc[ma_hs][3] = 4
            
            # Xử lý khối cơ bản (D)
            if dtb_toan + dtb_anh >= 32:
                xeploai_thidaihoc[ma_hs][4] = 1
            elif dtb_toan + dtb_anh >= 24:
                xeploai_thidaihoc[ma_hs][4] = 2
            elif dtb_toan + dtb_anh >= 20:
                xeploai_thidaihoc[ma_hs][4] = 3
            else:
                xeploai_thidaihoc[ma_hs][4] = 4
    
    return xeploai_thidaihoc


# def main():
#     diem_trungbinh_file = "./diem_trungbinh.txt"  # Đường dẫn cho file điểm trung bình
#     diem_trungbinh_folder = "./"  # Đường dẫn cho thư mục chứa file điểm trung bình
    
#     # Xếp loại học lực chuẩn và ghi vào file
#     xeploai_hoc_luc = xeploai_hocsinh(diem_trungbinh_file)
#     xeploai_nang_luc = xeploai_thidaihoc_hocsinh(diem_trungbinh_folder)
    
#     with open("danhgia_hocsinh.txt", 'w') as file:
#         file.write("Ma HS;xeploai_TB chuan;xeploai_A;xeploai_A1;xeploai_B;xeploai_C;xeploai_D\n")
#         for ma_hs, xeploai in xeploai_hoc_luc.items():
#             file.write(f"{ma_hs};{xeploai};{xeploai_nang_luc[ma_hs][0]};{xeploai_nang_luc[ma_hs][1]};{xeploai_nang_luc[ma_hs][2]};{xeploai_nang_luc[ma_hs][3]};{xeploai_nang_luc[ma_hs][4]}\n")


# if __name__ == "__main__":
#     main()

def main():
    diem_trungbinh_file = "./diem_trungbinh.txt"  # Đường dẫn cho file điểm trung bình
    diem_trungbinh_folder = "./"  # Đường dẫn cho thư mục chứa file điểm trung bình
    
    # Xếp loại học lực chuẩn và ghi vào file
    xeploai_hoc_luc = xeploai_hocsinh(diem_trungbinh_file)
    xeploai_nang_luc = xeploai_thidaihoc_hocsinh(diem_trungbinh_folder)
    # Hàng đầu tiên của file “danhgia_hocsinh.txt” gồm các trường: “Ma HS”, “xeploai_TB chuan”, “xeploai_A”, “xeploai_A1”, “xeploai_B ”, “xeploai_C”, xeploai_D”. Hàng thứ 2 theo VD sau: “Nguyen Hai Nam; Gioi; 1; 1; 1; 3; 2”.
    with open("danhgia_hocsinh.txt", 'w') as file:
        file.write('“Ma HS”, “xeploai_TB chuan”, “xeploai_A”, “xeploai_A1”, “xeploai_B ”, “xeploai_C”, xeploai_D”\n')
        for ma_hs, xeploai in xeploai_hoc_luc.items():
            xeploai_nang_luc_hs = xeploai_nang_luc[ma_hs]
            file.write(f"{ma_hs}; {xeploai}; {xeploai_nang_luc_hs[0]}; {xeploai_nang_luc_hs[1]}; {xeploai_nang_luc_hs[2]}; {xeploai_nang_luc_hs[3]}; {xeploai_nang_luc_hs[4]}\n")


if __name__ == "__main__":
    main()

