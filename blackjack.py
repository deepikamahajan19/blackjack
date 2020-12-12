import random
suits=('heart','diamond','spade','club')
values={'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'jack':10,'queen':10,'king':10,'ace':11}
ranks=('one','two','three','four','five','six','seven','eight','nine','ten','jack','queen','king')
playing=True

class Card:
    def __init__(self,rank,suit):
        self.rank=rank
        self.suit=suit

    def __str__(self):
        return (f'{self.rank} of {self.suit}')


class Deck:
    def __init__(self):
        self.all_cards=[]
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(rank,suit))

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal(self):
        card=self.all_cards.pop()
        return card

    def __str__(self):
        deckComp=''
        for card in self.all_cards:
            deckComp+='\n'+card.__str__()
        return deckComp

#class for players
class Hand:
    def __init__(self):
        self.value=0  # total value whwn we add all the cards together
        self.aces=0   # keep record for number of aces
        self.cards=[] #for keeping record what cards a player has in his hands
    #when a player draws a card from deck it is now in his hand so we update
    #player's cards value, add carrd to player's card list an dalso call for
    #adjust for aces
    def add_cards(self,card):
        self.cards.append(card)
        self.value+=values[card.rank]
        if card.rank=='ace':
            self.aces+=1
    #for adjustment of aces
    def adjust_ace(self):
        while self.value >21 and self.aces:
            self.value-=10
            self.aces-=1
    def __str__(self):
        return str(self.value)


class Chips(object):
    def __init__(self,total):
        self.total = total
        self.bet=0

    def win(self,bet):
        self.total+=bet
    def lose(self,bet):
        self.total-=bet

#for taking betting amount from the player
def take_bet(chips):
    while True:
        try:
            chips.bet=int(input('enter betting amount '))
        except:
            print('please enter an integer value')
        else:
            if chips.total<chips.bet:
                print('you dont have enough chips')
            else:
                break
#when a player hits means he want to draw a card from the deck
def hit(deck,hand):
    single_card=deck.deal()     #draw card from deck
    hand.add_cards(single_card) #add this card to player's hand
    print(single_card)
    hand.adjust_ace()           #call for adjjust for aces for player

#ask user for hit or stand
def hit_or_stand(deck,hand):
    global playing
    while True:
        x=input('Hit or Stand press h for hit and s for stand ')
        if x[0].lower()=='h':      #if users choics is hit call hit function
            hit(deck,hand)
        else:
            print()
            print('PLAYER STANDS')  # if he stands break the loop and set playing variable to false
            playing=False
            break

#function for showing cards
#for showing all cards of player and first card of dealer
def show_some(player,dealer):
    print()
    print('PLAYERS CARDS')
    for card in player.cards:
        print(card)
    print()
    print('DEALER CARD')
    print(dealer.cards[0])
#for showing all cards of player's and dealer's
def show_all(player,dealer):
    print()
    print('PLAYERS CARDS')
    for card in player.cards:
        print(card)
    print()
    print('DEALER CARD')
    for card in dealer.cards:
        print(card)

def player_busts(player,dealer,chips):
    print('PALYER BUSTS')
    chips.lose(player_chips.bet)

def player_win():
    print('PLAYER WINS')
    chips.win(player_chips.bet)
def dealer_busts(player,dealer,chips):
    print(' PLAYER WINS! DEALER BUSTED')
    chips.win(player_chips.bet)

def dealer_win():
    print('DEALER WINS! PLAYER BUSTED')
    chips.lose(player_chips.bet)
def push():
    print('PLAYER AND DEALER TIES')
######################
#logic of game
######################

deck=Deck()     #create a deck of cards
deck.shuffle()  #shuffle that deck
player=Hand()   #make a player hand
dealer=Hand()   #make a dealer hand

player_chips=Chips(100)

#make bet
take_bet(player_chips)
#distribute two-two cards to dealer and player
player.add_cards(deck.deal())
player.add_cards(deck.deal())
dealer.add_cards(deck.deal())
dealer.add_cards(deck.deal())
#show all cards of player an done card of dealer
show_some(player,dealer)

while playing:
    hit_or_stand(deck,player)          #ask player to hit or stand
    show_some(player,dealer)           #show all cards of palyer and one dealer card
    #if players value is greater than 21 player losses call player bust method
    if player.value>21:
        player_busts(player,dealer,player_chips)
        break
#if player value is less than 21means its now dealers turn
    if player.value<=21:
        #dealer has to hit if its value is less than 17
        while dealer.value<17:
            hit(deck,dealer)
        show_all(player,dealer)  #show all cards of player and dealer as its now dealer turn
        #decisson making code
        if dealer.value>17:
            dealer_busts(player,dealer,player_chips)
        elif player.value>dealer.value:
            player_win(player,dealer,player_chips)
        elif player.value<dealer.value:
            dealer_wins(player,dealer,player_chips)
        else:
            push()
    print(f'\n player total chips are at {player_chips.total}')
    #asking user to play for another round
    new_game=input('Wouls you like to play another hand? press y for yes n for no ')
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        playing=False
        break
