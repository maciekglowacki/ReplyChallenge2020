directions: {
    'UP',
    'DOWN',
    'LEFT',
    'RIGHT'
}


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'X: {self.x}, Y: {self.y}'

    def kurwa(self, direction):
        if direction == 'UP':
            self.y -= 1
        elif direction == 'DOWN':
            self.y += 1
        elif direction == 'LEFT':
            self.x -= 1
        elif direction == 'RIGHT':
            self.x += 1


cell = Cell(1, 2)
print(cell)
cell.kurwa('UP')
print(cell)
cell.kurwa('DOWN')
print(cell)
cell.kurwa('LEFT')
print(cell)
cell.kurwa('RIGHT')
print(cell)


def move(cell, direction):
    result = {
        'UP': lambda cell: cell.y - 1,
        'DOWN': lambda cell: cell.y + 1,
        'LEFT': lambda cell: cell.x - 1,
        'RIGHT': lambda cell: cell.x + 1
    }[direction](cell)
