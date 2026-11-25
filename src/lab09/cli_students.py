import argparse
import sys

from src.lab08.models import format_student

from src.lab09.group import add_student, find_students, list_students, remove_student, update_student


def main(argv=None):
    parser = argparse.ArgumentParser(description="Работа с CSV-базой студентов")
    parser.add_argument(
        "--db", default="data/lab09/students.csv", help="Путь к CSV-базе"
    )
    commands = parser.add_subparsers(dest="command", required=True)

    add_parser = commands.add_parser("add", help="Добавить студента")
    add_parser.add_argument("--fio", required=True)
    add_parser.add_argument("--birthdate", required=True)
    add_parser.add_argument("--group", required=True)
    add_parser.add_argument("--gpa", required=True)

    list_parser = commands.add_parser("list", help="Вывести список студентов")
    list_parser.add_argument("--sort", choices=("fio", "gpa"))

    find_parser = commands.add_parser("find", help="Найти студентов по части ФИО")
    find_parser.add_argument("--q", required=True)

    remove_parser = commands.add_parser("remove", help="Удалить записи по ФИО")
    remove_parser.add_argument("--fio", required=True)

    update_parser = commands.add_parser("update", help="Обновить запись по ФИО")
    update_parser.add_argument("--fio", required=True)
    update_parser.add_argument("--birthdate")
    update_parser.add_argument("--group")
    update_parser.add_argument("--gpa")

    args = parser.parse_args(argv)
    try:
        if args.command == "add":
            add_student(
                args.db,
                {
                    "fio": args.fio,
                    "birthdate": args.birthdate,
                    "group": args.group,
                    "gpa": float(args.gpa),
                },
            )
        elif args.command == "list":
            for student in list_students(args.db, args.sort):
                print(format_student(student))
        elif args.command == "find":
            for student in find_students(args.db, args.q):
                print(format_student(student))
        elif args.command == "remove":
            removed = remove_student(args.db, args.fio)
            print(f"Удалено записей: {removed}")
        elif args.command == "update":
            fields = {field: getattr(args, field) for field in ("birthdate", "group", "gpa") if getattr(args, field) is not None}
            if "gpa" in fields:
                fields["gpa"] = float(fields["gpa"])
            if update_student(args.db, args.fio, **fields):
                print("Запись обновлена")
            else:
                print("Студент не найден")
    except (ValueError, KeyError, OSError) as exc:
        print(f"Ошибка: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
