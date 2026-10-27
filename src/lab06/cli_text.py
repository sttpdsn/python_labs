import argparse
from lib.text import *


def main(argv=None):
    parser = argparse.ArgumentParser(description="Работа с текстовыми файлами")
    subparsers = parser.add_subparsers(dest="command", required=True)

    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help="Входной файл")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки с 1")

    stats_parser = subparsers.add_parser("stats", help="Вывести топ слов по частоте")
    stats_parser.add_argument("--input", required=True, help="Входной файл")
    stats_parser.add_argument("--top", default=5, help="Количество слов (по умолчанию: 5)")

    args = parser.parse_args(argv)
    if args.command == "stats" and args.top <= 0:
        parser.error("--top должен быть положительным целым числом")

    try:
        with args.input.open(encoding="utf-8") as file:
            if args.command == "cat":
                for number, line in enumerate(file, start=1):
                    if args.n:
                        print(f"{number}: {line}", end="")
                    else:
                        print(line, end="")
            elif args.command == "stats":
                text = file.read()
                for word, count in top_n(count_freq(tokenize(normalize(text))), args.top):
                    print(f"{word}\t{count}")
    except FileNotFoundError:
        raise FileNotFoundError("Файл не найден")

if __name__ == "__main__":
    main()
