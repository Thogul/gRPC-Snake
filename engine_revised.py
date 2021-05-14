import protobuffer_pb2 as game

#type hinting stuff
from typing import List
Wall_obj = game.Object

class Engine():
    def __init__(self) -> None:
        self.snakes: List[game.Snake] = []
        self.foods: List[game.Food] = []
        self.walls: List[game.Object] = []

    def __new_snake(self, id:str, x:int, y:int, score:int=0) -> game.Snake:
        raise NotImplementedError

    def __new_food(self, x:int, y:int, skin:str='A', strength:int=1) -> game.Food:
        raise NotImplementedError

    def __new_wall(self, x:int, y:int, skin='#') -> game.Object:
        raise NotImplementedError

    def set_snake_direction(self, id:str, direction:str) -> None:
        '''
        Get the snakes with the given id, then set the direction the snake is
        supposed to move in the next gamestate update
        '''
        raise NotImplementedError

    def data_to_client(self) -> game.Data:
        raise NotImplementedError

    def spawn_food_at_snakes(self) -> None:
        raise NotImplementedError

    def __spawn_food(self, minx:int, miny:int, maxx:int, maxy:int) -> None:
        raise NotImplementedError

    def generate_outer_walls(self) -> None:
        raise NotImplementedError
    
    def generate_wall(self, fromx:int, fromy:int, tox:int, toy:int) -> None:
        raise NotImplementedError
    
    def update(self) -> None:
        '''
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
    food = game.Food(0, 1, 'A', 1)
    print(food)
