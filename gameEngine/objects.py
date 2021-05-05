from dataclasses import dataclass

@dataclass
class Food():
    x: int
    y: int
    strength: int = 1
    skin: str = 'A'

@dataclass
class Bodypart():
    x: int
    y: int
    skin: str = 'O'

if __name__ == '__main__':
    body = Bodypart(10, 11)
    print(body)
    food = Food(2, 3)
    print(food)