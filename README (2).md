# ✍️ Ứng dụng Nhận Diện Chữ Viết Tay A-Z

Ứng dụng sử dụng mô hình học sâu (deep learning) để nhận diện chữ cái viết tay từ `A` đến `Z`. Người dùng có thể vẽ trực tiếp lên khung canvas và hệ thống sẽ dự đoán chữ cái tương ứng.

## 🧠 Mô Hình

Ứng dụng sử dụng mô hình `.h5` đã được huấn luyện với dữ liệu hình ảnh chữ cái viết tay (ví dụ: EMNIST).

## 🖥️ Yêu Cầu Hệ Thống

- Python 3.x
- Các thư viện Python:
  ```bash
  pip install pygame opencv-python keras numpy matplotlib
  ```

## 📁 Cấu Trúc Dự Án

```
handwriting_recognition/
├── main.py              # File chính chạy ứng dụng
├── model_hand.h5        # Mô hình đã huấn luyện
└── README.md            # Tệp hướng dẫn
```

## ▶️ Cách Chạy Ứng Dụng

1. Đảm bảo `model_hand.h5` nằm cùng thư mục với `main.py` hoặc cập nhật đúng đường dẫn trong code:
   ```python
   model = load_model('D:/chuẩn/model_hand.h5')  # Cập nhật nếu cần
   ```

2. Chạy ứng dụng bằng lệnh:
   ```bash
   python main.py
   ```

3. Giao diện sẽ hiển thị một cửa sổ gồm:
   - **Khung đen**: nơi để bạn vẽ chữ cái.
   - **Hướng dẫn**: cách sử dụng.
   - **Kết quả dự đoán**: hiển thị chữ cái nhận diện được và độ chính xác.

## 🖱️ Hướng Dẫn Sử Dụng

- **Bắt đầu vẽ**: Dùng chuột trái để vẽ một chữ cái trong khung đen.
- **Xem dự đoán**: Sau khi nhả chuột, hệ thống sẽ tự động đưa ra dự đoán.
- **Xóa khung vẽ**: Nhấn phím `C` trên bàn phím để xóa và vẽ lại từ đầu.

## 📝 Lưu Ý

- Vui lòng viết rõ ràng, chỉ một chữ cái trong mỗi lần vẽ.
- Mô hình có thể hoạt động tốt hơn nếu bạn viết gần giống dữ liệu huấn luyện (in hoa, đơn nét).

## 📸 Hình Ảnh Minh Họa

![demo](https://user-images.githubusercontent.com/your-image-url/demo.png)

## 📌 Đóng Góp & Mở Rộng

Bạn có thể cải tiến ứng dụng bằng cách:
- Thêm nút `Dự đoán` và `Xóa`.
- Cho phép lưu hình ảnh người dùng vẽ.
- Hiển thị top-3 dự đoán gần đúng nhất.

---

👨‍💻 **Tác giả**: [Tên bạn ở đây]  
📅 **Cập nhật lần cuối**: 2025-05-03
