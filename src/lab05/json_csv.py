import json
import csv
from pathlib import Path

def json_to_csv(json_path: str, csv_path: str) -> None:
    source = Path(json_path)
    target = Path(csv_path)

    if not source.is_file():
        raise FileNotFoundError("Файл не найден")
    if source.suffix.lower() != ".json":
        raise ValueError("Входной файл должен быть JSON")
    if target.suffix.lower() != ".csv":
        raise ValueError("Выходной файл должен быть CSV")
    
    with source.open(newline="", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            raise ValueError("JSON пустой или содержит некорректные данные")

    columns = []
    for item in data:
        for key in item:
            if key not in columns:
                columns.append(key)

    with target.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        writer.writerows(data)

def csv_to_json(csv_path: str, json_path: str) -> None:
    source = Path(csv_path)
    target = Path(json_path)

    if not source.is_file():
        raise FileNotFoundError("Файл не найден")
    if source.suffix.lower() != ".csv":
        raise ValueError("Входной файл должен быть CSV")
    if target.suffix.lower() != ".json":
        raise ValueError("Выходной файл должен быть JSON")

    with source.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f, restval="")

        if not reader.fieldnames:
            raise ValueError("В CSV нет заголовка")
        
        rows = list(reader)

    if len(rows) == 0:
        raise ValueError("В CSV нет данных")

    with Path(json_path).open("w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=1)