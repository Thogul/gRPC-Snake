import queue
from sys import maxsize
import threading
from time import sleep

import grpc

import protobuffer_pb2 as game
import protobuffer_pb2_grpc as rpc

from engine_revised import Engine
from queue import Queue


#address = '192.168.43.122'
address = 'localhost'
#address = '0.0.0.0'
port = 50051

class Client():

    def __init__(self, id:str, engine: Engine):
        self.id = id
        self.engine = engine
        self.gotten_data = Queue(maxsize=0)
        channel = grpc.insecure_channel(address+':'+str(port))
        self.conn = rpc.GameServerStub(channel)


        #New listening thread for getting messages
        self.id_action = game.Action()
        self.id_action.id = self.id
        self.id_action.direction = "stream"
        self.stream_thread = threading.Thread(target=self.__listen_for_messages, daemon=True)

        self.started = False
        
    def start(self):
        self.send_action('spawn')
        self.stream_thread.start()
        self.started = True
    
    def stop(self):
        self.send_action('stop')
    
    def __listen_for_messages(self):
        for data in self.conn.GameStream(self.id_action):
            #print(data)
            self.gotten_data.put(data)
            '''
            print('- - - - - - - - - - -')
            all_items = self.engine.get_items_on_screen(self.id, data)
            self.engine.render_field(all_items)
            '''

    def send_action(self, action):
        if action != '':
            n = game.Action()
            n.id = self.id
            n.direction = action
            print(f'Sending action: {action}')
            self.conn.GameAction(n)

if __name__ == '__main__':
    from sys import argv
    client = None
    if len(argv) == 2:
        client = Client(argv[1], Engine)
    else:
        client = Client('Thomas', Engine)
    while True:
        client.send_action(input())
