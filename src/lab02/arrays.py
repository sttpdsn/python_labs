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


def flatten(mat: list[list | tuple]) -> list:
    result = []
    for row in mat:
        if not isinstance(row, (list, tuple)):
            raise TypeError("Все элементы должны быть списком или кортежем")
        result.extend(row)

    return result


def show_results(function, cases) -> None:
    for value in cases:
        try:
            result = function(value)
        except (ValueError, TypeError) as error:
            result = error

        print(f"{value} -> {result}")


if __name__ == "__main__":
    print("min_max:")
    show_results(min_max, [[3, -1, 5, 5, 0], [42], [-5, -2, -9], [], [1.5, 2, 2.0, -3.1]])

    print("\nunique_sorted:")
    show_results(unique_sorted, [[3, 1, 2, 1, 3], [], [-1, -1, 0, 2, 2], [1.0, 1, 2.5, 2.5, 0]])

    print("\nflatten:")
    show_results(flatten, [[[1, 2], [3, 4]], [[1, 2], (3, 4, 5)], [[1], [], [2, 3]], [[1, 2], "ab"]])
