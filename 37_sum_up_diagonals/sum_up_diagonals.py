def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    diagonal1 = 0
    diagonal2 = 0
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if i == j:
                diagonal1 += matrix[i][j]
            if i + j == n - 1:
                diagonal2 += matrix[i][j]
    return diagonal1 + diagonal2
