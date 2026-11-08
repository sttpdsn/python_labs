import random

from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort

SORTS = (bubble_sort, insertion_sort, selection_sort)


def check_sorting(fn, trials=100) -> int:
    count = 0
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        original = nums[:]
        result = fn(nums)
        assert result == sorted(original), f"{fn.__name__}: {original}, результат {result}"
        assert nums == original, f"{fn.__name__} изменила список {original}"
        count += 1
    return count


def check_search() -> int:
    count = 0
    for trial in range(100):
        n = trial if trial < 3 else random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        sorted_nums = sorted(nums)
        queries = [random.randint(-100, 100), 101]
        if sorted_nums:
            queries.extend([sorted_nums[0], sorted_nums[-1]])
        else:
            queries.extend([0, -101])

        for x in queries:
            try:
                expected = nums.index(x)
            except ValueError:
                expected = -1
            result = linear_search(nums, x)
            assert result == expected, f"linear_search: {nums}, x={x}, результат {result}"
            count += 1

            try:
                expected = sorted_nums.index(x)
            except ValueError:
                expected = -1
            result = binary_search(sorted_nums, x)
            if expected == -1:
                assert result == -1, f"binary_search: {sorted_nums}, x={x}, результат {result}"
            else:
                assert 0 <= result < len(sorted_nums), f"binary_search: {sorted_nums}, x={x}, индекс {result}"
                assert sorted_nums[result] == x, f"binary_search: {sorted_nums}, x={x}, индекс {result}"
            count += 1
    return count


def check_two_sum(trials=100) -> int:
    count = 0
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        target = random.randint(-200, 200)
        brute = two_sum_brute(nums, target)
        fast = two_sum_fast(nums, target)
        assert (brute is None) == (fast is None), f"{nums}, target={target}: {brute}, {fast}"

        for pair in (brute, fast):
            if pair is not None:
                i, j = pair
                assert 0 <= i < j < len(nums), f"{nums}, target={target}, пара {pair}"
                assert nums[i] + nums[j] == target, f"{nums}, target={target}, пара {pair}"
            count += 1
    return count


def run_checks() -> int:
    random.seed(42)
    total = 0
    for fn in SORTS:
        total += check_sorting(fn)
    total += check_search()
    total += check_two_sum()
    return total


if __name__ == "__main__":
    print(f"OK: {run_checks()} проверок")
