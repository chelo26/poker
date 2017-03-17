"""
Poker simulation
@ Marcelo Gutierrez
"""

import numpy as np
from collections import defaultdict



class PokerGame:

    def __init__(self):
        # Variables from the poker game: number of players, list of players, deck
        self.number_players = 0
        self.dealer= Dealer()
        self.players = []
        self.deck = Deck()
        self.table = Table()

    def create_players(self,n):
        # Creating a list of Players
        for i in xrange(n):
           self.players.append(Player(i))
        return self.players

    def first_round(self):
        # We start with a constant blind and everybody follows:
        minimum_bet=10
        players_on = defaultdict(list)
        for player in self.players:
            if self.dealer.ask_to_play(player,minimum_bet):
                minimum_bet = self.dealer.ask_to_play(player, minimum_bet)
                players_on[player.player_id].append((player.player_id,minimum_bet))
        return players_on

    def show_cards(self):
        for i in self.players:
            print "player %d, hand %s"%(i.player_id,str(i.hand))
        print "table visible cards: %s"%(str(self.table.visible_cards))
        print "table hidden cards: %s" % (str(self.table.hidden_cards))



class Deck:

    SUITS = {1:"aces",2:"hearts",3:"diamonds", 4:"clubs"}
    VALUES = {2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"10",11:"J",12:"Q",13:"K",14:"A"}

    def __init__(self):
        self.cards=set(self.shuffle())

    def shuffle(self):
        list_cards=[]
        for suit in SUITS:
            for value in VALUES:
                list_cards.append((suit,value))
        return list_cards

    def pop_random_card(self):
        return self.cards.pop()

    def get_remaining_cards(self):
        return len(self.cards)



class Table():
    # Visible and covered cards, get updated by the dealer
    def __init__(self):
        self.visible_cards = []
        self.hidden_cards = []



class Dealer:
    # Dealer will have a deck and will be able to distribute cards
    def __init__(self):
        self.dealer_deck = Deck()

    def distribute_cards(self,list_players, table):
        if len(list_players) ==0:
            print "0 players, create players"
        else:
            for player in list_players:
                # Texas Hold'em, distributes 2 cards:
                player.hand.append(self.dealer_deck.pop_random_card())
                player.hand.append(self.dealer_deck.pop_random_card())

            for i in xrange(3):
                table.visible_cards.append(self.dealer_deck.pop_random_card())
            for i in xrange(2):
                table.hidden_cards.append(self.dealer_deck.pop_random_card())

    def ask_to_play(self,player,minimum_bet,round="first"):
        if round=="first":
            return player.constant_bet(minimum_bet)
        if round=="second":
            player.evaluate_table(visible_table)
            return


class Player:
    def __init__(self,id,money=100):
        self.player_id = id
        self.money = money
        self.hand = []

    def __str__(self):
        return

    def constant_bet(self,minimum_bet):
        if minimum_bet<self.money:
            return minimum_bet

    def update_money(self,amount):
        self.money+=amount

    def evaluate_cards(self,table):
        total_cards = self.hand+table.visible_cards

        # I guess here goes the state evaluation




if __name__=="__main__":

    poker=PokerGame()
    poker.create_players(5)
    poker.dealer.distribute_cards(poker.players,poker.table)
    dictio_bets=poker.first_round()

    poker.show_cards()
