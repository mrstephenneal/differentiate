# Retrieve unique values from two nested lists.
from differentiate import diff


def nested():
    x = [[0, 1, 2, 3, 4],
         [5, 6, 7, 8, 9],
         [10, 11, 12, 13, 14]]
    y = [[5, 6, 7, 8, 9],
         [10, 11, 12, 13, 14],
         [15, 16, 17, 18, 19]]

    uniques = diff(x, y)
    print(uniques)  # [[15, 16, 17, 18, 19], [0, 1, 2, 3, 4]]
    return uniques


def flat():
    x = [0, 1, 2, 3, 4]
    y = [3, 4, 5, 6, 7]

    uniques = diff(x, y)
    print(uniques)  # [5, 6, 7]
    return uniques


def main():
    nested()
    flat()


if __name__ == '__main__':
    main()
