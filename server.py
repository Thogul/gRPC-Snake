from concurrent import futures
from logging import lastResort
import sys
from threading import Thread

import grpc
import time

import protobuffer_pb2 as game
import protobuffer_pb2_grpc as rpc

import db

from engine_revised import Engine
import signal

import prometheus_client
import time
import psutil

class GameServer(rpc.GameServerServicer):
    def __init__(self, engine: Engine, db: db.DB):
        self.snakes = []
        self.engine = engine
        self.db = db

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
    
    def GameScores(self, request: game.Nothing, context) -> game.HighScores:
        high_scores = game.HighScores()
        if self.db is None:
            return high_scores
        #high_scores.extend(self.db.get_scores())
        high_scores.scores.extend(self.db.get_scores())
        return high_scores

def logging_thread():
    UPDATE_PERIOD = 1 #1 sec update period
    SYSTEM_USAGE = prometheus_client.Gauge('system_usage',
                                        'Hold current system resource usage',
                                        ['resource_type'])

    prometheus_client.start_http_server(9999)
    
    while True:
        print('logging stuff')
        SYSTEM_USAGE.labels('CPU').set(psutil.cpu_percent())
        SYSTEM_USAGE.labels('Memory').set(psutil.virtual_memory()[2])
        time.sleep(UPDATE_PERIOD)


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
    engine.generate_outer_walls(100, 100)
    engine.generate_wall(0,-10,0,20)
    
    grpc_server = GameServer(engine, d_b)

    with open('server.key', 'rb') as f:
        private_key = f.read()
    with open('server.crt', 'rb') as f:
        certificate_chain = f.read()
    
    server_credentials = grpc.ssl_server_credentials(
        ((private_key, certificate_chain,),))

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    rpc.add_GameServerServicer_to_server(grpc_server, server)

    #start prometeus rescource logging(only cpu and memory, but should have been more)
    #prometheus_thread = Thread(target=logging_thread, daemon=True)
    #prometheus_thread.start()

    print('Starting server, listening...')

    #server.add_insecure_port('192.168.43.122:' + str(port))
    server.add_secure_port('[::]:' + str(port), server_credentials)
    server.start()
    gameloop = Thread(target=engine.game_loop_thread, daemon=True)
    gameloop.start()

    logging_thread()
    #server.wait_for_termination()
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
