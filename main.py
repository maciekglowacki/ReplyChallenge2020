
import sys
from CustomerHeadquarter import CustomerHeadquarter
from printing import print_map
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

points = {
    'T': 50,
    'H': 70,
    '_': 100,
    'X': 120,
    '+': 150,
    '*': 200,
    '~': 800,
    '#': 100000
}

file_name = sys.argv[1]
my_file = open(file_name, "r")
customer_headquarters = []
terrain = []
map_width, map_height, customer_headquarters_count, reply_offices_max = [int(x) for x in my_file.readline().split()]

for i in range(customer_headquarters_count):
    x_coord, y_coord, reward = [int(x) for x in my_file.readline().split()]
    customer_headquarters.append(CustomerHeadquarter(i, x_coord, y_coord, reward))

for i in range(map_height):
    terrain.append([points[x] for x in my_file.readline().rstrip()])



# print_map(customer_headquarters, map_width, map_height, terrain)


grid = Grid(matrix=terrain)

start = grid.node(1, 24)
end = grid.node(2, 24)

finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
path, runs = finder.find_path(start, end, grid)

print('operations:', runs, 'path length:', len(path))
print(grid.grid_str(path=path, start=start, end=end))