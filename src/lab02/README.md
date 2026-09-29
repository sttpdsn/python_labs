# ЛР2 — Коллекции и матрицы
## arrays.py
### min_max
```
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        raise ValueError("Список не должен быть пустым")

    minimum = nums[0]
    maximum = nums[0]
    for num in nums:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num

    return minimum, maximum
```
Функция проверяет, не пустой ли список, циклом находит наименьший и наибольший элементы, выводит их кортежем.
![Пример работы функции](/images/lab02/min_max.png)

### unique_sorted
```
def unique_sorted(nums: list[float | int]) -> list[float | int]:
    for num in nums:
      if not isinstance(num, (int, float)):
          raise TypeError("Все элементы списка должны быть числами")
          
    result = list(set(nums))

    for i in range(len(result)):
        for j in range(i + 1, len(result)):
            if result[j] < result[i]:
                result[i], result[j] = result[j], result[i]

    return result
```
Функция проверяет, состоит ли список из чисел (int или float), после убирает повторы созданием множества и обратным превращением в список, затем сортирует пузырьком.
![Пример работы функции unique_sorted](/images/lab02/unique_sorted.png)

### flatten
```
def flatten(mat: list[list | tuple]) -> list:
    result = []
    for row in mat:
        if not isinstance(row, (list, tuple)):
            raise TypeError("Все элементы должны быть списком или кортежем")
        result.extend(row)

    return result
```
Функция проверяет, является ли каждый элемент полученного списка списком или кортежем, и расширяет выходной список каждым из них.
![Пример работы функции flatten](/images/lab02/flatten.png)

## matrix.py
### transpose
```
def transpose(mat: list[list[float | int]]) -> list[list]:
    check_matrix(mat)

    if not mat:
        return []

    result = []
    for col_index in range(len(mat[0])):
        new_row = []
        for row in mat:
            new_row.append(row[col_index])
        result.append(new_row)

    return result
```
Функция проверяет, является ли список списков правильной матрицей (квадратной или прямоугольной), затем для каждого столбца создает новую строку, в которую добавляет элементы из каждой строки с этим номером, строки сохраняются в списке result.
![Пример работы функции transpose](/images/lab02/transpose.png)

### row_sums
```
def row_sums(mat: list[list[float | int]]) -> list[float]:
    check_matrix(mat)
    return [sum(row) for row in mat]
```
Функция проверяет правильность матрицы и возвращает генератор с суммой для каждой строки в матрице.
![Пример работы функции row_sums](/images/lab02/row_sums.png)

### col_sums
```
def col_sums(mat: list[list[float | int]]) -> list[float]:
    return row_sums(transpose(mat))
```
Функция вызывает row_sums от транспонированной матрицы, что возвращает сумму по столбцам. (Функция row_sums проверяет правильность матрицы).
![Пример работы функции col_sums](/images/lab02/col_sums.png)

## tuples.py
### format_record
```
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
```
Функция проверяет ФИО, группу и GPA на правильность и при правильных данных выводит фамилию с заглавной и склеенные инициалы, группу и GPA с точностью до двух знаков после запятой.
![Пример работы функции format_record](/images/lab02/format_record.png)
