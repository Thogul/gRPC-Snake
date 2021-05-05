from snake import Snake
from objects import Food

import random

def clean_field(width=11, height=11):
    return [['*' for i in range(width)] for i in range(height)]

def insert_snake(field, snake:Snake):
    for bodypart in snake.body:
        field[bodypart.y][bodypart.x] = bodypart.skin
    field[snake.head.y][snake.head.x] = snake.head.skin

def insert_food(field, foods):
    for food in foods:
        field[food.y][food.x] = food.skin

def spawn_food(field):
    max_y = len(field)-1
    max_x = len(field[0])-1
    
    random_x = random.randint(0, max_x)
    random_y = random.randint(0, max_y)

    return  [random_x, random_y]

def print_field(field):
    for y in field:
        for x in y:
            print(x, end=' ')
        print('\n', end='')

snake = Snake()
field = clean_field()
foods = [Food(spawn_food(field)[0], spawn_food(field)[1])]
while True:
    field = clean_field()
    insert_food(field, foods)
    insert_snake(field, snake)
    print_field(field)
    direction = input('Direction: ')
    snake.move(direction)
    if snake.collision([snake], foods):
        break
    if len(foods) < 1:
        foods.append(Food(spawn_food(field)[0], spawn_food(field)[1], 5))