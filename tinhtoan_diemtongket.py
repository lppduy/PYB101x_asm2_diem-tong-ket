def tinhdiem_trungbinh(input_file):
    diem_trungbinh = {}  # Khởi tạo dictionary để lưu điểm trung bình của từng học sinh
    
    with open(input_file, 'r') as file:
        lines = file.readlines()
        
        # Lấy danh sách các môn học từ hàng đầu tiên của file
        subjects = lines[0].strip().split(',')[1:]
        
        for line in lines[1:]:
            data = line.strip().split(';')  # Tách dữ liệu từng dòng thành danh sách
            ma_hs = data[0]  # Lấy mã học sinh
            
            diem_tb = {}  # Khởi tạo dictionary để lưu điểm trung bình của từng môn học
            
            for i in range(1, len(data)):
                mon_hoc = subjects[i - 1]  # Lấy tên môn học
                
                diem = [float(x) for x in data[i].split(',')]  # Tách dữ liệu điểm thành phần thành danh sách
                
                if len(diem) == 4:  # Môn tự nhiên
                    # Tính điểm trung bình và làm tròn đến 2 chữ số
                    diem_tb[mon_hoc] = round(0.05 * diem[0] + 0.1 * diem[1] + 0.15 * diem[2] + 0.7 * diem[3], 2)
                elif len(diem) == 5:  # Môn xã hội
                    # Tính điểm trung bình và làm tròn đến 2 chữ số
                    diem_tb[mon_hoc] = round(0.05 * diem[0] + 0.1 * diem[1] + 0.1 * diem[2] + 0.15 * diem[3] + 0.6 * diem[4], 2)
            
            diem_trungbinh[ma_hs] = diem_tb  # Lưu điểm trung bình của học sinh vào dictionary chính
            
    return diem_trungbinh

def luudiem_trungbinh(output_file, diem_trungbinh):
    with open(output_file, 'w') as file:
        subjects = list(diem_trungbinh.values())[0].keys()
        header = "Ma HS," + ",".join(subjects) + "\n"
        file.write(header)
        
        for ma_hs, diem_tb in diem_trungbinh.items():
            diem_tb_str = [str(diem) for diem in diem_tb.values()]
            line = ma_hs + "," + ",".join(diem_tb_str) + "\n"
            file.write(line)

def main():
    input_file = "diem_chitiet.txt"
    output_file = "diem_trungbinh.txt"
    
    diem_trungbinh = tinhdiem_trungbinh(input_file)  # Tính điểm trung bình từ file dữ liệu
    luudiem_trungbinh(output_file, diem_trungbinh)  # Lưu điểm trung bình ra file
    
if __name__ == "__main__":
    main()
