def format_record(rec: tuple[str, str, float]) -> str:
    if not isinstance(rec, tuple):
        raise TypeError("Запись должна быть кортежем")
    if len(rec) != 3:
        raise ValueError("Запись должна содержать ФИО, группу и GPA")

    fio, group, gpa = rec

    if not isinstance(fio, str) or not isinstance(group, str):
        raise TypeError("ФИО и группа должны быть строками")
    if not isinstance(gpa, (int, float)):
        raise TypeError("GPA должен быть числом")
    if not 0.0 <= gpa <= 5.0:
        raise ValueError("GPA должен быть от 0 до 5")

    fio_parts = fio.split()
    if len(fio_parts) not in (2, 3):
        raise ValueError("ФИО должно состоять из двух или трёх слов")

    group = group.strip()
    if not group:
        raise ValueError("Группа не должна быть пустой")

    surname = fio_parts[0].capitalize()
    initials = "".join(f"{name[0].upper()}." for name in fio_parts[1:])

    return f"{surname} {initials}, гр. {group}, GPA {gpa:.2f}"


def show_results(function, cases) -> None:
    for value in cases:
        try:
            result = function(value)
        except (ValueError, TypeError) as error:
            result = error

        print(f"{value} -> {result}")


if __name__ == "__main__":
    print("format_record:")
    show_results(
        format_record,
        [
            ("Иванов Иван Иванович", "BIVT-25", 4.6),
            ("Петров Пётр", "IKBO-12", 5.0),
            ("Петров Пётр Петрович", "IKBO-12", 5.0),
            ("  сидорова  анна   сергеевна ", "BPM-01", 3.999),
            ("Иванов Иван", "", 4.0),
            ("Иванов Иван", "BIVT-01", "пять"),
        ],
    )
