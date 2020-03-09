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
