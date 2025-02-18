from game import Game
from settings import LEVELS

if __name__ == "__main__":
    for level in LEVELS:
        game = Game(level)
        game.run()