from concurrent import futures

import grpc
import time

import protobuffer_pb2 as game
import protobuffer_pb2_grpc as rpc

from engine_revised import Engine

class GameServer(rpc.GameServerServicer):
    def __init__(self, engine: Engine):
        self.snakes = []
        self.engine = engine

    def GameStream(self, request_iterator, context):
        lastindex = 0

        while True:
            time.sleep(0.05)
            data = self.engine.data_to_client()
            #data = game.Data()
            #data.snakes.extend(self.snakes)

            yield data
    
    def GameAction(self, request: game.Action, context):
        print(f'{request.id} generated new snek')
        #self.engine.move_sanek(request.id, request.diretction)
        snake = game.Snake()
        snake.head.x = 0
        snake.head.y = 0
        snake.head.skin = '@'
        body = game.Object()
        body.x = 0
        body.y = -1
        body.skin = 'O'
        snake.body.append(body)

        self.snakes.append(snake)
        return game.Nothing()

if __name__ == '__main__':
    port = 50051


    engine = Engine()
    engine.spawn_snake('Thomas')
    grpc_server = GameServer(engine)

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    rpc.add_GameServerServicer_to_server(grpc_server, server)

    print('Starting server, listening...')

    server.add_insecure_port('[::]:' + str(port))
    server.start()
    #server.wait_for_termination()

    while True:
        input('Make new snake')
        engine.spawn_snake()
