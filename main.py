import sys
from CustomerHeadquarter import CustomerHeadquarter

file_name = sys.argv[1]
my_file = open(file_name, "r")

map_width, map_height, customer_headquarters_count, reply_offices_max = [
    int(x) for x in my_file.readline().split()]


points = {
    'T': 50,
    'H': 70,
    '_': 100,
    'X': 120,
    '+': 150,
    '*': 200,
    '~': 800,
    '#': float('inf')
}

customer_headquarters = []

for i in range(customer_headquarters_count):
    x_coord, y_coord, reward = [int(x) for x in my_file.readline().split()]
    customer_headquarters.append(
        CustomerHeadquarter(i, x_coord, y_coord, reward))


terrain = [ [j for j in my_file.readline().strip()] for i in range(map_height)]


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



