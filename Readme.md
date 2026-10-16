# Population Repo

Bài tập Python xây dựng pipeline lấy dữ liệu dân số từ API Ninjas, kiểm tra dữ liệu và lưu thành JSON, CSV.

## Chức năng
- Lấy dữ liệu dân số theo quốc gia từ API.
- Lưu và đọc dữ liệu JSON.
- Kiểm tra cấu trúc và tính hợp lệ của dữ liệu.
- Xuất kết quả ra CSV.
- Ghi log quá trình chạy.

## Cài đặt

```bash
pip install -r requirements.txt
```

## Cách chạy

Lấy dữ liệu từ API:

```bash
python main.py --country vietnam --mode api
```

Đọc dữ liệu JSON đã lưu:

```bash
python main.py --country vietnam --mode load_json
```

## Kết quả

- `data/raw/`: Dữ liệu JSON gốc.
- `data/processed/`: Dữ liệu CSV.
- `logs/`: Nhật ký chạy chương trình.

