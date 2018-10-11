# Retrieve unique values from two nested lists.
from differentiate import diff


x = [[0, 1, 2, 3, 4],
     [5, 6, 7, 8, 9],
     [10, 11, 12, 13, 14]]
y = [[5, 6, 7, 8, 9],
     [10, 11, 12, 13, 14],
     [15, 16, 17, 18, 19]]

uniques = diff(x, y)
print(uniques)  # [[15, 16, 17, 18, 19], [0, 1, 2, 3, 4]]
