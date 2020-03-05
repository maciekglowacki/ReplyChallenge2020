import sys
from CustomerHeadquarter import CustomerHeadquarter

file_name = sys.argv[1]
my_file = open(file_name, "r")

map_width, map_height, customer_headquarters_count, reply_offices_max = [int(x) for x in my_file.readline().split()]
# print(map_width, map_height, customer_headquarters_count, reply_offices_max)
# print("XXD")

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
    customer_headquarters.append(CustomerHeadquarter(i, x_coord, y_coord, reward))

for customer_headquarter in customer_headquarters:
    print(customer_headquarter)
print(points['+'])

terrain = []
for i in range(map_height):
    terrain.append([x for x in my_file.readline()])

# terrain = [[] for i in range(map_height + 1)]
# for i in range(map_height):
#     for i2 in range(map_width):
#         terrain[map_height].append([x for x in my_file.readline().split(' ')])

# for i in range(map_width):
#         terrain = list()  

 

for i in range(map_height):
    for i2 in range(map_width):
        print(terrain[i][i2], end = '') 
    print(" ")   



