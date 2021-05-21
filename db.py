from typing import List
from pymongo import MongoClient
import protobuffer_pb2 as game

class DB():
    def __init__(self) -> None:
        
        self.ip = 'db'
        self.port = 27017
        self.client = MongoClient(self.ip, self.port)

        self.d_b = self.client.High_Scores

    def insert_score(self, id, score):
        score = {"id": id, "score": score}
        self.d_b.Scores.insert_one(score)

    def get_scores(self, amount = 5) -> List[game.Score]:
        high_scores = []
        for highscore in self.d_b.Scores.find().sort("score", -1).limit(amount):
            score = game.Score()
            score.id = highscore["id"]
            score.score = highscore["score"]
            high_scores.append(score)
        return high_scores

if __name__ == '__main__':
    db = DB()
    db.insert_score('Thomas', 999999999)
    print(db.get_scores())