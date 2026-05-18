# 🩺 Dự Án Dự Đoán Bệnh Tim - MediUDA

Chào mừng bạn đến với dự án **MediUDA - Hệ thống chẩn đoán và dự đoán nguy cơ mắc bệnh tim** sử dụng thuật toán Học Máy **k-Nearest Neighbors (k-NN)**. 

🌐 **Link trang web trực tuyến:** [https://dudoanbenhtim.onrender.com](https://dudoanbenhtim.onrender.com)

---

## 🚀 Công Nghệ Sử Dụng
*   **Backend:** Python 3.11+, Django Web Framework, Django REST Framework.
*   **Machine Learning:** NumPy, Pandas, Scikit-learn (dùng để chia tập dữ liệu và xử lý mảng).
*   **Frontend:** HTML5, CSS3, JavaScript, jQuery, Bootstrap 4.
*   **Deployment:** Render Cloud Platform, Gunicorn, WhiteNoise (quản lý file tĩnh).

---

## 📂 Danh Sách 13 Chỉ Số Sức Khỏe Đầu Vào
Hệ thống sử dụng mô hình k-NN được huấn luyện trực tiếp trên tập dữ liệu chuẩn đoán tim (`heart.csv`) dựa trên 13 thông số đầu vào sau:
1.  **Tuổi (Age):** Độ tuổi của bệnh nhân (0 - 100).
2.  **Giới tính (Sex):** Nam (1) hoặc Nữ (0).
3.  **Đau ngực (Chest Pain - cp):** Loại đau ngực (Giá trị từ 0 đến 3).
4.  **Huyết áp nghỉ (Resting Blood Pressure - trestbps):** Huyết áp tâm thu lúc nghỉ ngơi (80 - 200 mmHg).
5.  **Cholesterol (chol):** Hàm lượng Cholesterol trong máu (100 - 600 mg/dl).
6.  **Đường huyết lúc đói (Fasting Blood Sugar - fbs):** Nếu > 120 mg/dl (1), ngược lại (0).
7.  **Điện tâm đồ lúc nghỉ (Restecg):** Kết quả điện tâm đồ lúc nghỉ ngơi (0, 1, 2).
8.  **Nhịp tim tối đa (Maximum Heart Rate - thalach):** Nhịp tim lớn nhất đạt được lúc gắng sức (60 - 220).
9.  **Đau ngực do gắng sức (Exercise Induced Angina - exang):** Có (1) hoặc Không (0).
10. **ST chênh (Oldpeak):** Mức độ suy giảm ST do gắng sức so với lúc nghỉ (0.0 - 6.2).
11. **Độ dốc (Slope):** Độ dốc của đoạn ST lúc gắng sức đỉnh điểm (0, 1, 2).
12. **Số lượng mạch chính (ca):** Số lượng các mạch máu chính được tô màu bởi fluoroscopy (0 - 4).
13. **Thallium scan (thal):** Kết quả đo phóng xạ Thallium (0 - 3).

---

## 💻 Hướng Dẫn Cách Chạy Dự Án Dưới Local (Máy Cá Nhân)

Để chạy dự án này trên máy tính của bạn, hãy làm theo các bước đơn giản sau:

### Bước 1: Tải mã nguồn về máy
Mở Terminal hoặc CMD (Command Prompt) lên và chạy lệnh sau để clone dự án:
```bash
git clone https://github.com/LUANVANSADBOY78/DuDoanBenhTim.git
cd DuDoanBenhTim
```

### Bước 2: Tạo môi trường ảo Python (Virtual Environment)
Việc này giúp quản lý các thư viện cài đặt không bị xung đột với hệ thống của máy:
*   **Trên Windows:**
    ```bash
    python -m venv .venv
    .\.venv\Scripts\activate
    ```
*   **Trên macOS / Linux:**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

### Bước 3: Cài đặt các thư viện cần thiết
Cài đặt tất cả các thư viện cần thiết được định nghĩa sẵn trong `requirements.txt`:
```bash
pip install -r requirements.txt
```

### Bước 4: Chạy migration dữ liệu (Nếu có)
Khởi tạo cơ sở dữ liệu mặc định của Django:
```bash
python manage.py migrate
```

### Bước 5: Khởi động Server cục bộ
Khởi chạy dự án dưới local:
```bash
python manage.py runserver
```

### Bước 6: Truy cập ứng dụng
Sau khi khởi động thành công, mở trình duyệt web lên và truy cập đường dẫn:
👉 **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

---

## 🧠 Nguyên Lý Hoạt Động Của Thuật Toán k-NN Trong Dự Án
1.  **Đọc Dữ Liệu:** Khi ứng dụng khởi chạy, hệ thống tự động tải tệp dữ liệu bệnh tim `heart.csv`.
2.  **Huấn Luyện:** Chia tập dữ liệu thành 2 tập (80% để Train k-NN và 20% để Test đánh giá độ chính xác).
3.  **Tính Khoảng Cách (Euclidean Distance):** Khi người dùng nhập các chỉ số sức khỏe của mình từ Form và ấn **"Chẩn đoán"**, hệ thống sẽ tính khoảng cách Euclidean giữa điểm dữ liệu mới nhập với tất cả các mẫu trong tập huấn luyện (`X_train`).
4.  **Dự Đoán Kết Quả:** Lấy ra $k=3$ láng giềng gần nhất có khoảng cách nhỏ nhất. Nhãn bệnh (0: Khỏe mạnh, 1: Mắc bệnh) xuất hiện nhiều nhất trong 3 láng giềng này sẽ được chọn làm nhãn dự đoán và trả về màn hình cho người dùng ngay lập tức thông qua công nghệ API truyền nhận dạng JSON không cần tải lại trang.

---
💡 *Dự án được xây dựng và đóng góp bởi **LUANVANSADBOY78**.*
