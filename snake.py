from food import Food
from bodypart import Bodypart


class Snake():

    def __init__(self, x: int = 2, y: int = 2, start_length: int = 5, name: str = 'ME'):
        #self.head = position
        self.head = Bodypart(x, y, '@')
        self.length = start_length
        #self.body = [self.head[:]]
        self.body = []
        self.invalid_direction = 's'
        self.last_direction = 'w'
        for i in range(1, self.length):
            self.body.append(Bodypart(self.head.x, self.head.y-i))
        #print(self.body)
        self.score = 0
        self.alive = True
        self.name = name

    def move(self, direction: str, speed: int = 1):
        #firtly try to move, if no valid move was sent, skip the rest
        moves = ['w', 'a', 's', 'd']
        lastx, lasty = self.head.x, self.head.y
        if direction not in moves:
            self.move(self.last_direction)
            return
        elif direction == self.invalid_direction:
            self.move(self.last_direction)
            return
        elif direction == 'w':
            self.head.y += 1
            self.invalid_direction = 's'
            self.last_direction = 'w'
        elif direction == 's':
            self.head.y -= 1
            self.invalid_direction = 'w'
            self.last_direction = 's'
        elif direction == 'd':
            self.head.x += 1
            self.invalid_direction = 'a'
            self.last_direction = 'd'
        elif direction == 'a':
            self.head.x -= 1
            self.invalid_direction = 'd'
            self.last_direction = 'a'
        else:
            return

        #rotate all elements to the righ, with last one looping around
        #OPS, is slow! can be optimized if it becomes a problem, but probably wont
        self.body = [self.body[-1]] + self.body[:-1]
        self.body[0].x = lastx
        self.body[0].y = lasty
        #firtly move the whole body forward by one position from back to front

    def collision(self, snakes: list, foods: list):
        for food in foods:
            if self.head == food:
                print('collided with food')
                foods.remove(food)
                self.grow(food.strength)
        
        for snake in snakes:
            for bodypart in snake.body:
                if self.head == bodypart:
                    print('Collided with a body')
                    self.alive = False
                    return True
                    #die.exe

            if self.name == snake.name:
                continue
            if self.head == snake.head:
                print('Collided with head')
                self.alive = False
                return True
                #die.exe

    def grow(self, strength: int):
        for _ in range(strength):
            self.body.append(Bodypart(self.body[-1].x, self.body[-1].y))
        print('growing')

    def wall_collision(self, walls:list):
        for wall in walls:
            if self.head == wall:
                print('collided with wall')
                self.alive = False
                return True
                #die.exe

    def add_score(self, amount=None):
        if amount is None:
            self.score += self.length*10
        else:
            self.score += amount

if __name__ == '__main__':
    snake = Snake()
    food = Food(5, 5)

    snake.collision([], [food])