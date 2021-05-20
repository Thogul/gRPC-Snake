from concurrent import futures
import sys
from threading import Thread

import grpc
import time

import protobuffer_pb2 as game
import protobuffer_pb2_grpc as rpc

import db

from engine_revised import Engine

class GameServer(rpc.GameServerServicer):
    def __init__(self, engine: Engine):
        self.snakes = []
        self.engine = engine

    def GameStream(self, request, context):
        lastindex = 0
        id = request.id
        while True:
            time.sleep(0.05)
            data = self.engine.data_to_client(id)
            #data = game.Data()
            #data.snakes.extend(self.snakes)
            yield data
    
    def GameAction(self, request: game.Action, context):
        #Move snek!
        self.engine.set_snake_direction(request.id, request.direction)
        print(f'{request.id} moved')
        #self.engine.move_sanek(request.id, request.diretction)
        return game.Nothing()

if __name__ == '__main__':
    port = 50051

    from sys import argv
    d_b = None
    if len(argv) == 2:
        if argv[1] == 'True':
            d_b = db.DB()
    engine = Engine(d_b)
    #engine.spawn_snake('Thomas')
    #engine.foods.append(engine._Engine__new_food(5, 5, '%', 3))
    engine.generate_outer_walls(50, 50)
    grpc_server = GameServer(engine)

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    rpc.add_GameServerServicer_to_server(grpc_server, server)

    print('Starting server, listening...')

    #server.add_insecure_port('192.168.43.122:' + str(port))
    server.add_insecure_port('[::]:' + str(port))
    server.start()
    gameloop = Thread(target=engine.game_loop_thread, daemon=True)
    gameloop.start()
    server.wait_for_termination()
    '''
    id = 0
    while True:

        input('Make new snake')
        engine.spawn_snake(str(id))
        id += 1
    '''
