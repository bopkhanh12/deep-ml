def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
    if not a or not a[0] or not b:
        return []
    num_rows = len(a)
    num_cols = len(a[0])
    if num_cols != len(b):
        return -1
    arr = []
    for i in range(num_rows):
        row_dot = 0.0
        for j in range(num_cols):
            row_dot += a[i][j] * b[j]
        arr.append(row_dot)
    return arr