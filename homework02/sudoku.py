
def read_sudoku(filename):
    digits = [c for c in open(filename).read() if c in '123456789.']
    grid = group(digits, 9)
    return grid

def group(values, n):
    """
    >>> group([1,2,3,4], 2)
    [[1, 2], [3, 4]]
    >>> group([1,2,3,4,5,6,7,8,9], 3)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """

    if len(values) % n != 0:
        print("retard")
        quit()


    length = len(values)
    elemsInPart = len(values) // n

    return [ values[i*length // elemsInPart : (i+1)*length // elemsInPart] for i in range(elemsInPart)]

print(group([1,2,3,4,5,6,7,8,9], 3))
print("")
