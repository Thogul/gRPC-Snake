from snake import Snake
from objects import Food

import random

def clean_field(width=11, height=11):
    return [['*' for i in range(width)] for i in range(height)]

def print_field(field):
    for y in field:
        for x in y:
            print(x, end=' ')
        print('\n', end='')

def render_field(field, main_snake: Snake, foods, snakes=[]):
    #first, clean up the whole field
    field = clean_field()

    middley, middlex = len(field)//2, len(field[0])//2

    #render priority:main snake, other snakes, food
    #draw all foods that is within screen
    midscreeny, midscreenx = main_snake.head.y, main_snake.head.x
    for food in foods:
        deltay, deltax = midscreeny-food.y, midscreenx-food.x
        if (deltay <= middley) and (deltax <= middlex):
            field[middley-deltay][middlex-deltax] = food.skin

    #draw in main snake, body then head, incase of body errors
    for bodypart in main_snake.body:
        deltax = bodypart.x - main_snake.head.x
        deltay = bodypart.y - main_snake.head.y
        field[middley+deltay][middlex+deltax] = bodypart.skin
    field[middley][middlex] = main_snake.head.skin

    print_field(field)

def spawn_food(field):
    max_y = len(field)-1
    max_x = len(field[0])-1
    
    random_x = random.randint(0, max_x)
    random_y = random.randint(0, max_y)

    return  [random_x, random_y]


if __name__ == '__main__':
    snake = Snake()
    field = clean_field()
    foods = [Food(0,0)]
    while True:
        render_field(field, snake, foods)
        direction = input('Direction: ')
        snake.move(direction)
        if snake.collision([snake], foods):
            break