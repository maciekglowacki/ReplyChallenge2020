class CustomerHeadquarter:
    def __init__(self,id, x_coord, y_coord, reward):
        self.id = id
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.reward = reward

    def __str__(self):
        return f'Customer: {self.id}, x_coord: {self.x_coord}, y_coord: {self.y_coord}, reward: {self.reward}'
