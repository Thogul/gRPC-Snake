from time import sleep
import protobuffer_pb2 as game
import random

from threading import Thread

#import db #database

#type hinting stuff
from typing import List, Dict, Tuple
Wall_obj = game.Object
Id = str
Direction = str

class Engine():
    def __init__(self, db = None) -> None:
        self.snakes: List[game.Snake] = []
        self.foods: List[game.Food] = []
        self.walls: List[game.Object] = []
        self.max_food = 10
        self.boundariesx : Tuple(int, int) = (0, 0)
        self.boundariesy : Tuple(int, int) = (0, 0)
        self.db = db
        
        #save directions in a dictionary of [id, direction]
        self.directions: Dict[Id, Direction] = {}

    @ staticmethod
    def new_object(x:int, y:int, skin:str):
        object = game.Object()
        object.x = x
        object.y = y
        object.skin = skin
        return object

    @staticmethod
    def __new_snake(id:str, x:int, y:int, score:int=0, length:int=5) -> game.Snake:
        snake = game.Snake()
        snake.id = id
        snake.head.x = x
        snake.head.y = y
        snake.head.skin = '@'
        for yoffset in range(1, length):
            bodypart = game.Object()
            bodypart.x = x
            bodypart.y = snake.head.y - yoffset
            bodypart.skin = 'O'
            snake.body.append(bodypart)
        return snake

    @staticmethod
    def __new_food(x:int, y:int, skin:str='A', strength:int=1) -> game.Food:
        food = game.Food()
        food.x = x
        food.y = y
        food.skin = skin
        food.strength = strength
        return food

    @staticmethod
    def __new_wall(x:int, y:int, skin='#') -> game.Object:
        wall = game.Object()
        wall.x = x
        wall.y = y
        wall.skin = '#'
        return wall

    def set_snake_direction(self, id:str, direction:str) -> None:
        '''
        Get the snakes with the given id, then set the direction the snake is
        supposed to move in the next gamestate update
        '''
        self.directions[id] = direction
        #check if snake exists, and if not. Spawn a new one.
        for snake in self.snakes:
            if snake.id == id:
                return
        print('Could not find new snake, made a new one with id:' + id)
        self.spawn_snake(id, )

    def data_to_client(self) -> game.Data:
        data = game.Data()
        data.snakes.extend(self.snakes)
        data.foods.extend(self.foods)
        data.walls.extend(self.walls)
        return data

    def spawn_food_at_snakes(self) -> None:
        if len(self.snakes) > 0:
            randint = random.randint(0, len(self.snakes)-1)
            snake = self.snakes[randint]
            headx, heady = snake.head.x, snake.head.y
            if self.max_food > len(self.foods):
                self.__spawn_food(headx-5, heady-5, headx+5, heady+5)

    def __spawn_food(self, minx:int, miny:int, maxx:int, maxy:int) -> None:
        import warnings
        warnings.warn("Warning...........Not tested!")
        
        mat = None
        under = True
        while under:
            under = False
            randomx = random.randint(minx, maxx)
            randomy = random.randint(miny, maxy)
            mat = self.__new_food(randomx, randomy)

            for snake in self.snakes:
                if (mat.x == snake.head.x) and (mat.y == snake.head.y):
                    under = True
                    continue

                for bodypart in snake.body:
                    if (mat.x == bodypart.x) and (mat.y == bodypart.y):
                        under = True
                        break

            for wall in self.walls:
                if (mat.x == wall.x) and (mat.y == wall.y):
                    under = True
                    break
            
            if (mat.x <= self.boundariesx[0]) or (mat.x >= self.boundariesx[1]) or (mat.y <= self.boundariesy[0]) or (mat.y >= self.boundariesy[1]):
                under = True

        golden = random.randint(1,10)
        if golden == 10:
            mat.skin = '%'
            mat.strength = 3

        self.foods.append(mat)

    def generate_outer_walls(self, height: int = 10, width: int = 10) -> None:
        #Height and width needs to be atleast 6
        x_offset = width//2
        y_offset = height//2
        self.boundariesx = (-x_offset+3, x_offset-3)
        self.boundariesy = (-y_offset+3, y_offset-3)

        self.generate_wall(-x_offset, y_offset+1, x_offset+1, y_offset+1)
        self.generate_wall(-x_offset, -y_offset-1, x_offset+1, -y_offset-1)
        self.generate_wall(-x_offset-1, -y_offset, -x_offset-1, y_offset+1)
        self.generate_wall(x_offset+1, -y_offset, x_offset+1, y_offset+1)

    def generate_wall(self, fromx:int, fromy:int, tox:int, toy:int) -> None:
        if fromy == toy:
            for xoffset in range(0, tox-fromx):
                wall = self.__new_wall(fromx+xoffset, fromy)
                self.walls.append(wall)
        elif fromx == tox:
            for yoffset in range(0, toy-fromy):
                wall = self.__new_wall(fromx, fromy+yoffset)
                self.walls.append(wall)

    def spawn_snake(self, id: str = 'Guest') -> None:
        '''
        Spawn a new snake with the given id, also add directions to snake
        '''
        #basic implementation
        minx, maxx = self.boundariesx
        x = random.randint(minx, maxx)
        miny, maxy = self.boundariesy
        y = random.randint(miny, maxy-10)
        snake = self.__new_snake(id, x, y, 0, 4) #Testing legnth
        self.snakes.append(snake)
        self.directions[id] = 'w'

        import warnings
        warnings.warn("Warning...........Just basic implementation")

    def move_snake(self, id:str, direction) -> None:
        #firstly find the right snake:
        #VERY UGLY CODE
        moves = ['w', 'a', 's', 'd']
        for snake in self.snakes:
            if snake.id == id:
                lastx, lasty = snake.head.x, snake.head.y
                if direction == 'w':
                    if snake.body[0].y == lasty+1:
                        self.move_snake(id, 's')
                        return
                    else:
                        snake.head.y += 1
                if direction == 's':
                    if snake.body[0].y == lasty-1:
                        self.move_snake(id, 'w')
                        return
                    else:
                        snake.head.y -= 1
                if direction == 'd':
                    if snake.body[0].x == lastx + 1:
                        self.move_snake(id, 'a')
                        return
                    else:
                        snake.head.x += 1
                if direction == 'a':
                    if snake.body[0].x == lastx - 1:
                        self.move_snake(id, 'd')
                        return
                    else:
                        snake.head.x -= 1

                #move the body:
                for i in range(1, len(snake.body)):
                    snake.body[-i].x = snake.body[-i-1].x
                    snake.body[-i].y = snake.body[-i-1].y
                snake.body[0].x = lastx
                snake.body[0].y = lasty

                return

    def grow_snake(self, id:str, food:game.Object) -> None:
        #add a new snake object on the same spot as the last snake bodypart
        for snake in self.snakes:
            if snake.id == id:
                for _ in range(food.strength):
                    bodypart = game.Object()
                    bodypart.x = snake.body[-1].x
                    bodypart.y = snake.body[-1].y
                    bodypart.skin = 'O'
                    snake.body.append(bodypart)
                try:
                    self.foods.remove(food)
                except ValueError:
                    print('Could not remove food from snake!' + food)
                return

    def kill_snake(self, id):
        print(id + 'Died')
        for snake in self.snakes:
            if snake.id == id:
                score = snake.score
                x, y = snake.body[0].x, snake.body[0].y
                self.snakes.remove(snake)
                self.directions.pop(id, None)
                if self.db is not None:
                    Thread(target=lambda:self.db.insert_score(id, score), daemon=True).start()
                self.__spawn_food(x, y, x, y)

    def update_scores(self) -> None:
        for snake in self.snakes:
            snake.score += (len(snake.body)+1)//2

    def collisions(self):
        #Run throught each snake and see if it collides with anything
        #Maybe when running through snakes, make it not run through earlier snakes
        #Dont know what we should do with head to head collision(both dead, priority?)

        #run through each snake:
        for snake in self.snakes:
            #run through itself, for self collision
            for bodypart in snake.body:
                if (snake.head.x == bodypart.x) and (snake.head.y == bodypart.y):
                    #snake has collided with itself, delete or something
                    #self.kill_snake(snake.id) something like this id
                    self.kill_snake(snake.id)
            
            #All other snakes body collision
            for other_snake in self.snakes:
                if other_snake == snake:
                    continue
                if (snake.head.x == other_snake.head.x) and (snake.head.y == other_snake.head.y):
                    self.kill_snake(snake.id)
                    self.kill_snake(other_snake.id)
                    continue
                for bodypart in other_snake.body:
                    if (snake.head.x == bodypart.x) and (snake.head.y == bodypart.y):
                        #Collision suff idk
                        self.kill_snake(snake.id)

            for wall in self.walls:
                if (snake.head.x == wall.x) and (snake.head.y == wall.y):
                    #Do collision
                    self.kill_snake(snake.id)
            
            for food in self.foods:
                if (snake.head.x == food.x) and (snake.head.y == food.y):
                    #Eat an apple or something
                    self.grow_snake(snake.id, food)

    def update(self) -> None:
        '''
        OBS: We think we want to use threadlocking when updating the game
            Maybe only per update part, but likely the whole shæbang
        Take care of updating the game:
         - Move snakes
         - Handle collision
         - remove dead snakes
         - etc..

         For clearity, make needed private functions for
         functionality that is needed
         '''
        self.collisions()
        #if len(self.directions) > 0:
        for id, direction in self.directions.items():
            self.move_snake(id, direction)

        self.spawn_food_at_snakes()
        self.update_scores()
    
    def game_loop_thread(self) -> None:
        while True:
            sleep(0.1)
            print('updating')
            self.update()

    @staticmethod
    def get_items_on_screen(id:str, data:game.Data, width:int=11, height:int=11) -> List[game.Object]:
        #get the main snake first, for center reference
        main_snake = None
        #should be with i, snake in enumerate(data.snakes):
        for i, snake in enumerate(data.snakes):
            if snake.id == id:
                main_snake = data.snakes.pop(i)
        if main_snake is None:
            #my snake is not there, i might be dead or something
            #maybe not update anything idk
            print('was no main snek')
            return []

        #start the algorithm
        items_onscreen = []
        middlex, middley = width//2, height//2
        referencex, referencey = main_snake.head.x, main_snake.head.y

        #The order/priority of items in screen(what is drawn on top of what)
        #is mainsnakehead, mainsnakebody, other snakeheads, other snakebodies, walls, food
        #That means that the list is "reversed" with lowest pre first in the list

        for food in data.foods:
            deltax, deltay = food.x - referencex , referencey - food.y
            x = middlex + deltax
            y = middley + deltay
            if ((0<= x < width) and (0<= y < height)):
                #items_onscreen.append(food)
                newfood = Engine.__new_food(x, y, food.skin, food.strength)
                items_onscreen.append(newfood)

        for other_snake in data.snakes:
            deltax, deltay = other_snake.head.x - referencex , referencey - other_snake.head.y
            x = middlex + deltax
            y = middley + deltay
            if ((0<= x < width) and (0<= y < height)):
                items_onscreen.append(Engine.new_object(x, y, '@'))

            for bodypart in other_snake.body:
                deltax, deltay = bodypart.x - referencex , referencey - bodypart.y
                x = middlex + deltax
                y = middley + deltay
                if ((0<= x < width) and (0<= y < height)):
                    items_onscreen.append(Engine.new_object(x, y, 'O'))

        for wall in data.walls:
            deltax, deltay = wall.x - referencex , referencey - wall.y
            x = middlex + deltax
            y = middley + deltay
            if ((0<= x < width) and (0<= y < height)):
                items_onscreen.append(Engine.new_object(x, y, '#'))

        #Add main snake, with head last so it's printed on top of everything else
        for bodypart in main_snake.body:
            deltax, deltay = bodypart.x - referencex , referencey - bodypart.y
            x = middlex + deltax
            y = middley + deltay
            if ((0<= x < width) and (0<= y < height)):
                items_onscreen.append(Engine.new_object(x, y, 'O'))

        items_onscreen.append(Engine.new_object(middlex, middley, '@'))
        
        return items_onscreen

    @staticmethod
    def render_field(items, screen_width=11, screen_height=11):
        field = [['*' for i in range(screen_width)] for i in range(screen_height)]
        for item in items:
            field[item.y][item.x] = item.skin
    
        for y in field:
            for x in y:
                print(x, end=' ')
            print('\n', end='')

if __name__ == '__main__':
    engine = Engine()
    engine.spawn_snake('Thomas')
    #engine.foods.append(engine._Engine__new_food(0, 0))
    #print(engine.data_to_client())
    for snake in engine.data_to_client().snakes:
        print(snake.head.x, snake.head.y, snake.head.skin)
        for bodypart in snake.body:
            print(bodypart.x, bodypart.y, bodypart.skin)
    engine.move_snake('Thomas', 'd')
    print('Moving snake')
    for snake in engine.data_to_client().snakes:
        print(snake.head.x, snake.head.y, snake.head.skin)
        for bodypart in snake.body:
            print(bodypart.x, bodypart.y, bodypart.skin)
    #print(engine.data_to_client())
    #engine.collisions()
