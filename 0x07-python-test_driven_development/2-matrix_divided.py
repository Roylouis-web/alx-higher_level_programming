#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    :param matrix: matrix to be passed as parameter
    :param div: divisor of each element of the matrix
    :return: a new matrix
    """
    row1 = "Each row of the matrix"
    row2 = "must have the same size"
    element1 = "matrix must be a matrix"
    element2 = "(list of lists) of integers/floats"
    new = matrix.copy()
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    i = 0
    while i < len(new):
        len1 = len(new[i])
        if i + 1 < len(new):
            len2 = len(new[i + 1])

            if len1 != len2:
                raise TypeError(f"{row1} {row2}")
        i += 1

    for j in new:
        for k in j:
            if not isinstance(k, (int, float)):
                raise TypeError(f"{element1} {element2}")

    return [[round(x/div, 2) for x in l] for l in new]
