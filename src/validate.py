def parse_population(data):
    if data == []:
        raise ValueError("Không tìm thấy dữ liệu dân số, hoặc quốc gia không hợp lệ")
    if not isinstance(data,dict):
        raise ValueError("Response phải là dạng dict")
    if "historical_population" not in data:
        raise ValueError("Thiếu trường dữ liệu historical_population")
    records = data.get("historical_population")
    if not isinstance(records,list):
        raise ValueError("Records phải là dạng list")
    
    if not records:
        raise ValueError("Records ko dc trống")
    for index,record in enumerate(records,start = 1):
        if not isinstance(record,dict):
            raise ValueError(f"Record phải có dạng dict {index}")
    return records 