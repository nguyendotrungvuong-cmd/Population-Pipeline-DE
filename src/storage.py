import json
from pathlib import Path
import csv

dir = Path(__file__).resolve().parent.parent
raw_dir = dir / "data/raw"
processed_dir = dir / "data/processed"


def save_json(country, data):
    raw_dir.mkdir(parents=True, exist_ok=True)
    file_path = raw_dir / f"{country}.json"
    with file_path.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    return file_path


def load_json(country):
    file_path = raw_dir / f"{country}.json"
    with file_path.open("r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def save_csv(country, records):
    processed_dir.mkdir(parents=True, exist_ok=True)
    file_path = processed_dir / f"{country}.csv"
    columns = list(records[0].keys())
    with file_path.open("w", encoding="utf-8-sig", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(records)
    return file_path
