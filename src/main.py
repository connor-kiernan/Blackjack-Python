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

def rank_to_value(rank):
    if rank in ["Ace", "Jack", "Queen", "King"]:
        return 10
    else:
        return int(rank)

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
        
        if(rank_to_value(players_hand[0][1]) ==
           rank_to_value(players_hand[1][1])):
            options.append("p")
            print("S[p]lit")
            
        if(dealers_hand[0][1] == "Ace"):
            options.append("i")
            print("[I]nsurance")
    
    return options;

def get_player_choice(options):
    player_choice = input().lower;
    
    if player_choice in options:
        return player_choice;
    
    print("Invalid choice")
    return get_player_choice(options)
        
def play_first_turn():
    options = get_and_display_options(True)
    player_choice = get_player_choice(options)
    
    match(player_choice):
            case "h":
                print("hit")
                deal_card(players_hand)
            case "s":
                print("stand")
                # dealer_play()
            case "d":
                print("double down")
                # deal_card(players_hand)
                # # check bust
                # dealer_play()
            case "i":
                print("insurance")
                # insurance_bet()
            case "p":
                print("split")
                # split()
    
        
                
            
            
        
    
    

def main():
    initialise_deck();
    shuffle_deck();
    playing = True;
    
    while(playing):
        deal_initial_hand()
        print(players_hand)
        print(dealers_hand)
        play_first_turn()
        playing = False;
        
        
        
        

if __name__ == "__main__":
    main()




# checkBust
# hit
# doubleDown, cant double down after first turn
# split if cards are same rank, split aces can only double down, split aces + picture = 21, not blackjack
# initialDeal
# stand
# check, blackjack 3 to 2, push
# dealer(playerTotal)
# if dealer gets ace, player can use up to half their stake as insureance, pays 2 to 1
# dealer must draw until >= 17
# sideBets?
