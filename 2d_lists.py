matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix)

#iterating thro the elements
for row in matrix:
    for item in  row:
        print(item)


#for efficiency and large data sets
from itertools import chain

# Flattening the matrix and iterating through it
for item in chain.from_iterable(matrix):
    print(item)
