# ЛР6 — CLI-утилиты для текста и конвертации данных

`cli_text.py` выводит содержимое файлов и считает частоты слов.
`cli_convert.py` запускает конвертацию JSON, CSV и XLSX с помощью функций из лабораторной №5.

## Запуск

```bash
python3 -m src.lab06.cli_text <подкоманда> [параметры]
python3 -m src.lab06.cli_convert <подкоманда> [параметры]
```

## Команды cli_text.py

| Подкоманда | Назначение | Параметры |
| --- | --- | --- |
| `cat` | Вывести содержимое файла построчно | `--input <путь>` — обязательный входной файл; `-n` — нумерация строк с 1 |
| `stats` | Вывести самые частые слова | `--input <путь>` — обязательный входной файл; `--top <N>` — число слов (по умолчанию 5) |

### cat — вывод файла

```bash
python3 -m src.lab06.cli_text cat --input data/samples/people.csv
python3 -m src.lab06.cli_text cat --input data/samples/people.csv -n
```
Файл читается в UTF-8. С флагом `-n` каждая строка получает номер в формате `1: содержимое строки`.
![пример](/images/lab06/cat.png)

### stats — частоты слов

```bash
python3 -m src.lab06.cli_text stats --input data/samples/text.txt
python3 -m src.lab06.cli_text stats --input data/samples/text.txt --top 3
```

Результат выводится в формате «слово — табуляция — количество», по убыванию частоты; при равной частоте — по алфавиту. Если разных слов меньше, чем `N`, выводятся все имеющиеся. Значение `--top` должно быть положительным целым числом.
![пример](/images/lab06/stats.png)

## Команды cli_convert.py

| Подкоманда | Назначение | Параметры |
| --- | --- | --- |
| `json2csv` | Преобразовать JSON в CSV | `--in <путь>` — входной JSON; `--out <путь>` — выходной CSV |
| `csv2json` | Преобразовать CSV в JSON | `--in <путь>` — входной CSV; `--out <путь>` — выходной JSON |
| `csv2xlsx` | Преобразовать CSV в XLSX | `--in <путь>` — входной CSV; `--out <путь>` — выходной XLSX |

Для каждой подкоманды оба параметра обязательны. Требования к структуре данных и обработка файлов определяются функциями из `lab05`.

```bash
python3 -m src.lab06.cli_convert json2csv --in data/samples/people.json --out data/out/people_from_json.csv
python3 -m src.lab06.cli_convert csv2json --in data/samples/people.csv --out data/out/people_from_csv.json
python3 -m src.lab06.cli_convert csv2xlsx --in data/samples/people.csv --out data/out/people_from_csv.xlsx
```
Результаты работы сохранены в `data/out`.

## Справка

Флаги `-h` и `--help` выводят справку. Они доступны как для всей утилиты, так и для каждой подкоманды.

![ошибка](/images/lab06/cli_text_help.png)
![ошибка](/images/lab06/cat_help.png)
![ошибка](/images/lab06/stats_help.png)
![ошибка](/images/lab06/cli_convert_help.png)
![ошибка](/images/lab06/json2csv_help.png)
![ошибка](/images/lab06/csv2json_help.png)
![ошибка](/images/lab06/csv2xlsx_help.png)