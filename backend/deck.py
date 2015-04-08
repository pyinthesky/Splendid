import random


class Card(object):

    def __init__(self, tier, points, color, black, red, white, blue, green):
        self.tier   = tier
        self.points = points
        self.color  = color
        self.width  = 15
        self.colors = 5
        cost        =   {
                            "black" : black,
                            "red"   : red,
                            "white" : white,
                            "blue"  : blue,
                            "green" : green,
                        }
        self.cost   = {k:v for k, v in cost.items() if v > 0}

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        cost = "|%s|\n" % (' '.ljust(self.width)) * (self.colors - len(self.cost))
        for k,v in self.cost.items():
            c = "%s(%d)" % (k.upper()[0],v)
            cost += "|%s|\n" % c.ljust(self.width)
        point_st = "(%d) %s" % (self.points, "* " * self.tier)
        st  = "\n".join([" %s " % ('-'*self.width),
                         "|%s%s|" % (point_st, self.color.upper().rjust(self.width-len(point_st),' ')),
                         "|%s|" % ('-'*self.width),
                         cost[:-1],
                         " %s " % ('-'*self.width),])
        return st


class Deck(object):

    def __init__(self, card_list):
        self.card_list = card_list
        self.shuffle()
        self.available = []
        for x in range(4):
            self.deal_card()

    def shuffle(self):
        random.shuffle(self.card_list)

    def deal_card(self):
        if len(self.card_list):
            self.available.append( self.card_list.pop() )
        else:
            self.available.append( Card(0, 0, "none", 10, 10, 10, 10, 10) )

class Tier1(Deck):
    def __init__(self):
        card_list = [
                        Card(1, 1, 'red', 0, 0, 4, 0, 0),
                        Card(1, 0, 'red', 3, 1, 1, 0, 0),
                        Card(1, 0, 'red', 0, 0, 3, 0, 0),
                        Card(1, 0, 'red', 1, 0, 2, 1, 1),
                        Card(1, 0, 'red', 2, 0, 2, 0, 1),
                        Card(1, 0, 'red', 1, 0, 1, 1, 1),
                        Card(1, 0, 'red', 0, 0, 0, 2, 1),
                        Card(1, 0, 'red', 0, 2, 2, 0, 0),
                        
                        Card(1, 1, 'white', 0, 0, 0, 0, 4),
                        Card(1, 0, 'white', 1, 2, 0, 0, 0),
                        Card(1, 0, 'white', 1, 1, 0, 1, 2),
                        Card(1, 0, 'white', 1, 1, 0, 1, 1),
                        Card(1, 0, 'white', 0, 0, 0, 3, 0),
                        Card(1, 0, 'white', 1, 0, 0, 2, 2),
                        Card(1, 0, 'white', 2, 0, 0, 2, 0),
                        Card(1, 0, 'white', 1, 0, 3, 1, 0),
                        
                        Card(1, 1, 'black', 0, 0, 0, 4, 0),
                        Card(1, 0, 'black', 0, 1, 1, 1, 1),
                        Card(1, 0, 'black', 0, 1, 0, 0, 2),
                        Card(1, 0, 'black', 0, 0, 0, 0, 3),
                        Card(1, 0, 'black', 1, 3, 0, 0, 1),
                        Card(1, 0, 'black', 0, 1, 1, 2, 1),
                        Card(1, 0, 'black', 0, 0, 2, 0, 2),
                        Card(1, 0, 'black', 0, 1, 2, 2, 0),
                        
                        Card(1, 1, 'blue', 0, 4, 0, 0, 0),
                        Card(1, 0, 'blue', 1, 2, 1, 0, 1),
                        Card(1, 0, 'blue', 2, 0, 0, 0, 2),
                        Card(1, 0, 'blue', 0, 2, 1, 0, 2),
                        Card(1, 0, 'blue', 0, 1, 0, 1, 3),
                        Card(1, 0, 'blue', 2, 0, 1, 0, 0),
                        Card(1, 0, 'blue', 3, 0, 0, 0, 0),
                        Card(1, 0, 'blue', 1, 1, 1, 0, 1),
                        
                        Card(1, 1, 'green', 4, 0, 0, 0, 0),
                        Card(1, 0, 'green', 0, 0, 2, 1, 0),
                        Card(1, 0, 'green', 0, 2, 0, 2, 0),
                        Card(1, 0, 'green', 2, 2, 0, 1, 0),
                        Card(1, 0, 'green', 2, 1, 1, 1, 0),
                        Card(1, 0, 'green', 1, 1, 1, 1, 0),
                        Card(1, 0, 'green', 0, 3, 0, 0, 0),
                        Card(1, 0, 'green', 0, 0, 1, 3, 1)
                     ]
        super(Tier1, self).__init__(card_list)
        self.tier   = 1

class Tier2(Deck):
    def __init__(self):
        card_list = [
                        Card(2, 3, 'red', 0, 6, 0, 0, 0),
                        Card(2, 2, 'red', 0, 0, 1, 4, 2),
                        Card(2, 2, 'red', 5, 0, 0, 0, 0),
                        Card(2, 2, 'red', 5, 0, 3, 0, 0),
                        Card(2, 1, 'red', 3, 2, 0, 3, 0),
                        Card(2, 1, 'red', 3, 2, 2, 0, 0),
                        
                        Card(2, 3, 'white', 0, 0, 6, 0, 0),
                        Card(2, 2, 'white', 3, 5, 0, 0, 0),
                        Card(2, 2, 'white', 0, 5, 0, 0, 0),
                        Card(2, 2, 'white', 2, 4, 0, 0, 1),
                        Card(2, 1, 'white', 0, 3, 2, 3, 0),
                        Card(2, 1, 'white', 2, 2, 0, 0, 3),
                        
                        Card(2, 3, 'black', 6, 0, 0, 0, 0),
                        Card(2, 2, 'black', 0, 2, 0, 1, 4),
                        Card(2, 2, 'black', 0, 0, 5, 0, 0),
                        Card(2, 2, 'black', 0, 3, 0, 0, 5),
                        Card(2, 1, 'black', 2, 0, 3, 0, 3),
                        Card(2, 1, 'black', 0, 0, 3, 2, 2),
                        
                        Card(2, 3, 'blue', 0, 0, 0, 6, 0),
                        Card(2, 2, 'blue', 4, 1, 2, 0, 0),
                        Card(2, 2, 'blue', 0, 0, 5, 3, 0),
                        Card(2, 2, 'blue', 0, 0, 0, 5, 0),
                        Card(2, 1, 'blue', 0, 3, 0, 2, 2),
                        Card(2, 1, 'blue', 3, 0, 0, 2, 3),
                        
                        Card(2, 3, 'green', 0, 0, 0, 0, 6),
                        Card(2, 2, 'green', 0, 0, 0, 5, 3),
                        Card(2, 2, 'green', 0, 0, 0, 0, 5),
                        Card(2, 2, 'green', 1, 0, 4, 2, 0),
                        Card(2, 1, 'green', 2, 0, 2, 3, 0),
                        Card(2, 1, 'green', 0, 3, 3, 0, 2)
                    ]
        super(Tier2, self).__init__(card_list)
        self.tier   = 2


class Tier3(Deck):
    def __init__(self):
        card_list   =   [
                            Card(3, 5,"red",0,3,0,0,7),
                            Card(3, 4,"red",0,0,0,0,7),
                            Card(3, 4,"red",0,3,0,3,6),
                            Card(3, 3,"red",3,0,3,5,3),

                            Card(3, 5,"white",7,0,3,0,0),
                            Card(3, 4,"white",7,0,0,0,0),
                            Card(3, 4,"white",6,3,3,0,0),
                            Card(3, 3,"white",3,5,0,3,3),

                            Card(3, 5,"black",3,7,0,0,0),
                            Card(3, 4,"black",0,7,0,0,0),
                            Card(3, 4,"black",3,6,0,0,3),
                            Card(3, 3,"black",0,3,3,3,5),

                            Card(3, 5,"blue",0,0,7,3,0),
                            Card(3, 4,"blue",0,0,7,0,0),
                            Card(3, 4,"blue",3,0,6,3,0),
                            Card(3, 3,"blue",5,3,3,0,3),

                            Card(3, 5,"green",0,0,0,7,3),
                            Card(3, 4,"green",0,0,0,7,0),
                            Card(3, 4,"green",0,0,3,6,3),
                            Card(3, 3,"green",3,3,5,3,0),
                        ]
        super(Tier3, self).__init__(card_list)
        self.tier   = 3

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        card_str_list = []
        for card in self.available:
            card_str_list.append(card.__str__().split("\n"))
        card_line_list = []
        for x in range(len(card_str_list[0])):  # gives us number of lines
            card_line_list.append('    '.join([st[x].strip('\n') for st in card_str_list]))
        return "\n".join(card_line_list) + "\n\n"


if __name__ == "__main__":
    t3_deck = Tier3()
    print(t3_deck)
    while "y" == input("$ "):
        t3_deck.available.pop(0)
        t3_deck.deal_card()
        print(t3_deck)
