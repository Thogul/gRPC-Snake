from snake import Snake
from objects import Food

def clean_field(width=11, height=11):
    return [['*' for i in range(width)] for i in range(height)]

def insert_snake(field, snake:Snake):
    for bodypart in snake.body:
        field[bodypart.y][bodypart.x] = bodypart.skin
    field[snake.head.y][snake.head.x] = snake.head.skin

def insert_food(field, foods):
    for food in foods:
        field[food.y][food.x] = food.skin


def print_field(field):
    for y in field:
        for x in y:
            print(x, end=' ')
        print('\n', end='')

snake = Snake()
field = clean_field()
foods = [Food(2, 2)]
while True:
    field = clean_field()
    insert_food(field, foods)
    insert_snake(field, snake)
    print_field(field)
    direction = input('Direction: ')
    snake.move(direction)
    if snake.collision([snake], foods):
        break