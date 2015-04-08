class Noble (object):
    def __init__(self, points, black, red, white, blue, green):
        self.cards = {'black': black,
                      'red': red,
                      'white': white,
                      'blue': blue,
                      'green': green}
                      
class NobleDeck(object):
    def __init__(self, number_of_players):
        self.shuffle()
        self.noble_list = [Noble(3, 0, 4, 0, 0, 4),
                           Noble(3, 3, 3, 3, 0, 0),
                           Noble(3, 0, 0, 4, 4, 0),
                           Noble(3, 4, 0, 4, 0, 0),
                           Noble(3, 0, 0, 0, 4, 4),
                           Noble(3, 0, 3, 0, 3, 3),
                           Noble(3, 0, 0, 3, 3, 3),
                           Noble(3, 4, 4, 0, 0, 0),
                           Noble(3, 3, 0, 3, 3, 0),
                           Noble(3, 3, 3, 0, 0, 3)]
        self.available = []
        for x in range(number_of_players+1):
            self.deal_noble()

    def shuffle(self):
        random.shuffle(self.noble_list)

    def deal_noble(self):
        if len(self.noble_list):
            self.available.append( self.noble_list.pop() )
