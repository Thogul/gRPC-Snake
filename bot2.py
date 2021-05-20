from PyQt5.QtCore import qSNaN
from protobuffer_pb2 import Snake, _SNAKE
from client import Client
from engine_revised import Engine
from threading import Thread
import random

import sys

bot_amount = int(sys.argv[1])



class Bot():
    def __init__(self, id, engine:Engine, client:Client) -> None:
        self.id = id
        self.engine = Engine
        self.client = Client(self.id, self.engine)
        self.heading = "w"
        
    def getFood(self):
        data = self.client.gotten_data.get()
        while len(data.foods) == 0:
            print('No food')
            data = self.client.gotten_data.get()
        mat = random.choice(data.foods)
        print('going for ', mat.x, mat.y)
        while True:
            data = self.client.gotten_data.get()
            snake = None
            for some_snake in data.snakes:
                if self.id == some_snake.id:
                    snake = some_snake
            if snake is None:
                print('am dead i guess')
                return
                
            if snake.head.x < mat.x:
                #while snake.head.x < mat.x:
                if self.heading == 'd':
                    continue
                elif self.heading == 'a':
                    self.client.send_action('w')
                    self.heading = 'w'
                else:
                    self.client.send_action('d')
                    self.heading = 'd'
                continue
            elif snake.head.x > mat.x:
                #while snake.head.x > mat.x:
                if self.heading == 'a':
                    continue
                elif self.heading == 'd':
                    self.client.send_action('w')
                    self.heading = 'w'
                else:
                    self.client.send_action('a')
                    self.heading = 'a'
                continue
            
            elif snake.head.y < mat.y:
                #while snake.head.y < mat.y:
                if self.heading == 'w':
                    continue
                elif self.heading == 's':
                    self.client.send_action('a')
                    self.heading = 'a'
                else:
                    self.client.send_action('w')
                    self.heading = 'w'
                continue
            elif snake.head.y > mat.y:
                #while snake.head.y > mat.y:
                if self.heading == 's':
                    continue
                elif self.heading == 'w':
                    self.client.send_action('a')
                    self.heading = 'a'
                else:
                    self.client.send_action('s')
                    self.heading = 's'
                continue

            elif (snake.head.x == mat.x) and (snake.head.y == mat.y):
                print('360 No-scope!')
                break
    
    def run(self):
        while True:
            data = self.client.gotten_data.get()
            if self.engine.get_items_on_screen(self.id, data) == []:
                self.client.send_action('w')
                self.heading = 'w'
                print('spawning')
            while self.engine.get_items_on_screen(self.id, data) == []:
                data = self.client.gotten_data.get()
                print('waiting spawn')

            self.getFood()


    def start(self):
        Thread(target=self.run, daemon=True).start()

if __name__ == '__main__':
    from time import sleep
    #bot_dos = Bot('Pro gamer', Engine, Client)
    #bot_dos.start()
    #bot_amount = 3
    for i in range(bot_amount):
        bot = Bot('bot'+str(i), Engine, Client)
        bot.start()
        sleep(2)
    while True:
        pass
