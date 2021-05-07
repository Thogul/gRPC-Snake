from snake import Snake
from food import Food

import random

class Engine():

    def __init__(self, screen_width=11, screen_height=11):
        self.snake = Snake()
        self.foods = []
        self.screen_width = screen_width
        self.screen_height = screen_height

    def clean_field(self, width=11, height=11):
        return [['*' for i in range(width)] for i in range(height)]

    def print_field(self, field):
        for y in field:
            for x in y:
                print(x, end=' ')
            print('\n', end='')

    def render_field(self, field, main_snake: Snake, foods, snakes=[]):
        #first, clean up the whole field
        field = self.clean_field()

        middley, middlex = len(field)//2, len(field[0])//2

        #render priority:main snake, other snakes, food
        #draw all foods that is within screen
        midscreeny, midscreenx = main_snake.head.y, main_snake.head.x
        for food in foods:
            deltay, deltax = midscreeny-food.y, midscreenx-food.x
            if (abs(deltay) <= middley) and (abs(deltax) <= middlex):
                field[middley-deltay][middlex-deltax] = food.skin

        #draw in main snake, body then head, incase of body errors
        for bodypart in main_snake.body:
            deltax = bodypart.x - main_snake.head.x
            deltay = bodypart.y - main_snake.head.y
            if (abs(deltay) <= middley) and (abs(deltax) <= middlex):
                field[middley+deltay][middlex+deltax] = bodypart.skin
            #field[middley+deltay][middlex+deltax] = bodypart.skin
        field[middley][middlex] = main_snake.head.skin

        self.print_field(field)

    def spawn_food(self, foods, main_snake, min_x=0, max_x=5, min_y=0, max_y=5):

        mat = None
        under = True
        while under:
            under = False
            x = random.randint(min_x, max_x)
            y = random.randint(min_y, max_y)

            mat = Food(x, y)

            if main_snake.head == mat:
                print("MAT UNDER HODE")
                under = True
                continue

            for bodypart in main_snake.body:
                if bodypart == mat:
                    print("MAT UNDER SLANGE")
                    under = True
                    break

            
                
        foods.append(mat)

    def get_items_on_screen(self):
        items_onscreen = [self.snake.head]
        middlex, middley = self.screen_width//2, self.screen_height//2
        centerx, centery = self.snake.head.x, self.snake.head.y

        for food in self.foods:
            deltax, deltay = centerx-food.x, centery-food.x
            if (abs(deltax) <= middlex) and (abs(deltay)-middley):
                items_onscreen.append(food)
        
        for bodypart in self.snake.body:
            deltax, deltay = bodypart.x-centerx, bodypart.y-centery
            if (abs(deltax)-middlex) and (abs(deltay)-middley):
                items_onscreen.append(bodypart)
            
        items_onscreen.append(self.snake.head)

        return items_onscreen

if __name__ == '__main__':
    max_food = 1
    engine = Engine()
    snake = Snake()
    field = engine.clean_field()
    foods = [Food(0,0)]
    while True:
        engine.render_field(field, snake, foods)
        print(len(engine.get_items_on_screen()))
        direction = input('Direction: ')
        snake.move(direction)
        if snake.collision([snake], foods):
            break
        if len(foods) < max_food:
            engine.spawn_food(foods, snake)
