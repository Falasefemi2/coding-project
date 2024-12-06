import random, sys

HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)
BACKSIDE = 'backside'
   
def main():
    money = 5000
    while True:
        if money <= 0:
            print("You are broke")
            print("Good thing you weren't playing with real money.")
            print("Thanks for playing")
            sys.exit()

        # Let the player enter their bet for this round:
        print(f"Money: {money}")
        bet = getBet(money)

        # Give the dealer and player two cards from the deck each:
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        # Handle player's actions:
        print(f"Bet: {bet}")
        while True:
            displayHands(playerHand, dealerHand, False)
            print()

            # Check if the player has busted
            if getHandValue(playerHand) > 21:
                break

            # Get the player's move
            move = getMove(playerHand, money - bet)

            # Handle player actions
            if move == 'H':
                playerHand.append(deck.pop())
                if getHandValue(playerHand) > 21:
                    break  # Player busts; exit loop
            elif move == 'S':
                break  # Player stands; end turn
            elif move == 'D':
                additionalBet = getBet(min(bet, money - bet))
                bet += additionalBet
                print(f"Bet increased to {bet}.")
                playerHand.append(deck.pop())
                break

        # Dealer's turn
        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                print("Dealer hits...")
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)

                if getHandValue(dealerHand) > 21:
                    break
                input("Press Enter to continue...")

        # Final results
        displayHands(playerHand, dealerHand, True)
        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)

        if dealerValue > 21:
            print(f"Dealer busts! You win ${bet}!")
            money += bet
        elif playerValue > 21 or playerValue < dealerValue:
            print("You lost!")
            money -= bet
        elif playerValue > dealerValue:
            print(f"You win ${bet}!")
            money += bet
        else:
            print("It's a tie! The bet is returned to you.")

        input("Press Enter to continue...")
        print('\n\n')

def getBet(maxBet):
     """Ask the player how much they want to bet for ths round"""
     while True:
         print("How much do you bet? (1-{}, or QUIT)".format(maxBet))
         bet = input('> ').upper().strip()
         if bet == 'QUIT':
             
             print("Thanks for playing!")
             sys.exit()
             
         if not bet.isdecimal():
             continue
         
         bet = int(bet)
         if 1 <= bet <= maxBet:
             return bet
         
def getDeck():
    """Return a list of (rank, suit) tuples for all 52 cards"""
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))
        for rank in ('j', 'Q', 'K', 'A'):
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck

def displayHands(playerHand, dealerHand, showDealerHand):
    """Show the player's and dealer's cards. Hide the dealer's first card if showDealerHand is False"""
    print()
    if showDealerHand:
        print('DEALER:', getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print('DEALER: ???')
        # Hide the dealer's first cards:
        displayCards([BACKSIDE] + dealerHand[1:])
    
    # Show the player's cards:
    print('PLAYER:', getHandValue(playerHand))
    displayCards(playerHand)
    
def getHandValue(cards):
    """Returns the value of the cards. Face cards are worth 10, aces are worth 11 or 1 (this function picks the most suitable ace value)"""
    value = 0
    numberOfAces = 0
    
    # Add the value for the non-ace cards:
    for card in cards:
        rank = card[0]
        if rank == 'A':
            numberOfAces += 1
        elif rank in ('K', 'Q', 'J'):
            value += 10
        else:
            value += int(rank)
            
    # Add the value for the aces:
    value += numberOfAces
    for i in range(numberOfAces):
        if value + 10 <= 21:
            value += 10
            
    return value

def displayCards(cards):
    """Display all the cards in the cards lists"""
    rows = ['', '', '', '', '']
    
    for i, card in enumerate(cards):
        rows[0] += '_____ '
        if card == BACKSIDE:
            # print a card's back
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            # Print the card's front
            rank, suit = card
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(rank.rjust(2, "_"))    
            
            # Print each row on the screen
    for row in rows:
        print(row)
        

def getMove(playerHand, money):
    """Asks the player for their move and returns 'H for the hit, S for the stand and D for double down"""
    while True:
        moves = ['(H)it', '(S)tand']
        
        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble down')
            
            movePrompt = ', '.join(moves) + '> '
            move = input(movePrompt).upper()
            if move in ('H', 'S'):
                return move
            if move == 'D' and '(D)ouble down' in moves:
                return move

            
if __name__ == '__main__':
    main()