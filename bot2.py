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
        
        while True:
            data = self.client.gotten_data.get()
            for snake in data.snakes:
                if self.id == snake.id:
                    self.snake = snake
                    break


    def getFood(self):
        
        mat = random.choice.data.foods
        snake = self.snake
            
        if snake.head.x < mat.x:
            while snake.head.x < mat.x:
                self.client.send_action('d')
        elif snake.head.x > mat.x:
            while snake.head.x > mat.x:
                self.client.send_action('a')
        
        if snake.head.y < mat.y:
            while snake.head.y < mat.y:
                self.client.send_action('w')
        elif snake.head.y > mat.y:
            while snake.head.y > mat.y:
                self.client.send_action('s')

        if (snake.x == mat.x) and (snake.y == mat.y):
            print('360 No-scope!')
            Bot.getFood()

    def run(self):
        while True:
            data = self.client.gotten_data.get()
            if self.engine.get_items_on_screen(self.id, data) == []:
                print('Spawning')
                self.client.send_action('w')
                Bot.getFood()


    def start(self):
        Thread(target=self.run, daemon=True).start()

if __name__ == '__main__':
    bot_dos = Bot('Pro gamer', Engine, Client)
    bot_dos.start()
    while True:
        pass