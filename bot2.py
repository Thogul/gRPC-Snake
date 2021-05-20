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
        self.client = client(self.id, self.engine)

    def getFood(self):
        
        mat = random.choice.Engine.foods
        snake = Engine.snake
            
        if snake.x < mat.x:
            while snake.x < mat.x:
                self.client.send_action('d')
        elif snake.x > mat.x:
            while snake.x > mat.x:
                self.client.send_action('a')
        
        if snake.y < mat.y:
            while snake.y < mat.y:
                self.client.send_action('w')
        elif snake.y > mat.y:
            while snake.y > mat.y:
                self.client.send_action('s')

        if (snake.x == mat.x) and (snake.y == mat.y):
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