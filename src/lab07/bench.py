import random
import timeit
from pathlib import Path

from src.lab04.io_txt_csv import write_csv
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort


def bench_sorts(n):
    data = [random.randint(-n, n) for _ in range(n)]
    rows = []
    for fn in (bubble_sort, insertion_sort, selection_sort, sorted):
        if n == 100_000 and fn is not sorted:
            # Ограничиваем размер для O(n**2), чтобы не ждать несколько минут.
            seconds = "пропуск: O(n**2)"
        else:
            seconds = timeit.timeit(lambda: fn(data), number=1)
        rows.append(("sort", n, fn.__name__, seconds))
    return rows


def bench_search():
    n = 100_000
    data = [random.randint(-n, n) for _ in range(n)]
    queries = [random.randint(-n, n) for _ in range(10_000)]
    seconds = timeit.timeit(lambda: sorted(data), number=1)
    rows = [("search", n, "sorted (подготовка)", seconds)]
    ordered = sorted(data)

    for fn, nums in ((linear_search, data), (binary_search, ordered)):
        def run_queries():
            for x in queries:
                fn(nums, x)

        seconds = timeit.timeit(run_queries, number=1)
        rows.append(("search", n, fn.__name__, seconds))
    return rows


def bench_two_sum(n):
    data = [random.randint(0, n) for _ in range(n)]
    # Два отрицательных числа в конце дают единственную подходящую пару.
    # Перебор дойдёт до конца, а не закончит случайно на первой паре.
    data[-2:] = [-1, -2]
    target = -3
    rows = []
    for fn in (two_sum_brute, two_sum_fast):
        seconds = timeit.timeit(lambda: fn(data, target), number=1)
        rows.append(("two_sum", n, fn.__name__, seconds))
    return rows


if __name__ == "__main__":
    random.seed(42)
    rows = []
    for n in (1_000, 10_000, 100_000):
        rows.extend(bench_sorts(n))
    rows.extend(bench_search())
    for n in (1_000, 10_000):
        rows.extend(bench_two_sum(n))

    print(f"{'task':<10} {'n':>7} {'impl':<24} {'seconds':>16}")
    for task, size, impl, seconds in rows:
        value = f"{seconds:.6f}" if isinstance(seconds, float) else seconds
        print(f"{task:<10} {size:>7} {impl:<24} {value:>16}")

    path = Path("data/lab07/bench.csv")
    path.parent.mkdir(parents=True, exist_ok=True)
    write_csv(rows, path, header=("task", "n", "impl", "seconds"))
    print(f"Результаты записаны в {path}")
