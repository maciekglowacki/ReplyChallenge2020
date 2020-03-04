import sys
from CustomerHeadquarter import CustomerHeadquarter

file_name = sys.argv[1]
file = open(file_name, "r")
map_width, map_height, customer_headquarters_count, reply_offices_max = [int(x) for x in file.readline().split()]
# print(map_width, map_height, customer_headquarters_count, reply_offices_max)

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
    x_coord, y_coord, reward = [int(x) for x in file.readline().split()]
    customer_headquarters.append(CustomerHeadquarter(i, x_coord, y_coord, reward))

#for customer_headquarter in customer_headquarters:
#    print(customer_headquarter)

terrain = []


