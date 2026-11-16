from datetime import date

STUDENT_FIELDS = ("fio", "birthdate", "group", "gpa")

def make_student(fio, birthdate, group, gpa):
    """Создать проверенную запись"""
    rec = {"fio": fio, "birthdate": birthdate, "group": group, "gpa": gpa}
    validate_student(rec)
    rec["fio"] = fio.strip()
    rec["group"] = group.strip()
    rec["gpa"] = float(gpa)
    return rec


def validate_student(rec):
    """Проверить ключи и значения записи"""
    if not isinstance(rec, dict):
        raise ValueError("Запись студента должна быть словарем")
    if set(rec) != set(STUDENT_FIELDS):
        missing = [key for key in STUDENT_FIELDS if key not in rec]
        extra = [key for key in rec if key not in STUDENT_FIELDS]
        raise ValueError(
            f"Неверный набор полей: отсутствуют {missing}, лишние {extra}"
        )

    for field in ("fio", "group"):
        if not isinstance(rec[field], str) or not rec[field].strip():
            raise ValueError(f"{field}: ожидается непустая строка")

    birthdate = rec["birthdate"]
    if not isinstance(birthdate, str):
        raise ValueError("birthdate: ожидается строка в формате YYYY-MM-DD")
    try:
        birthday = date.fromisoformat(birthdate)
    except ValueError:
        raise ValueError("birthdate: ожидается существующая дата в формате YYYY-MM-DD")
    if birthday.isoformat() != birthdate:
        raise ValueError("birthdate: ожидается формат YYYY-MM-DD")
    if birthday > date.today():
        raise ValueError("birthdate: дата рождения не может быть в будущем")

    gpa = rec["gpa"]
    if isinstance(gpa, bool) or not isinstance(gpa, (int, float)):
        raise ValueError("gpa: ожидается число (int или float), не bool")
    if not 0 <= gpa <= 5:
        raise ValueError("gpa: средний балл должен быть от 0 до 5")


def student_age(rec, today=None):
    """Вернуть число полных лет на указанную дату"""
    validate_student(rec)
    birthday = date.fromisoformat(rec["birthdate"])
    if today is None:
        today = date.today()
    if not isinstance(today, date):
        raise ValueError("today: ожидается объект date")
    if today < birthday:
        raise ValueError("today: дата расчета не может быть раньше рождения")
    return today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))


def student_to_dict(rec):
    """Вернуть независимую копию проверенной записи для сериализации"""
    validate_student(rec)
    return {field: rec[field] for field in STUDENT_FIELDS}


def student_from_dict(d):
    """Создать запись из словаря с точным набором полей"""
    validate_student(d)
    return make_student(**d)


def format_student(rec):
    """Представить отформатированную запись"""
    age = student_age(rec)
    surname, *names = rec["fio"].split()
    initials = "".join(name[0] + "." for name in names)
    short_name = f"{surname} {initials}".strip()
    return f"{short_name} ({rec['group']}), {age} лет, GPA {rec['gpa']:.2f}"


def update_student(rec, **fields):
    """Создать обновленную запись, неизвестные поля вызывают KeyError"""
    updated = student_to_dict(rec)
    for field in fields:
        if field not in STUDENT_FIELDS:
            raise KeyError(field)
    updated.update(fields)
    return student_from_dict(updated)
