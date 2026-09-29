def check_matrix(mat: list[list[float | int]]) -> None:
    for row in mat:
        if not isinstance(row, list):
            raise TypeError("Каждая строка матрицы должна быть списком")

    if mat:
        row_length = len(mat[0])
        for row in mat:
            if len(row) != row_length:
                raise ValueError("Матрица должна быть прямоугольной")


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


def row_sums(mat: list[list[float | int]]) -> list[float]:
    check_matrix(mat)
    return [sum(row) for row in mat]


def col_sums(mat: list[list[float | int]]) -> list[float]:
    return row_sums(transpose(mat))


def show_results(function, cases) -> None:
    for value in cases:
        try:
            result = function(value)
        except (ValueError, TypeError) as error:
            result = error

        print(f"{value} -> {result}")


if __name__ == "__main__":
    print("transpose:")
    show_results(transpose, [[[1, 2, 3]], [[1], [2], [3]], [[1, 2], [3, 4]], [], [[1, 2], [3]]])

    print("\nrow_sums:")
    show_results(row_sums, [[[1, 2, 3], [4, 5, 6]], [[-1, 1], [10, -10]], [[0, 0], [0, 0]], [[1, 2], [3]]])

    print("\ncol_sums:")
    show_results(col_sums, [[[1, 2, 3], [4, 5, 6]], [[-1, 1], [10, -10]], [[0, 0], [0, 0]], [[1, 2], [3]]])
