import protobuffer_pb2 as game

#type hinting stuff
from typing import List, Dict
Wall_obj = game.Object
Id = str
Direction = str

class Engine():
    def __init__(self) -> None:
        self.snakes: List[game.Snake] = []
        self.foods: List[game.Food] = []
        self.walls: List[game.Object] = []
        
        #save directions in a dictionary of [id, direction]
        self.directions: Dict[Id, Direction] = {}

    def __new_snake(self, id:str, x:int, y:int, score:int=0, length:int=5) -> game.Snake:
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

    def __new_food(self, x:int, y:int, skin:str='A', strength:int=1) -> game.Food:
        food = game.Food()
        food.x = x
        food.y = y
        food.skin = skin
        food.strength = strength
        return food

    def __new_wall(self, x:int, y:int, skin='#') -> game.Object:
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

    def data_to_client(self) -> game.Data:
        data = game.Data()
        data.snakes.extend(self.snakes)
        data.foods.extend(self.foods)
        data.walls.extend(self.walls)
        return data

    def spawn_food_at_snakes(self) -> None:
        raise NotImplementedError

    def __spawn_food(self, minx:int, miny:int, maxx:int, maxy:int) -> None:
        raise NotImplementedError

    def generate_outer_walls(self) -> None:
        raise NotImplementedError
    
    def generate_wall(self, fromx:int, fromy:int, tox:int, toy:int) -> None:
        raise NotImplementedError

    def spawn_snake(self, id: str = 'Guest') -> None:
        '''
        Spawn a new snake with the given id, also add directions to snake
        '''
        #basic implementation
        snake = self.__new_snake(id, 0, 0)
        self.snakes.append(snake)
        self.directions[id] = 'w'

        import warnings
        warnings.warn("Warning...........Just basic implementation")
    
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
        raise NotImplementedError

    @staticmethod
    def get_items_on_screen(data:game.Data) -> List[game.Object]:
        raise NotImplementedError


if __name__ == '__main__':
    engine = Engine()
    engine.spawn_snake('Thomas')
    print(engine.snakes)