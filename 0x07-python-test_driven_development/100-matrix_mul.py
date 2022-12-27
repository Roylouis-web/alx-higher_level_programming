#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    """
    param m_a: first list parameter
    param m_b: second list parameter
    return: the result multiplication of
            the two matrices
             """
    m_a_elem = "m_a should contain only integers or floats"
    m_b_elem = "m_b should contain only integers or floats"
    if isinstance(m_a, list):
        if not m_a:
            raise ValueError("m_a can't be empty")
        is_nested = all(isinstance(i, list) for i in m_a)
        if not is_nested:
            raise TypeError("m_a must be a list of lists")
        i = 0

        while i < len(m_a):
            len1 = len(m_a[i])
            if not m_a[i]:
                raise ValueError("m_a can't be empty")
            if i + 1 < len(m_a):
                len2 = len(m_a[i + 1])
                if len1 != len2:
                    raise TypeError("each row of m_a must be of the same size")
            j = 0
            while j < len(m_a[0]):
                if not isinstance(m_a[i][j], (int, float)):
                    raise TypeError(m_a_elem)
                elif isinstance(m_a[i][j], bool):
                    raise TypeError(m_a_elem)
                j += 1
            i += 1
    else:
        raise TypeError("m_a must be a list")

    if isinstance(m_b, list):
        if not m_b:
            raise ValueError("m_b can't be empty")
        is_nested = all(isinstance(i, list) for i in m_b)
        if not is_nested:
            raise TypeError("m_b must be a list of lists")
        i = 0

        while i < len(m_b):
            len1 = len(m_b[i])
            if not m_b[i]:
                raise ValueError("m_b can't be empty")
            if i + 1 < len(m_b):
                len2 = len(m_b[i + 1])
                if len1 != len2:
                    raise TypeError("each row of m_b must be of the same size")
            j = 0
            while j < len(m_b[i]):
                if not isinstance(m_b[i][j], (int, float)):
                    raise TypeError(m_b_elem)
                elif isinstance(m_b[i][j], bool):
                    raise TypeError(m_b_elem)
                j += 1
            i += 1
    else:
        raise TypeError("m_b must be a list")
    len_of_row = 0
    result = [[0 for j in range(len(m_b[0]))] for i in range(len(m_a))]
    for i in m_b:
        len_of_row += 1

    if len(m_a[0]) == len_of_row:
        for i in range(len(m_a)):
            for j in range(len(m_b[0])):
                for k in range(len(m_b)):
                    result[i][j] += m_a[i][k] * m_b[k][j]
    else:
        raise ValueError("m_a and m_b can't be multiplied")
    return result
