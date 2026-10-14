import argparse
from pathlib import Path
import sys
from src.lib.text import normalize, tokenize, count_freq, top_n
from src.lab04.io_txt_csv import read_text, write_csv

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--in", dest="input_path", type=Path,
                        default=Path("data/input.txt"), help="Входной файл")
    parser.add_argument("--out", dest="output_path", type=Path,
                        default=Path("data/report.csv"), help="Выходной файл")
    parser.add_argument("--encoding", default="utf-8", help="Кодировка входа")
    args = parser.parse_args(argv)

    try:
        text = read_text(args.input_path, encoding=args.encoding)
        text_freqs = count_freq(tokenize(normalize(text)))
        text_top = top_n(text_freqs, len(text_freqs))
        write_csv(text_top, args.output_path, ("word", "count"))
    except (OSError, UnicodeError, LookupError) as error:
        print(f"Ошибка: {error}")
        sys.exit(1)

    print(f"Всего слов: {sum(text_freqs.values())}")
    print(f"Уникальных слов: {len(text_freqs)}")
    print("Топ-5:")
    for word, count in text_top[:5]:
        print(f"{word}:{count}")
    return 0


if __name__ == "__main__":
    main()
