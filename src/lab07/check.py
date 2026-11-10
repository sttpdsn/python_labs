import random

from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort


EDGE_CASES = [[], [5], [2, 1], [1, 2, 3], [3, 2, 1], [2, 2, -1]]


def make_cases(trials):
    """Особые случаи и trials случайных списков."""
    cases = [list(nums) for nums in EDGE_CASES]
    for _ in range(trials):
        n = random.randint(0, 50)
        cases.append([random.randint(-100, 100) for _ in range(n)])
    return cases


def check_sorting(fn, trials=100):
    for nums in make_cases(trials):
        original = list(nums)
        result = fn(nums)
        message = f"{fn.__name__}: список {original}, результат {result}"
        assert result == sorted(original), message
        assert nums == original, f"Изменён исходный список: {message}"
        assert result is not nums, f"Не создан новый список: {message}"


def check_search():
    for nums in make_cases(100):
        ordered = sorted(nums)
        targets = [random.randint(-100, 100), -101, 101]
        if nums:
            targets.extend([ordered[0], ordered[-1]])
        for x in targets:
            try:
                expected = nums.index(x)
            except ValueError:
                expected = -1
            result = linear_search(nums, x)
            assert result == expected, f"linear_search: {nums}, x={x}, ответ {result}"

            try:
                expected = ordered.index(x)
            except ValueError:
                expected = -1
            result = binary_search(ordered, x)
            message = f"binary_search: {ordered}, x={x}, ответ {result}"
            if expected == -1:
                assert result == -1, message
            else:
                # При повторах индекс может отличаться от list.index.
                assert 0 <= result < len(ordered), message
                assert ordered[result] == x, message


def check_two_sum(trials=100):
    for nums in make_cases(trials):
        targets = [random.randint(-200, 200), -201, 201]
        if len(nums) >= 2:
            targets.append(nums[0] + nums[1])
        for target in targets:
            brute = two_sum_brute(nums, target)
            fast = two_sum_fast(nums, target)
            message = f"Two Sum: {nums}, target={target}, brute={brute}, fast={fast}"
            assert (brute is None) == (fast is None), message
            for pair in (brute, fast):
                if pair is not None:
                    assert len(pair) == 2, message
                    i, j = pair
                    assert 0 <= i < j < len(nums), message
                    assert nums[i] + nums[j] == target, message


if __name__ == "__main__":
    random.seed(42)
    trials = 100
    for fn in (bubble_sort, insertion_sort, selection_sort):
        check_sorting(fn, trials)
    check_search()
    check_two_sum(trials)
    # Проверка - один список для одной сортировки, поиска или Two Sum.
    total = 5 * (trials + len(EDGE_CASES))
    print(f"OK: {total} проверок")
