from game import Game
from character import Goku, Vegita

goku = Goku()
vegita = Vegita()
game = Game(goku, vegita)

game.battle()
