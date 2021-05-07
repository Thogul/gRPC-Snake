from dataclasses import dataclass

@dataclass
class Bodypart():
    x: int
    y: int
    skin: str = 'O'

    def __eq__(self, other):
        try:
            if self.x == other.x:
                if self.y == other.y:
                    return True
                else:
                    return False
            else:
                return False
        except:
            return False