import game_runner
from game_runner import *

game_player = Game_Runner(1)
try:
    game_player.run()
except IndexError:
    print "YOU WIN"

    
