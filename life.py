class Cell:
    def __init__(self, x, y, empty=False):
        self.x = x
        self.y = y
        self.empty = empty

    def __str__(self):
        return '[' + str(self.x) + ',' + str(self.y) + ']'


class World:
    MAX_X = 30
    MAX_Y = 30
    OFFSET = 8

    def __init__(self, field):
        self.field = [[] for i in range(World.MAX_X)]
        # extending field
        for y in range(World.MAX_Y):
            for x in range(World.MAX_X):
                self.field[x].append(Cell(x, y, True))

        for x in range(len(field)):
            for y in range(len(field[0])):
                is_empty = (field[x][y] == '-')
                cell = Cell(x + World.OFFSET, y + World.OFFSET, is_empty)
                self.field[x + World.OFFSET][y + World.OFFSET] = cell

    def do_iteration(self):
        born_cells = []
        died_cells = []

        for i in range(World.MAX_X):
            for j in range(World.MAX_Y):
                cell = self.field[i][j]
                neighbour_count = self.neighbour_count_of(cell)
                if cell.empty:
                    if neighbour_count == 3:
                        born_cells.append(cell)
                elif neighbour_count < 2 or neighbour_count > 3:
                    died_cells.append(cell)

        for c in died_cells:
            self.field[c.x][c.y] = Cell(c.x, c.y, True)

        for c in born_cells:
            self.field[c.x][c.y] = Cell(c.x, c.y)

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
    with open('/home/ipatrikeev/dev/input.txt') as f:
        for y in range(5):
            line = list(f.readline().strip())
            for x in range(7):
                lines[y].append(line[x])

    world = World(lines)

    for i in range(5):
        world.do_iteration()
        print(world.live_cell_count(), end=' ')
