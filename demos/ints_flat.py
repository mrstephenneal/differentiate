# Retreive  unique values from two flat lists.
from differentiate import diff


x = [0, 1, 2, 3, 4]
y = [3, 4, 5, 6, 7]

uniques = diff(x, y)
print(uniques)  # [5, 6, 7]
