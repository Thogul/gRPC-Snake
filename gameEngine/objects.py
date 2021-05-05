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