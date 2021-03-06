

def print_map(customer_headquarters, map_width, map_height, terrain):
    for y in range(map_height):
        for x in range(map_width):
                if is_headquarter(customer_headquarters, x, y):
                    print('C', end = '')
                else:
                    print(terrain[y][x], end = '')
        print()

def is_headquarter(customer_headquarters,x,y):
    for i in range (len(customer_headquarters)):
        if (customer_headquarters[i].x_coord == x and customer_headquarters[i].y_coord == y):
            return True
    return False