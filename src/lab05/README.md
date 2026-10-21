# ЛР5 — JSON и конвертации (JSON↔CSV, CSV→XLSX)
## Сценарий 1: JSON -> CSV
```python
json_to_csv("data/samples/people.json", "data/out/people_from_json.csv")
json_to_csv("data/samples/people_empty.json", "data/out/people_empty_from_json.csv")
```
Функция проверяет наличие входного файла, расширения путей и корректность JSON, затем собирает названия столбцов из ключей объектов в порядке их первого появления. После этого записывает заголовок и данные в CSV в кодировке UTF-8, оставляя отсутствующие поля пустыми.
![пример со всеми данными](/images/lab05/people_from_json.png)
![пример с пропусками](/images/lab05/people_empty_from_json.png)

## Сценарий 2: CSV -> JSON
```python
csv_to_json("data/samples/people.csv", "data/out/people_from_csv.json")
```
Функция проверяет наличие входного файла, расширения путей, заголовок и наличие данных, затем читает CSV как список словарей, где ключи — названия столбцов, а значения — строки. Полученный список сохраняется в JSON в кодировке UTF-8 с сохранением кириллицы и отступами.
![пример](/images/lab05/people_from_csv.png)

## Сценарий 3: CSV -> XLSX
```python
csv_to_xlsx("data/samples/cities.csv", "data/out/cities_from_csv.xlsx")
```
Функция проверяет наличие входного файла, расширения путей и наличие данных, затем переносит строки CSV на лист Sheet1 новой книги Excel. Ширина каждого столбца устанавливается по длине самого длинного значения, но не менее 8, после чего книга сохраняется в XLSX.
![пример](/images/lab05/cities_from_csv.png)