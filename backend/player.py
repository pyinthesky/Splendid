import json

class Player(object):
    def __init__(self, player_name):
        self.player_name            = player_name
        self.player_score           = 0
        self.player_victory_count   = 0
        self.player_tableau         = []
        self.player_hand            = []
        self.player_chips           =   {
                                            "black" : 0,
                                            "red"   : 0,
                                            "white" : 0,
                                            "blue"  : 0,
                                            "green" : 0,
                                        }

    def get_player_info(self):
        return json.dumps(self.__dict__)