from client import Client
from engine_revised import Engine
from threading import Thread


#make a basig bot that does nothing while respawning if dead

class Bot():
    def __init__(self, id, engine:Engine, client:Client) -> None:
        self.id = id
        self.engine = Engine
        self.client = client(self.id, self.engine)

    def run(self):
        while True:
            data = self.client.gotten_data.get()
            if self.engine.get_items_on_screen(self.id, data) == []:
                print('Spawning')
                self.client.send_action('w')

    def start(self):
        Thread(target=self.run, daemon=True).start()

if __name__ == '__main__':
    bot_uno = Bot('Bottersen', Engine, Client)
    bot_uno.start()
    while True:
        pass