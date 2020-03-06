import sys
from CustomerHeadquarter import CustomerHeadquarter
from printing import print_map

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

file_name = sys.argv[1]
my_file = open(file_name, "r")
customer_headquarters = []
terrain = []
map_width, map_height, customer_headquarters_count, reply_offices_max = [int(x) for x in my_file.readline().split()]

for i in range(customer_headquarters_count):
    x_coord, y_coord, reward = [int(x) for x in my_file.readline().split()]
    customer_headquarters.append(CustomerHeadquarter(i, x_coord, y_coord, reward))

for i in range(map_height):
    terrain.append([x for x in my_file.readline()])



print_map(customer_headquarters, map_width, map_height, terrain)



