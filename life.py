import time


class Cell:
    def __init__(self, x, y, empty=False):
        self.x = x
        self.y = y
        self.empty = empty

    def __str__(self):
        return '[' + str(self.x) + ',' + str(self.y) + ']'


class World:
    MAX_X = 500
    MAX_Y = 500
    OFFSET = 200

    def __init__(self, figure_a, figure_b, figure_x_offset, figure_y_offset):
        self.field = [[] for i in range(World.MAX_X)]
        # extending field
        for y in range(World.MAX_Y):
            for x in range(World.MAX_X):
                self.field[x].append(Cell(x, y, True))

        self.potential_changes = set()
        for x in range(len(figure_a)):
            for y in range(len(figure_a[0])):
                is_empty = (figure_a[x][y] == '-')
                cell = Cell(x + World.OFFSET, y + World.OFFSET, is_empty)
                self.field[x + World.OFFSET][y + World.OFFSET] = cell
                if not is_empty:
                    self.potential_changes.add(cell)
                    self.potential_changes.update(self.get_neighbour_set(cell))

        for x in range(len(figure_b)):
            for y in range(len(figure_b[0])):
                is_empty = (figure_b[x][y] == '-')
                cell = Cell(x + World.OFFSET + figure_x_offset, y + World.OFFSET + figure_y_offset, is_empty)
                self.field[x + World.OFFSET + figure_x_offset][y + World.OFFSET + figure_y_offset] = cell
                if not is_empty:
                    self.potential_changes.add(cell)
                    self.potential_changes.update(self.get_neighbour_set(cell))

        self.prev_gen_cell_number = 0
        self.unchanged_gen = 0

    def do_iteration(self):
        born_cells = []
        died_cells = []
        for cell in self.potential_changes:
            neighbour_count = self.neighbour_count_of(cell)
            if cell.empty:
                if neighbour_count == 3:
                    born_cells.append(cell)
            elif neighbour_count < 2 or neighbour_count > 3:
                died_cells.append(cell)

        self.potential_changes.clear()
        for c in died_cells:
            died_cell = Cell(c.x, c.y, True)
            self.field[c.x][c.y] = died_cell
            self.potential_changes.add(died_cell)
            self.potential_changes.update(self.get_neighbour_set(died_cell))

        for c in born_cells:
            born_cell = Cell(c.x, c.y)
            self.field[c.x][c.y] = born_cell
            self.potential_changes.add(born_cell)
            self.potential_changes.update(self.get_neighbour_set(born_cell))

        current_cell_count = self.live_cell_count()
        if current_cell_count == self.prev_gen_cell_number:
            self.unchanged_gen += 1
        else:
            self.unchanged_gen = 0
        self.prev_gen_cell_number = current_cell_count

    def neighbour_count_of(self, cell):
        result = 0
        x = cell.x
        y = cell.y

        if not self.is_empty_cell(x - 1, y):
            result += 1
        if not self.is_empty_cell(x - 1, y + 1):
            result += 1
        if not self.is_empty_cell(x, y + 1):
            result += 1
        if not self.is_empty_cell(x + 1, y + 1):
            result += 1
        if not self.is_empty_cell(x + 1, y):
            result += 1
        if not self.is_empty_cell(x + 1, y - 1):
            result += 1
        if not self.is_empty_cell(x, y - 1):
            result += 1
        if not self.is_empty_cell(x - 1, y - 1):
            result += 1

        return result

    def get_neighbour_set(self, cell):
        result = set()
        x = cell.x
        y = cell.y
        neighbours = [(x - 1, y), (x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x + 1, y), (x + 1, y + 1), (x, y + 1), (x - 1, y + 1)]
        for (x, y) in neighbours:
            norm_x, norm_y = World.normalize_coordinates(x, y)
            result.add(self.field[norm_x][norm_y])
        return result

    def is_empty_cell(self, x, y):
        x, y = World.normalize_coordinates(x, y)
        return self.field[x][y].empty is True

    @staticmethod
    def normalize_coordinates(x, y):
        resulted_x = x
        resulted_y = y
        if x < 0:
            resulted_x = World.MAX_X - 1
        elif x >= World.MAX_X:
            resulted_x = 0
        if y < 0:
            resulted_y = World.MAX_Y - 1
        elif y >= World.MAX_Y:
            resulted_y = 0
        return resulted_x, resulted_y

    def __str__(self):
        resulted_lines = []
        for y in range(World.MAX_Y):
            x_elements = []
            for x in range(World.MAX_X):
                x_elements.append('-' if self.field[x][y].empty else 'X')
            resulted_lines.append(' '.join(x_elements))
        return '\n'.join(resulted_lines)

    def live_cell_count(self):
        result = 0
        for i in range(World.MAX_X):
            for j in range(World.MAX_Y):
                if not self.field[i][j].empty:
                    result += 1
        return result


if __name__ == '__main__':
    lines = [[] for i in range(5)]

    glider = [['-', '-', 'X'], ['X', '-', 'X'], ['-', 'X', 'X']]
    acorn = [['-', '-', 'X'], ['X', '-', 'X'], ['-', '-', '-'], ['-', 'X', '-'], ['-', '-', 'X'], ['-', '-', 'X'],
              ['-', '-', 'X']]

    with open('/home/ipatrikeev/dev/input.txt') as f:
        x_offset, y_offset = [int(x) for x in f.readline().split()]

    world = World(acorn, glider, x_offset, y_offset * -1)
    iter_count = 0
    while True:
        world.do_iteration()
        iter_count += 1
        print(str(iter_count) + ' : ' + str(world.unchanged_gen))
        if world.unchanged_gen >= 5:
            break

    print(iter_count, world.live_cell_count())
