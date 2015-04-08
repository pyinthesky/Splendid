import json
import threading

from player import Player
from noble  import NobleDeck
from deck   import get_deck_list


class Chips(object):
    CHIP_BASE = {2:
                    {
                        "black" : 4,
                        "red"   : 4,
                        "white" : 4,
                        "blue"  : 4,
                        "green" : 4,
                        "gold"  : 5,
                    },
                 3:
                    {
                        "black" : 6,
                        "red"   : 6,
                        "white" : 6,
                        "blue"  : 6,
                        "green" : 6,
                        "gold"  : 5,
                    },
                 4:
                    {
                        "black" : 7,
                        "red"   : 7,
                        "white" : 7,
                        "blue"  : 7,
                        "green" : 7,
                        "gold"  : 5,
                    },
                 }
    def __init__(self, player_count):
        self._chip_pool = self.CHIP_BASE[player_count]

    @property
    def chip_pool(self):
        return json.dumps(self._chip_pool)

    @chip_pool.setter
    def chip_pool(self, value):
        self._chip_pool = json.loads(value)


class Board(object):
    def __init__(self, player_count):
        self.deck_list  = get_deck_list()
        self.noble_list = NobleDeck(player_count+1).noble_list
        self.chip_pool  = Chips(player_count)


class Game(threading.Thread):
    def __init__(self, player_name_list):
        super(Game, self).__init__()
        self.player_list = [ Player(player_name) for player_name in player_name_list ]
        self.game_board  = Board(len(self.player_list))

    def run(self):
        pass
