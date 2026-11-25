import csv
from pathlib import Path

from src.lab08.models import STUDENT_FIELDS, student_from_dict
from src.lab08.models import update_student as update_record


def ensure_storage(path):
    """Создать хранилище с заголовком, если его ещё нет."""
    path = Path(path)
    if not path.exists():
        save_students(path, [])


def load_students(path):
    """Прочитать и проверить записи студентов."""
    try:
        file = Path(path).open(encoding="utf-8", newline="")
    except FileNotFoundError:
        return []

    students = []
    with file:
        reader = csv.DictReader(file, strict=True)
        try:
            if reader.fieldnames != list(STUDENT_FIELDS):
                raise ValueError("CSV: ожидается заголовок")
            for row in reader:
                if None in row or None in row.values():
                    raise ValueError("неверное число колонок")
                try:
                    row["gpa"] = float(row["gpa"])
                except ValueError:
                    raise ValueError("gpa: ожидается число")
                students.append(student_from_dict(row))
        except (ValueError, csv.Error) as exc:
            raise ValueError(f"CSV, строка {reader.line_num}: {exc}")
    return students


def save_students(path, students):
    """Записать временный CSV и заменить им основной файл."""
    students = [student_from_dict(student) for student in students]
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary_path = path.with_name(f"{path.stem}_temp{path.suffix}")
    file = temporary_path.open("x", encoding="utf-8", newline="")
    try:
        with file:
            writer = csv.DictWriter(file, fieldnames=STUDENT_FIELDS)
            writer.writeheader()
            writer.writerows(students)
        temporary_path.replace(path)
    except BaseException:
        temporary_path.unlink(missing_ok=True)
        raise


def add_student(path, student):
    """Проверить и добавить студента с уникальным ФИО."""
    student = student_from_dict(student)
    students = load_students(path)
    if any(record["fio"] == student["fio"] for record in students):
        raise ValueError(f"Студент с ФИО «{student['fio']}» уже есть в базе")
    students.append(student)
    save_students(path, students)


def list_students(path, sort_by=None):
    """Вернуть записи в порядке файла, по ФИО или по GPA."""
    if sort_by not in (None, "fio", "gpa"):
        raise ValueError("Сортировка возможна только по ФИО или gpa")
    students = load_students(path)
    if sort_by is None:
        return students
    return sorted(students, key=lambda student: student[sort_by])


def find_students(path, substr):
    """Найти ФИО, содержащие подстроку без учёта регистра."""
    substr = substr.casefold()
    return [student for student in load_students(path) if substr in student["fio"].casefold()]


def remove_student(path, fio):
    """Удалить все записи с указанным ФИО."""
    students = load_students(path)
    remaining = [student for student in students if student["fio"] != fio]
    removed = len(students) - len(remaining)
    if removed:
        save_students(path, remaining)
    return removed


def update_student(path, fio, /, **fields):
    """Обновить первую запись с указанным ФИО."""
    for field in fields:
        if field not in STUDENT_FIELDS:
            raise KeyError(field)
    students = load_students(path)
    for index, student in enumerate(students):
        if student["fio"] == fio:
            students[index] = update_record(student, **fields)
            save_students(path, students)
            return True
    return False
