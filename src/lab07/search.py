def linear_search(nums, x) -> int:
    """Индекс первого вхождения x или -1. Время O(n), память O(1)."""
    for i, value in enumerate(nums):
        if value == x:
            return i
    return -1


def binary_search(sorted_nums, x) -> int:
    """Индекс любого вхождения x или -1. Время O(log n), память O(1).
    Список должен быть отсортирован по возрастанию, на неотсортированном списке результат не определен."""
    lo, hi = 0, len(sorted_nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if sorted_nums[mid] == x:
            return mid
        if sorted_nums[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def two_sum_brute(nums, target) -> tuple[int, int] | None:
    """Пара (i, j), i < j, с нужной суммой или None. Время O(n**2), память O(1)."""
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return i, j
    return None


def two_sum_fast(nums, target) -> tuple[int, int] | None:
    """Любая подходящая пара за один проход. Время в среднем O(n), память O(n)."""
    seen = {}
    for j, value in enumerate(nums):
        complement = target - value
        if complement in seen:
            return seen[complement], j
        seen[value] = j
    return None
