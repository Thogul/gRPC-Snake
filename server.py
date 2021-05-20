from concurrent import futures
import sys
from threading import Thread

import grpc
import time

import protobuffer_pb2 as game
import protobuffer_pb2_grpc as rpc

import db

from engine_revised import Engine
import signal

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

    with open('server.key', 'rb') as f:
        private_key = f.read()
    with open('server.crt', 'rb') as f:
        certificate_chain = f.read()
    
    server_credentials = grpc.ssl_server_credentials(
        ((private_key, certificate_chain,),))

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    rpc.add_GameServerServicer_to_server(grpc_server, server)

    print('Starting server, listening...')

    #server.add_insecure_port('192.168.43.122:' + str(port))
    server.add_secure_port('[::]:' + str(port), server_credentials)
    server.start()
    gameloop = Thread(target=engine.game_loop_thread, daemon=True)
    gameloop.start()
    server.wait_for_termination()
    
    '''
    try:
        while True:
            signal.pause()
    except KeyboardInterrupt:
        pass
    server.stop(0)
    exit(0)
    
    id = 0
    while True:

        input('Make new snake')
        engine.spawn_snake(str(id))
        id += 1
    '''
