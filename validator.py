
directions: {
    'U',
    'D',
    'L',
    'R'
}


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'X: {self.x}, Y: {self.y}'

    def move(self, direction):
        if direction == 'U':
            self.y -= 1
        elif direction == 'D':
            self.y += 1
        elif direction == 'L':
            self.x -= 1
        elif direction == 'R':
            self.x += 1

    def cost(self, terrain):
        return terrain[self.x][self.y]

    def reward(self, terrain, customer_headquarters):
        for customer_headquarter in customer_headquarters:
            if self.x == customer_headquarter.x_coord and self.y == customer_headquarter.y_coord:
                return customer_headquarter.reward
        return 0

    
    def path(self,terrain, directions):
        path = 0
        for direction in directions:
            self.move(direction)
            value = terrain[self.x][self.y]
            path += value
    
        return path

