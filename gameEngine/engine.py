from snake import Snake

def clean_field(width=11, height=11):
    return [['*' for i in range(width)] for i in range(height)]

def insert_snake(field, snake:Snake):
    for bodypart in snake.body:
        field[bodypart[0]][bodypart[1]] = 'O'
    field[snake.head[0]][snake.head[1]] = '@'

def print_field(field):
    for y in field:
        for x in y:
            print(x, end=' ')
        print('\n', end='')


snake = Snake()
field = clean_field()
while True:
    field = clean_field()
    insert_snake(field, snake)
    print_field(field)
    direction = input('Direction: ')
    snake.move(direction)