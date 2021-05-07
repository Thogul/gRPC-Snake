from dataclasses import dataclass

@dataclass
class Food():
    x: int
    y: int
    strength: int = 1
    skin: str = 'A'

    def __eq__(self, other):
        return True
        try:
            xbool = other.x == self.head.x
            ybool = other.y == self.head.x
            return xbool and ybool
        except:
            return False
