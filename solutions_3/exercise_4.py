m = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

identity_matrix = [[1 if i == j else 0 for j in range(len(m))] for i in range(len(m))]

for row in identity_matrix:
    print(row)
