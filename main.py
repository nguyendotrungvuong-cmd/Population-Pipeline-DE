
import logging
from pathlib import Path
from src.config import get_api_key
from src.argparse import arg_parse
from src.api_client import fetch_population
from src.storage import save_json, load_json,save_csv
from src.validate import validate
dir_log = Path(__file__).resolve().parent / "logs"
dir_log.mkdir(parents=True, exist_ok=True)
logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%H:%M:%S",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(dir_log / "pipeline.log", encoding="utf-8"),
        ],
    )
def main():
    args = arg_parse()
    country = args.country
    mode = args.mode
    
    logging.info(f"Country: {country}")
    logging.info(f"Mode: {mode}")
    try:
        if mode == "api":
            logging.info("Đang gọi API")
            api = get_api_key()
            logging.debug("API key loaded")
            logging.info("Đang lấy dữ liệu từ api")
            data = fetch_population(country=country, api_key=api)
            logging.info("Đã lấy thành công Data")
            save_json(country=country, data=data)
            logging.info("Đã lưu thành công json")
        else:
            data = load_json(country=country)
            logging.info("đã load thành công json")
        records = validate(data)
        logging.info(f"Đã lấy dc {len(records)} records")
        validate_records = validate(data=data)
        logging.info(f"Đã Pass kiểm tra: {len(validate_records)}")
        csv_path = save_csv(country=country,records=records)
        logging.info(f"Đã lưu file csv {csv_path}")
    except Exception:
        logging.exception("Thất bại")
        raise      
    else:
        logging.info("Đã chạy thành công pipeline")
if __name__ == "__main__":
    main()

