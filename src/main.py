import random
SUITS = ["♥", "♦", "♣", "♠"]
RANKS = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen",
          "King"]

BASE_DECK = []

deck = []
dealers_hand = []
players_hand = []

def initialise_deck():
    for suit in SUITS:
        for rank in RANKS:
            BASE_DECK.append((suit, rank))
    BASE_DECK.append(("", "JOKER"))
    BASE_DECK.append(("", "JOKER"))
            
def shuffle_deck():
    for _ in range(6):
        copiedDeck = BASE_DECK.copy()
        random.shuffle(copiedDeck)
        deck.extend(copiedDeck)
    random.shuffle(deck)

def rank_to_value(rank, hand):
    if rank == "Ace": #if hand contains an ace, work out if the hand total using Ace as 11 is > 21, if so we can use as as 1
        hand_copy = hand.copy()
        for i in range(len(hand)):
            if hand[i][1] == "Ace":
                hand_copy[i] = (hand[i][0], "11")
        if total(hand_copy) > 21:
            return 1
        return 11
    if rank in ["Jack", "Queen", "King"]:
        return 10
    else:
        return int(rank)

def total(hand):
    total = 0
    for card in hand:
        total += rank_to_value(card[1], hand)
    
    return total;

def deal_card(hand):
    hand.append(deck.pop())

def deal_initial_hand():
    for _ in range(2):
        deal_card(players_hand)
        deal_card(dealers_hand)
        
def get_and_display_options(isFirstTurn):
    options = ["h", "s"]
    print("[H]it")
    print("[S]tand")
    
    if(isFirstTurn):
        options.append("d")
        print("[D]ouble down")
        
        if (rank_to_value(players_hand[0][1], players_hand) ==
           rank_to_value(players_hand[1][1], players_hand)):
            options.append("p")
            print("S[p]lit")
            
        if(dealers_hand[0][1] == "Ace"):
            options.append("i")
            print("[I]nsurance")
    
    return options;

def get_player_choice(options):
    player_choice = input().lower()
    
    if player_choice in options:
        return player_choice
    
    print("Invalid choice")
    return get_player_choice(options)
        
def process_players_turn(isFirstRound):
    if total(players_hand) == 21:
        return False
    
    options = get_and_display_options(isFirstRound)
    player_choice = get_player_choice(options)
    
    match(player_choice):
            case "s":
                print("stand")
                
                return False
            case "d":
                print("double down")
                #doubleBet
                deal_card(players_hand)
                
                return total(players_hand) > 21
            case "h":
                print("hit")
                deal_card(players_hand)
            case "i":
                print("insurance")
                # insurance_bet()
            case "p":
                print("split")
                # split()
    print(players_hand)
    
    if total(players_hand) > 21:
        return True;
    
    return process_players_turn(False)  
            
        
def process_dealers_turn():
    while total(dealers_hand) < 17:
        deal_card(dealers_hand)
    
    return total(dealers_hand) > 21
    
def is_black_jack(hand):
    if len(hand) != 2:
        return False
    
    hand_values = []
    for card in hand:
        hand_values.append(rank_to_value(card[1], hand))
    
    return  sorted(hand_values) == [10,11]
    

def main():
    initialise_deck();
    shuffle_deck();
    playing = True;
    
    while(playing):
        players_hand.clear()
        dealers_hand.clear()
        
        deal_initial_hand()
        print(players_hand)
        print(dealers_hand)
        
        player_has_bust = process_players_turn(True)
        print(players_hand)
        
        if player_has_bust:
            print("Lose")
        else:
            print("Dealer's turn")
            dealer_has_bust = process_dealers_turn()
            print(dealers_hand)

            if dealer_has_bust:
                print("Win")
            else:
                player_turn_total = total(players_hand)
                dealer_turn_total = total(dealers_hand)
                
                if is_black_jack(players_hand) and not(is_black_jack(dealers_hand)):
                    print("Blackjack")
                else:
                    if player_turn_total == dealer_turn_total:
                        print("push")
                    elif player_turn_total > dealer_turn_total:
                        print("win")
                    else:
                        print("lose")
                        
        
        # playing = False;
           

if __name__ == "__main__":
    main()



#check for natural bj
# checkBust
# hit
# doubleDown, cant double down after first turn
# split if cards are same rank, split aces can only double down, split aces + picture = 21, not blackjack
# initialDeal
# stand
# check, blackjack 3 to 2, push = draw
# dealer(playerTotal)
# if dealer gets ace, player can use up to half their stake as insureance, pays 2 to 1
# dealer must draw until >= 17
# sideBets?
