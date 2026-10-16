def validate(data):
    if data == []:
        raise ValueError("Không tìm thấy dữ liệu dân số, hoặc quốc gia không hợp lệ")
    if not isinstance(data,dict):
        raise TypeError("Data phải có dạng dict")
    if "historical_population" not in data:
        raise ValueError("Trường historical_population bị thiếu")
    records = data.get("historical_population")
    if not isinstance(records,list):
        raise TypeError("Records phải có dạng list")
    if not records:
        raise ValueError("Không tồn tại records")
    for index,record in enumerate(records,start=1):
        if not isinstance(record,dict):
            raise TypeError(f"{index} Record phải có dạng dict")
        if not record:
            raise ValueError(f"{index}Record không tồn tại")
        for field in record:
            value = record[field]
            if value is None:
                raise ValueError(f"{index} {field} không dc null")
    return records
    