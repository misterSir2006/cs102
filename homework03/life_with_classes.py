import pygame
import random
from pygame.locals import *
from pprint import pprint as pp
from copy import deepcopy


class Cell:
    def __init__(self, row: int, col: int, state=0):
        self.alive = state
        self.row = row
        self.col = col

    def is_alive(self) -> bool:
        return self.alive


class CellList:
    def __init__(self, nrows: int, ncols: int, randomize=True):
        self.nrows = nrows
        self.ncols = ncols
        if randomize:
            self.grid = [[Cell(i, j, random.randint(0, 1))
                          for j in range(ncols)]
                         for i in range(nrows)]
        else:
            self.grid = [[Cell(i, j, 0)
                          for j in range(ncols)]
                         for i in range(nrows)]

    def get_neighbours(self, cell: Cell) -> list:
        neighbours = []
        x, y = cell.row, cell.col
        n = self.nrows - 1
        m = self.ncols - 1
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if not (0 <= i <= n and 0 <= j <= m) or (i == x and j == y):
                    continue
                neighbours.append(self.grid[i][j])

        return neighbours

    def update(self):
        new_grid = deepcopy(self.grid)
        for cell in self:
            neighbours = self.get_neighbours(cell)
            cnt = sum(c.is_alive() for c in neighbours)
            if cell.is_alive():
                if cnt < 2 or cnt > 3:
                        new_grid[cell.row][cell.col].alive = 0
            else:
                if cnt == 3:
                    new_grid[cell.row][cell.col].alive = 1

        self.grid = new_grid
        return self

    @classmethod
    def from_file(cls, filename: str):
        grid = []
        with open(filename) as f:
            for i, line in enumerate(f):
                grid.append([Cell(i, j, int(c))
                             for j, c in enumerate(line) if c in '01'])
        clist = cls(len(grid), len(grid[0]), False)
        clist.grid = grid
        return clist

    def __iter__(self):
        self.i_cnt, self.j_cnt = 0, 0
        return self

    def __next__(self):
        if (self.i_cnt == self.nrows):
            raise StopIteration

        cell = self.grid[self.i_cnt][self.j_cnt]
        self.j_cnt += 1
        if self.j_cnt == self.ncols:
            self.i_cnt += 1
            self.j_cnt = 0

        return cell

    def __str__(self):
        str = ""
        for i in range(self.nrows):
            for j in range(self.ncols):
                if (self.grid[i][j].alive):
                    str += '1 '
                else:
                    str += '0 '
            str += '\n'
        return str


class GameOfLife:
    def __init__(self, width=640, height=480, cell_size=10, speed=10):
        self.width = width
        self.height = height
        self.cell_size = cell_size

        # Устанавливаем размер окна
        self.screen_size = width, height
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

        # Вычисляем количество ячеек по вертикали и горизонтали
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        # Скорость протекания игры
        self.speed = speed

    def draw_grid(self):
        """ Отрисовать сетку """
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                             (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                             (0, y), (self.width, y))

    def run(self):
        """ Запустить игру """
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))

        # Создание списка клеток
        clist = CellList(self.cell_width, self.cell_height, True)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            self.draw_grid()

            self.draw_cell_list(clist)
            clist = CellList.update(clist)

            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()

    def draw_cell_list(self, clist) -> None:

        for cell in clist:

            color_cell = pygame.Color('white')

            if cell.is_alive():
                color_cell = pygame.Color('green')

            rect = Rect(cell.row * self.cell_size+1, cell.col * self.cell_size+1, self.cell_size-1, self.cell_size-1)
            pygame.draw.rect(self.screen, color_cell, rect)


if __name__ == '__main__':
    game = GameOfLife(320, 240, 20)
    game.run()

