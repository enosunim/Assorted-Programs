#   WARNING: unholy number of times ':=' is used here
#   walrus-free version coming soon
def acey_deucey() -> None:

    #   importing 'randint()' from 'random' module
    from random import randint as rint

    #   setting up deck of cards
    #   "0": "Joker"
        #   acts as a dummy card
    cards: list(str) = ["0", "Ace"] + [str(_) for _ in range(2, 11)] + ["Jack", "Queen", "King"]

    #   random card generator
        #   returns face card value of card
        #   "0"/"Joker" card not going to get picked
    def random_card() -> str:
        while 1: yield cards[rint(1, len(cards)-1)]

    #   setting up a class for cards
    class Cards:

        #   creates a "Cards" object, which holds the face value
        def __init__(self) -> None:
            self.face: str = next(random_card())

        #   returns face value of card
        def get_face(self) -> str:
            return self.face

        #   compares face value of current card object with another one
            #   gets index value of current card object's face value in deck of cards declared earlier (-> pos)
            #   returns true if other card's face value is found in the sublist containing the first "pos" elements of the deck
        def higher_than(self, card) -> bool:
            return card.get_face() in cards[:(pos := cards.index(self.get_face()))]

    #   current money you have is set to 100 (change it if you want)
    money: int = 100

    #   displays game mechanics
        #   (you can adjust the spacing of the text below however you like)
    print("""Game: Acey-Deucey
-----------------
How to play:
    I'll draw 2 cards (which are never the same, so don't worry about that),
    and you can bet on whether the next card I'll draw will be in between
    these 2 cards.
    
    If you think the 2 cards I drew are not OK with you,
    you can type '0' to skip them, and I'll draw 2 different cards for you.

    The game ends if you go bankrupt, or if you want to stop playing
    (which you can do by typing a negative number).

    If you win, you get back double of the bet you placed.

Easy game, right? Let's go! :D
----------------------------------------------------------------------------
""")

    #   loops as long as you have money
    while money > 0:

        #   loops until the cards have different face values
        while (c1 := Cards()).get_face() == (c2 := Cards()).get_face(): pass
        
        #   displays cards
            #   using chr(10) in f-string as '\n' (and other escape sequences are) not allowed in f-strings
        print("\nCards drawn:")
        print(f"{c1.get_face()}, {c2.get_face()}{chr(10)}")

        #   reads how much you bet
        bet: int = int(input(f"Amount in hand: {money}{chr(10)}Enter amount to bet: "))
        
        #   redraws cards if your bet is 0
        if bet == 0:
            print("\nNot feeling upto it? OK...")
            continue

        #   ends game if your bet is a negative number
        elif bet < 0:
            print("\nHad enough? Alright, thanks for playing. :)")
            break

        #   moment of truth
        #   draws a new card
        c3: Cards = Cards()

        #   displays new card
        print(f"{chr(10)}Card drawn: {c3.get_face()}")

        #   checks if new card is in between the first 2 cards
        #   lose if the card is bigger or smaller than both cards
            #   utilises the 'higher_than()' method created in the 'Cards' class
            #   both are true ---> new card has higer face value than both cards
            #   both are false ---> new card has lower face value than both cards
        if c3.higher_than(c1) == c3.higher_than(c2):
            print("\nUh-oh! This card's not between the first two. I'll take your money now. ;)")
            money -= bet

        #   win (double) otherwise
        else:
            print("\nYou got lucky. Here's your money, and some more.")
            money += bet*2

    #   displays how much money you have (or that you're broke)
        #   says "nice" if money equals 69, cuz why not?
    print(F"{chr(10)}You have {(f'${money} in your pocket.' + (' nice' * (money == 69))) if money > 0 else 'gone broke. Whoops... :P'}")

#   actually starts the game
acey_deucey()
