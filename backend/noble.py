import random
import json

class Noble (object):

    def __init__(self, points, black, red, white, blue, green):
        self.points = points
        self.cards  =   {
                            'black': black,
                            'red': red,
                            'white': white,
                            'blue': blue,
                            'green': green,
                        }

                      
class NobleDeck(object):

    def __init__(self, noble_count):
        self._noble_list =  [
                                Noble(3, 0, 4, 0, 0, 4),
                                Noble(3, 3, 3, 3, 0, 0),
                                Noble(3, 0, 0, 4, 4, 0),
                                Noble(3, 4, 0, 4, 0, 0),
                                Noble(3, 0, 0, 0, 4, 4),
                                Noble(3, 0, 3, 0, 3, 3),
                                Noble(3, 0, 0, 3, 3, 3),
                                Noble(3, 4, 4, 0, 0, 0),
                                Noble(3, 3, 0, 3, 3, 0),
                                Noble(3, 3, 3, 0, 0, 3),
                            ]
        random.shuffle(self._noble_list)
        self._noble_list = self._noble_list[:noble_count]

    @property
    def noble_list(self):
        return json.dumps(self._noble_list)