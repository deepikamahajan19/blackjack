# blackjack

class deck
there is a deck class in which i create a deck of 52 cards for this pirpose it uses global variables- suits and ranks
ths deck ckass has shuffle method t shuffle the cards created in this deck
this class also has a method for card drawn 

class card
this card just print the string reprenstation of card and also it is useful to create a card object whuch is used in deck creation 

class hand
this class served purpose of hands in which cards are placed after being drawn from deck 
I created two instances of this class one called player and other called dealer
each instance of this class has total, list of cards and no of aces attributes
methods of this class include add a card to hands and adjustment for aces 

class chips
this class has betting amount and total number of chips a hand has 
methods of this class are win bet and loss bet

we take bet from user using a method called bet
we have hit or stand function in which user gives input whether he wants to hit or stand 
if he chose hit we have a hit method in which a card is drawn from deck tahn add this card to hand of player or dealer

create a deck
shuffle it
take betting amount from user
distribute two cards to player and two cards to dealer 
show all cards of player and one card of dealer
ask user to hit or stand 
if user stands its dealers turn 
dealer has to hit untill his value is less than 17
than acc to values declare winner and call apporopirate method
