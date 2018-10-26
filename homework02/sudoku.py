#!/usr/bin/env python
# -*- coding: utf-8 -*-

def group(values, n):
    """
    >>> group([1,2,3,4], 2)
    [[1, 2], [3, 4]]
    >>> group([1,2,3,4,5,6,7,8,9], 3)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """

    if len(values) % n != 0:
        print("u = retard")
        quit()

    length = len(values)
    elemsInPart = len(values) // n

    return [ values[i*length // elemsInPart : (i+1)*length // elemsInPart] for i in range(elemsInPart)]



def read_sudoku(filename):
    digits = [c for c in open(filename).read() if c in '123456789.']
    grid = group(digits, 9)
    return grid



def display(values):
    width = 2
    line = '+'.join(['-' * (width * 3)] * 3)
    for row in range(9):
        print(''.join(values[row][col].center(width) + ('|' if str(col) in '25' else '') for col in range(9)))
        if str(row) in '25':
            print(line)
    print()



def get_row(values, pos):
    """ Возвращает все значения для номера строки, указанной в pos
    >>> get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '2', '.']
    >>> get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
    ['4', '.', '6']
    >>> get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
    ['.', '8', '9']
    """
    gridGovna = read_sudoku("puzzle1.txt")
    rowNumber, colNumber = pos

    row = gridGovna[rowNumber] 
    return row
gridGovna = read_sudoku("puzzle1.txt")
print (get_row(gridGovna, (8, 0)))



def get_col(values, pos):
    """ Возвращает все значения для номера столбца, указанного в pos
    >>> get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '4', '7']
    >>> get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1))
    ['2', '.', '8']
    >>> get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2))
    ['3', '6', '9']
    """
    gridGovna = read_sudoku("puzzle1.txt")
    rowNumber, colNumber = pos
    col = []

    for i in range(9):
        col.append(gridGovna[i][colNumber])
    return col
print(get_col(gridGovna, (0, 0)))




def get_block(values, pos):
    """ Возвращает все значения из квадрата, в который попадает позиция pos
    >>> grid = read_sudoku('puzzle1.txt')
    >>> get_block(grid, (0, 1))
    ['5', '3', '.', '6', '.', '.', '.', '9', '8']
    >>> get_block(grid, (4, 7))
    ['.', '.', '3', '.', '.', '1', '.', '.', '6']
    >>> get_block(grid, (8, 8))
    ['2', '8', '.', '.', '.', '5', '.', '7', '9']
    """
    row, col = pos
    blockList = []
    if (row == 0 or row == 1 or row == 2)  and (col == 0 or col == 1 or col == 2):
        blockList = (gridGovna[0][0:3] + gridGovna[1][0:3] + gridGovna[2][0:3])
        
    elif (row == 3 or row == 4 or row == 5) and (col == 0 or col == 1 or col == 2):
        blockList = (gridGovna[0][3:6] + gridGovna[1][3:6] + gridGovna[2][3:6])
        
    elif (row == 6 or row == 7 or row == 8) and (col == 0 or col == 1 or col == 2):
        blockList = (gridGovna[0][6:9] + gridGovna[1][6:9] + gridGovna[2][6:9])
        
    elif (row == 0 or row == 1 or row == 2) and (col == 3 or col == 4 or col == 5):
        blockList = (gridGovna[3][0:3] + gridGovna[4][0:3] + gridGovna[5][0:3])

    elif (row == 3 or row == 4 or row == 5) and (col == 3 or col == 4 or col == 5):
        blockList = (gridGovna[3][3:6] + gridGovna[4][3:6] + gridGovna[5][3:6])

    elif (row == 6 or row == 7 or row == 8) and (col == 3 or col == 4 or col == 5):
        blockList = (gridGovna[3][6:9] + gridGovna[4][6:9] + gridGovna[5][6:9])
  
    elif (row == 0 or row == 1 or row == 2) and (col == 6 or col == 7 or col == 8):
        blockList = (gridGovna[6][0:3] + gridGovna[7][0:3] + gridGovna[8][0:3])
 
    elif (row == 3 or row == 4 or row == 5) and (col == 6 or col == 7 or col == 8):
        blockList = (gridGovna[6][3:6] + gridGovna[7][3:6] + gridGovna[8][3:6])
        
    elif (row == 6 or row == 7 or row == 8) and (col == 6 or col == 7 or col == 8):
        blockList = (gridGovna[6][6:9] + gridGovna[7][6:9] + gridGovna[8][6:9])
        
    return blockList

print(get_block(gridGovna, (8, 6)))


def find_empty_positions(grid):
    """ Найти первую свободную позицию в пазле
    
    >>> find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
    (0, 2)
    >>> find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
    (1, 1)
    >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
    (2, 0)
    """
    for i in range(len(gridGovna)):
        for j in range(len(gridGovna)):
             if gridGovna[i][j] == '.':
                 return i, j

print("\n")
print(find_empty_positions(gridGovna))


