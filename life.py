import time


class World:
    MAX_X = 10000
    MAX_Y = 10000
    OFFSET = 5000
    CELL = 'X'

    def __init__(self, figure_a, figure_b, figure_x_offset, figure_y_offset):
        self.life_cell_count = 0
        self.field = [[] for i in range(World.MAX_X)]
        for x in range(World.MAX_X):
            self.field[x].extend([None] * World.MAX_Y)

        self.potential_changes = set()
        for x in range(len(figure_a)):
            for y in reversed(range(len(figure_a[0]))):
                is_empty = (figure_a[x][y] == '-')
                if not is_empty:
                    cell_x = x + World.OFFSET
                    cell_y = y + World.OFFSET
                    self.field[cell_x][cell_y] = World.CELL
                    self.potential_changes.add((cell_x, cell_y))
                    self.potential_changes.update(self.get_neighbours(cell_x, cell_y))
                    self.life_cell_count += 1

        for x in range(len(figure_b)):
            for y in reversed(range(len(figure_b[x]))):
                is_empty = (figure_b[x][y] == '-')
                if not is_empty:
                    cell_x = x + World.OFFSET + figure_x_offset - (len(figure_b) - 1)
                    cell_y = y + World.OFFSET + figure_y_offset
                    self.field[cell_x][cell_y] = World.CELL
                    self.potential_changes.add((cell_x, cell_y))
                    self.potential_changes.update(self.get_neighbours(cell_x, cell_y))
                    self.life_cell_count += 1

        self.prev_gen_cell_number = 0
        self.unchanged_gen = 0

    def do_iteration(self):
        born_cells = []
        died_cells = []
        for (x, y) in self.potential_changes:
            neighbour_count = self.neighbour_count_of(x, y)
            if self.field[x][y] is None:
                if neighbour_count == 3:
                    born_cells.append((x, y))
            elif neighbour_count < 2 or neighbour_count > 3:
                died_cells.append((x, y))

        self.potential_changes.clear()
        for (x, y) in died_cells:
            self.field[x][y] = None
            self.potential_changes.add((x, y))
            self.potential_changes.update(self.get_neighbours(x, y))

        for (x, y) in born_cells:
            self.field[x][y] = World.CELL
            self.potential_changes.add((x, y))
            self.potential_changes.update(self.get_neighbours(x, y))

        self.life_cell_count += len(born_cells)
        self.life_cell_count -= len(died_cells)

        current_cell_count = self.life_cell_count
        if current_cell_count == self.prev_gen_cell_number:
            self.unchanged_gen += 1
        else:
            self.unchanged_gen = 0
        self.prev_gen_cell_number = current_cell_count

    def neighbour_count_of(self, x, y):
        result = 0

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

    @staticmethod
    def get_neighbours(x, y):
        neighbours = [(x - 1, y), (x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x + 1, y), (x + 1, y + 1), (x, y + 1),
                      (x - 1, y + 1)]
        return neighbours

    def is_empty_cell(self, x, y):
        # x, y = World.normalize_coordinates(x, y)
        return self.field[x][y] is None

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
                x_elements.append('-' if self.field[x][y] is None else 'X')
            resulted_lines.append(' '.join(x_elements))
        return '\n'.join(resulted_lines)


if __name__ == '__main__':
    lines = [[] for i in range(5)]

    glider = [['-', '-', 'X'], ['X', '-', 'X'], ['-', 'X', 'X']]
    acorn = [['-', '-', 'X'], ['X', '-', 'X'], ['-', '-', '-'], ['-', 'X', '-'], ['-', '-', 'X'], ['-', '-', 'X'],
              ['-', '-', 'X']]

    start = time.time()
    with open('/home/ipatrikeev/dev/input.txt') as f:
        x_offset, y_offset = [int(x) for x in f.readline().split()]

    world = World(acorn, glider, x_offset, y_offset * -1)
    # print(world)
    iter_count = 0
    while True:
        world.do_iteration()
        iter_count += 1
        print(str(iter_count) + ' : ' + str(world.unchanged_gen))
        if world.unchanged_gen >= 5:
            break
    iter_count -= 5
    print(iter_count, world.life_cell_count)
    end = time.time()
    print('exec time: '"%.2f" % round(end - start, 2))
