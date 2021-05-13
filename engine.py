from hashlib import new
from snake import Snake
from food import Food
from bodypart import Bodypart

from copy import deepcopy

import random

class Engine():

    def __init__(self, border_width=11, border_height=11):
        self.snake = Snake(5, 5)
        self.foods = []
        self.border_width = border_width
        self.border_height = border_height
        self.walls = []
        self.max_apples = 1

    def clean_field(self, width=11, height=11):
        return [['*' for i in range(width)] for i in range(height)]

    def genereate_wall(self, fromx, fromy, tox, toy):
        #generate a group of bodyparts to act as a wall from x,y to x1,y1
        if fromy == toy:
            for offset in range(0, tox-fromx):
                self.walls.append(Bodypart(fromx+offset, fromy, '#'))
        elif fromx == tox:
            for offset in range(0, toy-fromy):
                self.walls.append(Bodypart(fromx, fromy+offset, '#'))
    
    def generate_outer_walls(self, height=10, width=10):
        #Generates an outer wall
        x_offset = width//2
        y_offset = height//2

        self.genereate_wall(-x_offset, y_offset+1, x_offset+1, y_offset+1)
        self.genereate_wall(-x_offset, -y_offset-1, x_offset+1, -y_offset-1)
        self.genereate_wall(-x_offset-1, -y_offset, -x_offset-1, y_offset+1)
        self.genereate_wall(x_offset+1, -y_offset, x_offset+1, y_offset+1)
        
        '''
        self.genereate_wall(0-x_offset, 0+y_offset, x_offset+1, 0+y_offset)
        self.genereate_wall(0-x_offset+1, 0-y_offset-1, x_offset+1, 0-y_offset-1)

        self.genereate_wall(0+x_offset+1, 0-y_offset, 0+x_offset+1, 0+y_offset+1)
        self.genereate_wall(0-x_offset, 0-y_offset, 0-x_offset, 0+y_offset+1)
        '''
        #print(self.walls)

    def spawn_food(self, min_x=0, max_x=5, min_y=0, max_y=5):

        mat = None
        under = True
        while under:
            under = False
            x = random.randint(min_x, max_x)
            y = random.randint(min_y, max_y)

            mat = Food(x, y)

            if self.snake.head == mat:
                #print("MAT UNDER HODE")
                under = True
                continue

            for wall in self.walls:
                if wall == mat:
                    #print("MAT UNDER VEGG")
                    under = True
                    break

            for bodypart in self.snake.body:
                if bodypart == mat:
                    #print("MAT UNDER SLANGE")
                    under = True
                    break
        print('spawned some food at', mat)
        golden = random.randint(1,10)
        if golden == 10:
            mat.strength = 3
            mat.skin = '%'
        self.foods.append(mat)

    def update(self):
        if self.max_apples > len(self.foods):
            self.spawn_food()

        self.snake.add_score()

        if self.snake.collision([self.snake], self.foods):
            return True
        elif self.snake.wall_collision(self.walls):
            return True
        else:
            return False

    @staticmethod
    def print_field(field):
        for y in field:
            for x in y:
                print(x, end=' ')
            print('\n', end='')

    def render_field(self, screen_width=11, screen_height=11):
        field = self.clean_field(screen_width, screen_height)
        items = self.get_items_on_screen(screen_width, screen_height)
        for item in items:
            field[item.y][item.x] = item.skin
    
        self.print_field(field)

    def get_items_on_screen(self, width=11, height=11):
        items_onscreen = []
        middlex, middley = width//2, height//2
        referencex, referencey = self.snake.head.x, self.snake.head.y

        #Add head to list

        for food in self.foods:
            deltax, deltay = food.x - referencex , referencey - food.y
            x = middlex + deltax
            y = middley + deltay
            if ((0<= x < width) and (0<= y < height)):
                #items_onscreen.append(food)
                newfood = Food(x, y, food.strength, food.skin)
                items_onscreen.append(newfood)
        
        for bodypart in self.snake.body:
            deltax, deltay = bodypart.x - referencex, referencey - bodypart.y
            x = middlex + deltax
            y = middley + deltay
            if ((0 <= x < width) and (0 <= y < height)):
                #items_onscreen.append(bodypart)
                items_onscreen.append(Bodypart(x, y))
        
        for wall in self.walls:
            deltax, deltay = wall.x - referencex, referencey - wall.y
            x = middlex + deltax
            y = middley + deltay
            if ((0 <= x < width) and (0 <= y < height)):
                #items_onscreen.append(bodypart)
                items_onscreen.append(Bodypart(x, y, '#'))


        items_onscreen.append(Bodypart(middlex, middley, '@'))

        return items_onscreen

if __name__ == '__main__':
    engine = Engine()
    engine.generate_outer_walls(20, 20)
    while True:
        engine.render_field()
        direction = input('Direction: ')
        engine.snake.move(direction)
        if engine.update():
            break