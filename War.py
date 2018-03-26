#  File: War.py
#  Description: card game
#  Student's Name: Logan Hashmi
#  Student's UT EID: Sah4334
#  Course Name: CS 313E
#  Unique Number: 51465
#
#  Date Created: 9/23/17
#  Date Last Modified:

import random


class Card():
    # card takes in the SUIT and RANK to create a card
    def __init__(self, Suit, Rank):
        # the if statements replace the integers with string representations
        if Rank == 11:
            self.warRank = Rank  # this variable saves the rank for whenever war is declared
            self.Rank = "J"
            self.Suit = Suit
        elif Rank == 12:
            self.warRank = Rank
            self.Rank = "Q"
            self.Suit = Suit
        elif Rank == 13:
            self.warRank = Rank
            self.Rank = "K"
            self.Suit = Suit
        elif Rank == 14:
            self.warRank = Rank
            self.Rank = "A"
            self.Suit = Suit
        else:
            # this is for all the number cards below Jack
            self.warRank = Rank
            self.Suit = Suit
            self.Rank = Rank

    # a string representation of the card and it's suit
    def __str__(self):
        self.singleCard = str(self.Rank) + str(self.Suit)
        return '{}'.format(self.singleCard)


class Deck():
    # an empty deck is created when the class is initiated
    def __init__(self):
        self.cardList = []

        # the for loop creates 13 cards of each Suits in order
        for i in range(2, 15):
            newCard = Card("C", i)
            self.cardList.append(newCard) # appends the card returned by the Card class to the empty deck

        for jk in range(2, 15):
            newCard = Card("D", jk)
            self.cardList.append(newCard)

        for mn in range(2, 15):
            newCard = Card("H", mn)
            self.cardList.append(newCard)

        for n in range(2, 15):
            newCard = Card("S", n)
            self.cardList.append(newCard)

    # this methods shuffles the deck randomly
    def shuffle(self):
        return random.shuffle(self.cardList)

    # this methods pops one card from the deck and places in the deck of the players
    def dealOne(self, player):
        removedCard = self.cardList.pop(0)
        player.hand.append(removedCard)
        player.handTotal += 1 # this keeps track of total amount of cards the players have

    # returns the string representation format asked by Dr.Bulko
    def __str__(self):
        str1 = ""
        str2 = ""
        str3 = ""
        str4 = ""
        counter = -1
        for i in self.cardList:
            counter += 1
            # loops through the deck and create a string representation of the cards
            if counter < 13:
                if len(str(i)) == 3:
                    str1 = str1+ " " + str(i)
                else:
                    str1 = str1 + "  "+ str(i)
            elif 12 < counter < 26:
                if len(str(i)) == 3:
                    str2 = str2 + " " + str(i)
                else:
                    str2 = str2 + "  " + str(i)
            elif 25 < counter < 39:
                if len(str(i)) == 3:
                    str3 = str3 + " "+ str(i)
                else:
                    str3 = str3 + "  " + str(i)
            else:
                if len(str(i)) == 3:
                    str4 = str4 + " " + str(i)
                else:
                    str4 = str4 + "  " + str(i)

        # returns the strings when the print function is called
        return str1 + "\n" + str2 + "\n" + str3 + "\n" + str4


class Player():
    # each player is starts with an empty hand
    def __init__(self):
        self.hand = []
        self.handTotal = 0

    # same string representation format as the deck class
    def __str__(self):
        str1 = ""
        str2 = ""
        str3 = ""
        str4 = ""
        counter = -1
        for i in self.hand:
            counter += 1
            if counter < 13:
                if len(str(i)) == 3:
                    str1 = str1 + " " + str(i)
                else:
                    str1 = str1 + "  " + str(i)
            elif 12 < counter < 26:
                if len(str(i)) == 3:
                    str2 = str2 + " " + str(i)
                else:
                    str2 = str2 + "  " + str(i)
            elif 25 < counter < 39:
                if len(str(i)) == 3:
                    str3 = str3 + " " + str(i)
                else:
                    str3 = str3 + "  " + str(i)
            else:
                if len(str(i)) == 3:
                    str4 = str4 + " " + str(i)
                else:
                    str4 = str4 + "  " + str(i)

        return str1 + "\n" + str2 + "\n" + str3 + "\n" + str4

    # checks to see if the player has any cards left
    def handNotEmpty(self):
        if self.handTotal >0:
            return True
        return False

    # this function is called whenever the game begins
def playGame(cardDeck,player1,player2):
    # prints out the initial cards the players have
    print("Initial hands:")
    print("Player1:")
    print(player1)
    print("Player2:")
    print(player2)
    roundCounter = 1
    # while loop will only break if any of the players have zero cards
    while player1.handTotal > 0 and player2.handTotal > 0:
        # the top card in the players deck is flipped over
        player1card1 = player1.hand.pop(0)
        player2card1 = player2.hand.pop(0)

        # round starts
        print("ROUND {}:".format(roundCounter))
        print("Player 1 plays:",player1card1)
        print("Player 2 plays:", player2card1,"\n")

        # checks to see if the player one has a higher ranked card
        if player1card1.warRank > player2card1.warRank:
            # adds one card to player1 deck total and subtracts one card from player2
            player1.handTotal+=1
            player2.handTotal-=1
            player1.hand.append(player1card1)
            player1.hand.append(player2card1)

            print("player 1 wins",roundCounter,":",player1card1,">",player2card1)
            roundCounter+=1
            print()
            print("Player 1 now has {} card(s) in hand:".format(player1.handTotal))
            print(player1)
            print("Player 2 now has {} card(s) in hand:".format(player2.handTotal))
            print(player2)

        # this statement does the same thing as above if player2 has a higher ranked card
        elif player1card1.warRank < player2card1.warRank:
            player2.handTotal+=1
            player1.handTotal-=1
            player2.hand.append(player1card1)
            player2.hand.append(player2card1)

            print("player 2 wins",roundCounter,":",player2card1,">",player1card1)
            roundCounter+=1

            print("Player 1 now has {} card(s) in hand:".format(player1.handTotal))
            print(player1)
            print("Player 2 now has {} card(s) in hand:".format(player2.handTotal))
            print(player2)

        # if both cards are equel than war starts again
        elif player1card1.warRank == player2card1.warRank:
            print("War starts:",player1card1,"=",player2card1)

            noWinner = True
            # this while loop runs until a player wins the round
            while noWinner:
                # create a list of the cards played
                firstWarCards = []
                player1card1 = player1card1
                player2card1 = player2card1

                # players cards are taken from the top of the deck and faced down in the field
                p1c1 = player1.hand.pop(0)
                p2c1 = player2.hand.pop(0)
                print("Player 1 puts", p1c1, "face down")
                print("Player 2 puts", p2c1, "face down")


                p1c2 = player1.hand.pop(0)
                p2c2 = player2.hand.pop(0)
                print("Player 1 puts", p1c2, "face down")
                print("Player 2 puts", p2c2, "face down")

                p1c3 = player1.hand.pop(0)
                p2c3 = player2.hand.pop(0)
                print("Player 1 puts", p1c3, "face down")
                print("Player 2 puts", p2c3, "face down")


                p1c4 = player1.hand.pop(0)
                p2c4 = player2.hand.pop(0)

                print("Player 1 puts", p1c4, "face up")
                print("Player 2 puts", p2c4, "face up")
                print()

                # checks to see if player1's rank is higher than player2
                if p1c4.warRank > p2c4.warRank:
                    # updates the total number of cards in each players deck
                    if len(firstWarCards) >0:
                        player1.handTotal += 5
                        player2.handTotal -= 5

                        # adds the cards to the bottom of the players deck
                        for i in firstWarCards[4:]:
                            player1.hand.append(i)
                        for j in firstWarCards[0:4]:
                            player1.hand.append(j)

                    player1.handTotal += 5
                    player2.handTotal -= 5

                    # adds the card in the order played
                    player1.hand.append(player1card1)
                    player1.hand.append(p1c1)
                    player1.hand.append(p1c2)
                    player1.hand.append(p1c3)
                    player1.hand.append(p1c4)

                    player1.hand.append(player2card1)
                    player1.hand.append(p2c1)
                    player1.hand.append(p2c2)
                    player1.hand.append(p2c3)
                    player1.hand.append(p2c4)

                    # prints out the results of the round
                    print("Player 1 wins round",roundCounter,":",p1c4,">",p2c4)
                    roundCounter+=1

                    print("Player 1 now has {} card(s) in hand:".format(player1.handTotal))
                    print(player1)
                    print("Player 2 now has {} card(s) in hand:".format(player2.handTotal))
                    print(player2)

                    # breaks the loop
                    noWinner = False

                # same as above if player 2 wins
                elif p1c4.warRank < p2c4.warRank:
                    if len(firstWarCards) > 0:
                        player2.handTotal += 5
                        player1.handTotal -= 5

                        for i in firstWarCards[0:4]:
                            player2.hand.append(i)
                        for j in firstWarCards[4:]:
                            player2.hand.append(j)

                    player2.handTotal += 5
                    player1.handTotal -= 5

                    player2.hand.append(player1card1)
                    player2.hand.append(p1c1)
                    player2.hand.append(p1c2)
                    player2.hand.append(p1c3)
                    player2.hand.append(p1c4)

                    player2.hand.append(player2card1)
                    player2.hand.append(p2c1)
                    player2.hand.append(p2c2)
                    player2.hand.append(p2c3)
                    player2.hand.append(p2c4)

                    print("Player 2 wins round", roundCounter, ":", p2c4, ">", p1c4)
                    roundCounter += 1
                    print()

                    print("Player 1 now has {} card(s) in hand:".format(player1.handTotal))
                    print(player1)
                    print("Player 2 now has {} card(s) in hand:".format(player2.handTotal))
                    print(player2)

                    noWinner = False

                # if 4th card is the same the war continues and it loops all over again
                elif p1c4.warRank == p2c4.warRank:
                    print("War starts:", p1c4, "=", p2c4)
                    player1card1 = player1.hand.pop(0)
                    player2card1 = player2.hand.pop(0)
                    firstWarCards.append(p1c1)
                    firstWarCards.append(p1c2)
                    firstWarCards.append(p1c3)
                    firstWarCards.append(p1c4)
                    firstWarCards.append(p2c1)
                    firstWarCards.append(p2c2)
                    firstWarCards.append(p2c3)
                    firstWarCards.append(p2c4)

                    continue

    return

def main():
    cardDeck = Deck()  # create a deck of 52 cards called "cardDeck"
    print("Initial deck:")
    print(cardDeck)  # print the deck so we can see that you built it correctly
    print()
    random.seed(15)  # leave this in for grading purposes
    cardDeck.shuffle()  # shuffle the deck
    print("Shuffled deck:")
    print(cardDeck)  # print the deck so we can see that your shuffle worked

    player1 = Player()  # create a player
    player2 = Player()  # create another player


    for i in range(26):  # deal 26 cards to each player, one at
        cardDeck.dealOne(player1)  # a time, alternating between players
        cardDeck.dealOne(player2)

    playGame(cardDeck, player1, player2)
    if player1.handNotEmpty():
        print("\n\nGame over.  Player 1 wins!")
    else:
        print("\n\nGame over.  Player 2 wins!")

    print("\n\nFinal hands:")
    print("Player 1:   ")
    print(player1)  # printing a player object should print that player's hand
    print("\nPlayer 2:")
    print(player2)  # one of these players will have all of the cards, the other none



main()
