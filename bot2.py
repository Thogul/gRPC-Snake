from client import Client
from engine_revised import Engine
from threading import Thread
import random

import sys

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
                if self.heading == 'd':
                    pass
                elif self.heading == 'a':
                    self.client.send_action('w')
                    self.heading = 'w'
                    sleep(0.5)
                else:
                    self.client.send_action('d')
                    self.heading = 'd'
                    sleep(0.05)
                continue
            elif snake.head.x > mat.x:
                if self.heading == 'a':
                    pass
                elif self.heading == 'd':
                    self.client.send_action('w')
                    self.heading = 'w'
                    sleep(0.05)
                else:
                    self.client.send_action('a')
                    self.heading = 'a'
                    sleep(0.05)
                continue
            
            elif snake.head.y < mat.y:
                if self.heading == 'w':
                    pass
                elif self.heading == 's':
                    self.client.send_action('a')
                    self.heading = 'a'
                    sleep(0.05)
                else:
                    self.client.send_action('w')
                    self.heading = 'w'
                    sleep(0.05)
                continue
            elif snake.head.y > mat.y:
                if self.heading == 's':
                    pass
                elif self.heading == 'w':
                    self.client.send_action('a')
                    self.heading = 'a'
                    sleep(0.05)
                else:
                    self.client.send_action('s')
                    self.heading = 's'
                    sleep(0.05)
                continue

            elif (snake.head.x == mat.x) and (snake.head.y == mat.y):
                print('360 No-scope!')
                break
    
    def run(self):
        while True:
            data = self.client.gotten_data.get()
            while self.engine.get_items_on_screen(self.id, data) == []:
                self.client.send_action('w')
                self.heading = 'w'
                print('spawning')
                data = self.client.gotten_data.get()
                sleep(0.5)

            self.getFood()


    def start(self):
        Thread(target=self.run, daemon=True).start()

if __name__ == '__main__':
    from time import sleep

    bot_amount = int(sys.argv[1])
    for i in range(bot_amount):
        bot = Bot('bot-'+str(i + 1)+' ', Engine, Client)
        bot.start()
        sleep(2)
    while True:
        pass
