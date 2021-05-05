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


if __name__ == '__main__':
    body = Bodypart(5, 5)
    #print(body)
    food = Food(5, 5)
    #print(food)
    print(body == food)