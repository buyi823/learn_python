#!/usr/bin/python3
print([str(round(355/113, i)) for i in range(1,6)])

matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
]
print(matrix)
print([[row[i] for row in matrix] for i in range(4)])

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

print(transposed)