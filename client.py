import threading

import grpc

import protobuffer_pb2 as game
import protobuffer_pb2_grpc as rpc


address = 'localhost'
port = 50051

class Client():

    def __init__(self, id):
        self.id = id
        channel = grpc.insecure_channel(address+':'+str(port))
        self.conn = rpc.GameServerStub(channel)

        #New listening thread for getting messages
        threading.Thread(target=self.__listen_for_messages, daemon=True).start()

    def __listen_for_messages(self):
        for data in self.conn.GameStream(game.Nothing()):
            #print(data)
            
            print('----------')
            for snake in data.snakes:
                print(f'snake @{snake.head.x}{snake.head.y}\nbody O{snake.body[0].x}{snake.body[0].x}')
            

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
        client = Client(int(argv[1]))
    else:
        client = Client(42)
    while True:
        client.send_action(input())
