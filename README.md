<div align="center">
# 🧠 NLP Analysis Medicine
### Hệ thống Phân tích Dữ liệu Y khoa bằng Xử lý Ngôn ngữ Tự nhiên
 
*Ứng dụng mô hình ngôn ngữ lớn để phân tích và xử lý dữ liệu y khoa tiếng Việt*
 
</div>
---
 
## 📋 Mục lục
 
- [Giới thiệu](#-giới-thiệu)
- [Yêu cầu hệ thống](#-yêu-cầu-hệ-thống)
- [Cài đặt](#-cài-đặt)
- [Cấu trúc thư mục](#-cấu-trúc-thư-mục)
- [Chạy ứng dụng](#-chạy-ứng-dụng)
- [Lưu ý](#-lưu-ý)
- [Tác giả](#-tác-giả)
---
 
## 🔍 Giới thiệu
 
Dự án sử dụng **Xử lý Ngôn ngữ Tự nhiên (NLP)** để phân tích dữ liệu y khoa. Mô hình được huấn luyện chuyên biệt cho lĩnh vực y tế, hỗ trợ trích xuất thông tin, phân loại bệnh lý và phân tích văn bản lâm sàng.
 
> ⚠️ **Lưu ý về Model:** Do file trọng số mô hình có kích thước lớn (>500MB), file này **không được lưu trên GitHub**. Bạn cần tải thủ công theo hướng dẫn bên dưới.
 
---
 
## 💻 Yêu cầu hệ thống
 
| Yêu cầu | Phiên bản tối thiểu |
|---------|-------------------|
| Python | 3.8+ |
| RAM | 8GB+ |
| Dung lượng ổ đĩa | 2GB+ (bao gồm model) |
| Kết nối Internet | Cần thiết để tải model |
 
---
 
## 🚀 Cài đặt
 
### Bước 1 — Clone dự án
 
```bash
git clone https://github.com/LuongTung2303/NLP_ANALYSIST_MEDICINE.git
cd NLP_ANALYSIST_MEDICINE
```
 
### Bước 2 — Tạo môi trường ảo
 
> 💡 **Khuyến nghị:** Dùng môi trường ảo để tránh xung đột thư viện giữa các dự án.
 
**Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```
 
**Linux / macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```
 
### Bước 3 — Cài đặt thư viện
 
```bash
pip install -r requirements.txt
```
 
### Bước 4 — Tải Model *(Bắt buộc)*
 
File `model.safetensors` (~500MB) cần được tải thủ công:
 
**1.** Tải file tại: `https://drive.google.com/file/d/10Dydr17tloKH8cCkwRc897S37DGuFOJ3/view`
 
**2.** Di chuyển file vào đúng thư mục:
 
```
NLP_ANALYSIST_MEDICINE/
└── src/
    └── saved_model/
        └── model.safetensors  ✅ ← Đặt file vào đây
```
 
---
 
## 📂 Cấu trúc thư mục
 
```
NLP_Analysist_Medicine/
├── src/
│   ├── saved_model/
│   │   └── model.safetensors     # File trọng số mô hình (tải thủ công)
│   └── main.py                   # File chạy chính
├── .gitignore
├── requirements.txt
└── README.md
```
 
---
 
## ▶️ Chạy ứng dụng
 
Sau khi hoàn tất tất cả các bước cài đặt, khởi chạy chương trình bằng lệnh:
 
```bash
python src/main.py
```
 
---
 
## 📝 Lưu ý
 
- Đảm bảo **kết nối internet ổn định** khi tải model từ Google Drive.
- Nếu gặp lỗi thiếu thư viện, chạy lại: `pip install -r requirements.txt`
- File `saved_model/` đã được thêm vào `.gitignore` — **không commit** file model lên GitHub.
---
 
## 👤 Tác giả
 
<div align="center">
**Luong Tung**
 
[![GitHub](https://img.shields.io/badge/GitHub-@LuongTung2303-181717?style=for-the-badge&logo=github)](https://github.com/LuongTung2303)
 
</div>