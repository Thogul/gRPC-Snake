from PyQt5.QtCore import qSNaN
from protobuffer_pb2 import Snake, _SNAKE
from client import Client
from engine_revised import Engine
from threading import Thread
import random



class Bot():
    def __init__(self, id, engine:Engine, client:Client) -> None:
        self.id = id
        self.engine = Engine
        self.client = Client(self.id, self.engine)
        self.heading = "w"
        
    def getFood(self):
        data = self.client.gotten_data.get()
        while len(data.foods) == 0:
            data = self.client.gotten_data.get()
        mat = random.choice(data.foods)
        while True:
            data = self.client.gotten_data.get()
            snake = None
            for some_snake in data.snakes:
                if self.id == some_snake.id:
                    snake = some_snake
            if snake is None:
                print('am dead i guess')
                exit(0)
                
            if snake.head.x < mat.x:
                #while snake.head.x < mat.x:
                if self.heading == 'a':
                    self.client.send_action('w')
                else:
                    self.client.send_action('d')
                    self.heading = 'd'
                continue
            elif snake.head.x > mat.x:
                #while snake.head.x > mat.x:
                if self.heading == 'd':
                    self.client.send_action('w')
                    self.heading = 'w'
                else:
                    self.client.send_action('a')
                    self.heading = 'a'
                continue
            
            if snake.head.y < mat.y:
                #while snake.head.y < mat.y:
                if self.heading == 's':
                    self.client.send_action('a')
                    self.heading = 'a'
                else:
                    self.client.send_action('w')
                    self.heading = 'w'
                continue
            elif snake.head.y > mat.y:
                #while snake.head.y > mat.y:
                if self.heading == 'w':
                    self.client.send_action('a')
                    self.heading = 'a'
                else:
                    self.client.send_action('s')
                    self.heading = 's'
                continue

            if (snake.head.x == mat.x) and (snake.head.y == mat.y):
                print('360 No-scope!')
                return
    
    def run(self):
        while True:
            data = self.client.gotten_data.get()
            if self.engine.get_items_on_screen(self.id, data) == []:
                print('Spawning')
                self.client.send_action('w')
            self.getFood()


    def start(self):
        Thread(target=self.run, daemon=True).start()

if __name__ == '__main__':
    bot_dos = Bot('Pro gamer', Engine, Client)
    bot_dos.start()
    while True:
        pass
