# Population Repo

Bài tập Python xây dựng pipeline thu thập dữ liệu dân số từ API Ninjas, kiểm tra dữ liệu và xuất kết quả ra JSON, CSV.

## 1. Chức năng chính

- Lấy dữ liệu dân số theo quốc gia từ API.
- Lưu dữ liệu gốc dưới dạng JSON.
- Đọc lại JSON đã lưu mà không cần gọi API.
- Kiểm tra cấu trúc và tính hợp lệ của dữ liệu.
- Xuất dữ liệu đã xử lý ra CSV.
- Ghi log quá trình chạy và lỗi phát sinh.

## 2. Các hàm chính

| Hàm | Chức năng |
|---|---|
| `get_api_key()` | Đọc API key từ biến môi trường. |
| `fetch_population()` | Gửi request đến API và nhận dữ liệu dân số. |
| `save_json()` | Lưu dữ liệu gốc vào file JSON. |
| `load_json()` | Đọc dữ liệu từ file JSON đã lưu. |
| `parse_population()` | Kiểm tra cấu trúc response và lấy danh sách bản ghi dân số. |
| `validate()` | Kiểm tra tính hợp lệ của các bản ghi. |
| `save_csv()` | Xuất danh sách bản ghi ra file CSV. |
| `main()` | Điều phối các bước thực hiện pipeline. |

## 3. Luồng xử lý

**Chế độ API:**

`Nhập quốc gia → Gọi API → Lưu JSON → Parse → Validate → Xuất CSV`

**Chế độ đọc JSON:**

`Nhập quốc gia → Đọc JSON → Parse → Validate → Xuất CSV`

## 4. Các bước kiểm tra dữ liệu

1. **Input:** Kiểm tra tên quốc gia không được để trống.
2. **API:** Kiểm tra lỗi HTTP và phản hồi từ API.
3. **Response:** Kiểm tra dữ liệu trả về có đúng kiểu `dict` và chứa `historical_population`.
4. **Records:** Kiểm tra danh sách bản ghi không rỗng và mỗi bản ghi có kiểu `dict`.
5. **Validation:** Kiểm tra các trường dữ liệu theo quy tắc được định nghĩa trong chương trình.
6. **Logging:** Ghi nhận các bước xử lý và thông báo lỗi khi pipeline thất bại.

## 5. Cài đặt

```bash
pip install -r requirements.txt
```
## 6. Chạy chương trình

Lấy dữ liệu từ API:

```bash
python main.py --country vietnam --mode api
```

Đọc dữ liệu JSON đã lưu:

```bash
python main.py --country vietnam --mode load_json
```

## 7. Kết quả

- `data/raw/`: File JSON gốc.
- `data/processed/`: File CSV.
- `logs/`: Nhật ký chạy chương trình.

**Lưu ý:** Không đưa API key thật hoặc file `.env` lên GitHub.
