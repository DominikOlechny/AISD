matrix = [
    [5, 4, 7],
    [2, 9, 3],
    [1, 8, 6]
]

for row in matrix:
    min_val = row[0]
    min_index = 0
    for i in range(1, len(row)):
        if row[i] < min_val:
            min_val = row[i]
            min_index = i
    row[0], row[min_index] = row[min_index], row[0]

print(matrix)