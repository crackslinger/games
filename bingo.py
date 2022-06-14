""" Bingo-CLI simple game """
import random
import time

class BingoCage:

    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        for i in range(36):
            yield self._items.pop()
            time.sleep(1)

    def show(self):
        for value in self.pick():
            print(value)

def game():
    r = 1
    while True:
        balls = [i for i in range(1, 49)]
        bingo = BingoCage(balls)
        print("*********************************************")
        print("*                                           *")
        print(f"*                GAME {r}                     *")
        print("*                                           *")
        print("*********************************************")
        bingo.show()
        print(f"Balls that didn't come out this turn: {bingo._items}")
        r += 1

        time.sleep(5)




if __name__ == '__main__':
    game()

