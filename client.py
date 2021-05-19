import threading

import grpc

import protobuffer_pb2 as game
import protobuffer_pb2_grpc as rpc

from engine_revised import Engine

address = 'localhost'
port = 50051

class Client():

    def __init__(self, id:str, engine: Engine):
        self.id = id
        self.engine = engine
        channel = grpc.insecure_channel(address+':'+str(port))
        self.conn = rpc.GameServerStub(channel)

        #New listening thread for getting messages
        threading.Thread(target=self.__listen_for_messages, daemon=True).start()

    def __listen_for_messages(self):
        for data in self.conn.GameStream(game.Nothing()):
            #print(data)
            print('- - - - - - - - - - -')
            all_items = self.engine.get_items_on_screen(self.id, data)
            self.engine.render_field(all_items)
            

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
        client = Client(int(argv[1]), Engine)
    else:
        client = Client('Thomas', Engine)
    while True:
        client.send_action(input())
