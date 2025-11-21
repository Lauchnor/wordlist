def num_letters(n_row,n_col):
    return n_col*2 + n_row*2 - 4

##---Part 3---##
import numpy as np
data = np.loadtxt("loop4.csv", delimiter=",", dtype=str, encoding='utf8')

words = []
rows, columns = data.shape

for c in range(columns):
    words.append(data[0, c])

for r in range(1, rows - 1):
    words.append(data[r, columns - 1])

for c in range(columns - 1, -1, -1):
    words.append(data[rows - 1, c])

for r in range(rows - 2, 0, -1):
    words.append(data[r, 0])

print(words)

assert len(words) == num_letters(rows, columns)


##---Part 4---##
