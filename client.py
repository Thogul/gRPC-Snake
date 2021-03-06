from sys import maxsize
import threading

import grpc

import protobuffer_pb2 as game
import protobuffer_pb2_grpc as rpc

from engine_revised import Engine
from queue import Queue


address = 'localhost'
port = 50051

class Client():

    def __init__(self, id:str, engine: Engine):
        self.id = id
        self.engine = engine
        self.gotten_data = Queue(maxsize=0)

        with open('server.crt', 'rb') as f:
            trusted_certs = f.read()
        credentials = grpc.ssl_channel_credentials(root_certificates=trusted_certs)
        channel = grpc.secure_channel(address+':'+str(port), credentials)
        self.conn = rpc.GameServerStub(channel)


        #New listening thread for getting messages
        self.id_message = game.Id()
        self.id_message.id = self.id
        threading.Thread(target=self.__listen_for_messages, daemon=True).start()

    def __listen_for_messages(self):
        for data in self.conn.GameStream(self.id_message):
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

    def get_high_scores(self):
        return self.conn.GameScores(game.Nothing())


if __name__ == '__main__':
    from sys import argv
    client = None
    if len(argv) == 2:
        client = Client(argv[1], Engine)
    else:
        client = Client('Thomas', Engine)

    for score in client.get_high_scores().scores:
        print(score.id, score.score)