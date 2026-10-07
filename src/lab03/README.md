# ЛР3 — Тексты и частоты слов
## text.py
### normalize
```python
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    text = text.casefold() if casefold else text.lower()
    if yo2e:
        text = text.replace("ё", "е").replace("Ё", "Е")
    text = "".join(" " if unicodedata.category(char) == "Cc" else char for char in text)
    return " ".join(text.split())
```
Функция применяет casefold или lower (в зависимости от флага при запуске, по умолчанию - casefold) на строук, затем заменяет ё на е при (также в зависимости от флага, по умолчанию он активирован), далее проходит по списку и заменяет управляющие символы юникода на пробелы, собирает через join, потом убирает лишние пробелы, собирая список из слов через пробел с помощью join.
![Примеры](/images/lab03/normalize.png)

### tokenize
```python
def tokenize(text: str) -> list[str]:
    return re.findall(r"\w+(?:-\w+)*", text)
```
Функция проходит по строке регулярным выражением и возвращает все совпадения.
![Примеры](/images/lab03/tokenize.png)

### count_freq
```python
def count_freq(tokens: list[str]) -> dict[str, int]:
    freq: dict[str, int] = {}
    for token in tokens:
        freq[token] = freq.get(token, 0) + 1
    return freq
```
Функция заводит словарь с ключом - словом и значением - количеством вхождений. Метод get при отсутствии в словаре ранее присваивает значение 0 и не бросает ошибку.

### top_n
```python
def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda item: (-item[1], item[0]))[:n]
```
Функция сортирует список элементов словаря по ключу - сначала по убыванию количества вхождений, затем по алфавиту значения. Затем делает срез до n штук, переданных при запуске функции.
![Пример](/images/lab03/count_freq_top_n.png)

## text_stats.py
```python
from text import count_freq, normalize, tokenize, top_n
import sys

def main() -> None:
    tokens = tokenize(normalize(sys.stdin.read()))
    freq = count_freq(tokens)

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")
    for word, count in top_n(freq):
        print(f"{word}:{count}")

if __name__ == "__main__":
    main()
```
Функция принимает stdin, затем нормализует и токенизует его, создает словарь частоты вхождения. Для количества слов выводит длину списка токенов, для уникальных - длину словаря с частотой вхождений, потом с помощью цикла for построчно выводит топ-5 слов из списка top_n.
