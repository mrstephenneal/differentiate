class Differentiate:
    def __init__(self, x, y):
        """
        Retrieve a unique of list of elements that do not exist in both x and y.
        Capable of parsing one-dimensional (flat) and two-dimensional (lists of lists) lists.

        Steps:
            1. Retrieve input existing data types
            2. Transform x and y inputs into sequences of unique, immutable values
            3. Create set if values found in both x and y

        :param x: list #1
        :param y: list #2
        :return: list of unique values
        """
        self._input_type = None
        self._x = x
        self._y = y
        self._x_set = self._transform(x)
        self._y_set = self._transform(y)
        self._uniques = self._get_uniques()

    @property
    def uniques(self):
        return self._uniques

    @property
    def uniques_x(self):
        return [self._input_type(i) for i in self._uniques if self._input_type(i) in self._x]

    @property
    def uniques_y(self):
        return [self._input_type(i) for i in self._uniques if self._input_type(i) in self._y]

    def _get_uniques(self):
        # Generate set of non-shared values and return list of values in original type
        uniques = {i for i in self._y_set if i not in self._x_set}

        # Add unique elements from shorter list
        for i in self._x_set:
            if i not in self._y_set:
                uniques.add(i)
        return uniques

    def _transform(self, data):
        # Convert dictionaries to lists of tuples
        if isinstance(data, dict):
            data = list(data.items())

        # Get the input type to convert back to before return
        input_type = type(data[0])
        if self._input_type != input_type:
            self._input_type = input_type

        # Immutable and Unique - Convert list of tuples into set of tuples
        if input_type not in (str, int, float):
            return set(map(tuple, data))

        # Unique values only
        else:
            return set(data)


def diff(x, y, x_only=False, y_only=False):
    """Wrapper function for Differentiate class"""
    d = Differentiate(x, y)

    # Return unique values from x, y or both
    if x_only:
        return d.uniques_x
    elif y_only:
        return d.uniques_y
    else:
        return d.uniques


def differentiate(x, y):
    """Wrapper function for legacy imports of differentiate."""
    return diff(x, y)


def main():
    from argparse import ArgumentParser

    # Declare argparse argument descriptions
    usage = 'Compare two files text files and retrieve unique values'
    description = 'Compare two data sets or more (text files or lists/sets) and return the unique elements that are ' \
                  'found in only one data set.'
    helpers = {
        'files': "Input two text file paths",
    }

    # construct the argument parse and parse the arguments
    ap = ArgumentParser(usage=usage, description=description)
    ap.add_argument('files', help=helpers['files'], nargs='+')
    args = vars(ap.parse_args())

    data = []
    # Read each text file
    for tf in args['files']:
        with open(tf, 'r') as f:
            # Remove whitespace and \n
            data.append([l.strip() for l in f.readlines()])

    # Run differentiate
    d = diff(data[0], data[1])
    print('\nUnique Items ({}):\n-------------------'.format(len(d)))
    for i in d:
        print(i)


if __name__ == '__main__':
    main()
