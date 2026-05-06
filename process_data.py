import pandas as pd
import os

def export_to_test_txt(excel_path, output_path):
    # Đảm bảo thư mục đích tồn tại
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    print(f"📦 Đang xử lý file: {excel_path}")
    df = pd.read_excel(excel_path)
    
    # Xử lý các giá trị NaN để tránh lỗi khi ghi file
    df['token'] = df['token'].fillna('').astype(str).str.strip()
    df['bio_tag'] = df['bio_tag'].fillna('O').astype(str).str.strip()

    count_cases = 0
    with open(output_path, 'w', encoding='utf-8') as f:
        current_case_id = None
        
        for _, row in df.iterrows():
            case_id = row['case_id']
            
            # Nếu sang case_id mới, ghi một dòng trống để ngắt câu (sentence break)
            if current_case_id is not None and case_id != current_case_id:
                f.write('\n')
                count_cases += 1
                
            # Ghi Token và Tag cách nhau 1 khoảng trắng
            f.write(f"{row['token']} {row['bio_tag']}\n")
            current_case_id = case_id
            
    print(f"✅ Đã chuyển đổi xong {count_cases + 1} bệnh án.")
    print(f"🚀 File lưu tại: {output_path}")

# Cấu hình đường dẫn dựa theo cấu trúc folder trong ảnh của bạn
input_excel = "data/raw/benh_an_noi_khoa/data_50_test.xlsx" 
output_txt = "data/processed/test.txt"

if __name__ == "__main__":
    export_to_test_txt(input_excel, output_txt)