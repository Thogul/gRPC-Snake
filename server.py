from concurrent import futures
from threading import Thread

import grpc
import time

import protobuffer_pb2 as game
import protobuffer_pb2_grpc as rpc

from engine_revised import Engine

import db

class GameServer(rpc.GameServerServicer):
    def __init__(self, engine: Engine, db:db.DB=None):
        self.snakes = []
        self.db = db
        self.engine = engine
        #nasty way to set db, but w/e
        self.engine.db = self.db

    def GameStream(self, request_iterator, context) -> game.Data:
        lastindex = 0

        while True:
            time.sleep(0.05)
            data = self.engine.data_to_client()
            #data = game.Data()
            #data.snakes.extend(self.snakes)

            yield data
    
    def GameAction(self, request: game.Action, context) -> game.Nothing:
        #Move snek!
        self.engine.set_snake_direction(request.id, request.direction)
        print(f'{request.id} moved')
        #self.engine.move_sanek(request.id, request.diretction)
        return game.Nothing()

    def GameScores(self, request, context) -> game.HighScores:
        High_Scores = game.HighScores()
        if self.db is not None:
            High_Scores.scores.extend(db.get_scores())
        return High_Scores

if __name__ == '__main__':
    port = 50051

    db = db.DB()
    engine = Engine()
    #engine.spawn_snake('Thomas')
    #engine.foods.append(engine._Engine__new_food(5, 5, '%', 3))
    engine.generate_outer_walls(50, 50)
    grpc_server = GameServer(engine, db)

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    rpc.add_GameServerServicer_to_server(grpc_server, server)

    print('Starting server, listening...')

    #server.add_insecure_port('192.168.43.122:' + str(port))
    server.add_insecure_port('[::]:' + str(port))
    server.start()
    gameloop = Thread(target=engine.game_loop_thread, daemon=True)
    gameloop.start()
    server.wait_for_termination()
    exit(0)
    '''
    id = 0
    while True:

        input('Make new snake')
        engine.spawn_snake(str(id))
        id += 1
    '''
