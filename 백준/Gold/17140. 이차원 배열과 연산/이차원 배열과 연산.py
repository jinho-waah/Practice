import sys
input = sys.stdin.readline
from collections import Counter

def r_operation(matrix):
    max_col_size = 0
    new_matrix = []

    for row in matrix:
        counter = Counter(row)
        if 0 in counter:
            del counter[0]  # Ignore zeros
        sorted_items = sorted(counter.items(), key=lambda x: (x[1], x[0]))  # Sort by frequency, then by number
        new_row = []
        for num, freq in sorted_items:
            new_row.extend([num, freq])
        max_col_size = max(max_col_size, len(new_row))
        new_matrix.append(new_row)

    # Pad rows with zeros to make them the same length
    for row in new_matrix:
        row.extend([0] * (max_col_size - len(row)))

    return new_matrix

def c_operation(matrix):
    transposed = list(zip(*matrix))  # Transpose the matrix
    transposed_result = r_operation(transposed)  # Perform R operation on the transposed matrix
    return [list(row) for row in zip(*transposed_result)]  # Transpose back

def solve(r, c, k, initial_matrix):
    time = 0

    while time <= 100:
        # Check if the target cell has the desired value
        if r - 1 < len(initial_matrix) and c - 1 < len(initial_matrix[0]) and initial_matrix[r - 1][c - 1] == k:
            return time

        # Determine whether to apply R or C operation
        if len(initial_matrix) >= len(initial_matrix[0]):  # Apply R operation
            initial_matrix = r_operation(initial_matrix)
        else:  # Apply C operation
            initial_matrix = c_operation(initial_matrix)

        # Trim the matrix to 100x100 if necessary
        if len(initial_matrix) > 100:
            initial_matrix = initial_matrix[:100]
        if len(initial_matrix[0]) > 100:
            initial_matrix = [row[:100] for row in initial_matrix]

        time += 1

    return -1

# 입력 처리 및 실행
r, c, k = map(int, input().split())
initial_matrix = [list(map(int, input().split())) for _ in range(3)]

print(solve(r, c, k, initial_matrix))
