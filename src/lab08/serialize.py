import csv
import json
from models import STUDENT_FIELDS, student_from_dict, student_to_dict

def students_to_json(students, path):
    """Сохранить проверенные записи в UTF-8 JSON с отступом в два пробела."""
    data = [student_to_dict(student) for student in students]
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def students_from_json(path):
    """Прочитать JSON-массив; при ошибке указать номер записи, начиная с 1."""
    with open(path, encoding="utf-8") as file:
        data = json.load(file)
    if not isinstance(data, list):
        raise ValueError("JSON должен содержать массив записей студентов")

    students = []
    for number, record in enumerate(data, start=1):
        try:
            students.append(student_from_dict(record))
        except ValueError as exc:
            raise ValueError(f"Запись {number}: {exc}")
    return students


def students_from_csv(path):
    """Прочитать CSV в режиме strict, преобразовав строковый gpa в число."""
    students = []
    with open(path, encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        if reader.fieldnames is None or sorted(reader.fieldnames) != sorted(
            STUDENT_FIELDS
        ):
            raise ValueError("CSV: ожидаются заголовки fio,birthdate,group,gpa")
        for number, record in enumerate(reader, start=1):
            try:
                record["gpa"] = float(record["gpa"])
                students.append(student_from_dict(record))
            except (ValueError, TypeError) as exc:
                raise ValueError(f"Запись {number}: {exc}")
    return students
