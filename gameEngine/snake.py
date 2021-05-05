

class Snake():

    def __init__(self, position = [5, 5], start_length = 3):
        self.head = position
        self.length = start_length
        self.body = [self.head[:]]
        self.invalid_direction = 's'
        self.last_direction = 'w'
        for i in range(1, self.length):
            self.body.append([self.head[0], self.head[1]+i])
        print(self.body)

    def move(self, direction:str, speed=1):
        #firtly try to move, if no valid move was sent, skip the rest
        if direction == self.invalid_direction:
            self.move(self.last_direction)
        elif direction == 'w':
            self.head[0] -= 1
            self.invalid_direction = 's'
            self.last_direction = 'w'
        elif direction == 's':
            self.head[0] += 1
            self.invalid_direction = 'w'
            self.last_direction = 's'
        elif direction == 'a':
            self.head[1] -= 1
            self.invalid_direction = 'd'
            self.last_direction = 'a'
        elif direction == 'd':
            self.head[1] += 1
            self.invalid_direction = 'a'
            self.last_direction = 'd'
        else:
            return

        #firtly move the whole body forward by one position from back to front
        body_length = len(self.body)
        for i in range(1, len(self.body)):
            self.body[body_length-i] = self.body[body_length-i-1]

        self.body[0] = self.head[:]
        print(self.body)

    def grow(self):
        pass

    def collision(self, snakes):
        pass

    def wall_collision(self, walls):
        pass

if __name__ == '__main__':
    snake = Snake()