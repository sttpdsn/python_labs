import csv
from pathlib import Path


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    return Path(path).read_text(encoding=encoding)


def write_csv(
    rows: list[tuple | list],
    path: str | Path,
    header: tuple[str, ...] | None = None,
) -> None:
    width = len(header) if header is not None else (len(rows[0]) if rows else 0)
    if any(len(row) != width for row in rows):
        raise ValueError("Все строки CSV и заголовок должны иметь одинаковую длину")
    with Path(path).open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=",")
        if header is not None:
            writer.writerow(header)
        writer.writerows(rows)
