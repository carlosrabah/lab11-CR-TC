import p1_random as p1
rng = p1.P1Random()

stats = {"player_wins": 0, "dealer_wins": 0, "ties": 0}

def player_card(card_number, hand_number, x, stats):
    if card_number == 1:
        card_number = "ACE"
    elif card_number == 11:
        card_number = "JACK"
    elif card_number == 12:
        card_number = "QUEEN"
    elif card_number == 13:
        card_number = "KING"

    print(f"""\nYour card is a {card_number}!
Your hand is: {hand_number}""")

    if hand_number == 21:
        print("\nBLACKJACK! You win!")
        stats["player_wins"] += 1
        start_game(x, stats)
    elif hand_number > 21:
        print("\nYou exceeded 21! You lose.")
        stats["dealer_wins"] += 1
        start_game(x, stats)
    else:
        while True:
            selection = int(input(f"""\n1. Get another card
2. Hold hand
3. Print statistics
4. Exit
\nChoose an option:  """))

            if selection == 1:
                card_number = rng.next_int(13) + 1

                if card_number > 10:
                    hand_number += 10
                else:
                    hand_number += card_number

                player_card(card_number, hand_number, x, stats)
                break
            elif selection == 2:
                dealer_card(hand_number, x, stats)
                break
            elif selection == 3:
                percentage = (stats["player_wins"] / (stats["player_wins"] + stats["dealer_wins"] + stats["ties"])) * 100
                print(f"""\nNumber of Player wins: {stats["player_wins"]}
Number of Dealer wins: {stats["dealer_wins"]}
Number of tie games: {stats["ties"]}
Total # of games played is: {stats["player_wins"] + stats["dealer_wins"] + stats["ties"]}
Percentage of Player wins: {percentage:.1f}%""")
            elif selection == 4:
                return False
            else:
                print("""Invalid input!
Please enter an integer value between 1 and 4.""")

def dealer_card(hand_number, x, stats):
    dealer_number = rng.next_int(11) + 16

    if dealer_number > 21:
        result = "You win!"
        stats["player_wins"] += 1

    elif dealer_number < 21:
        if dealer_number > hand_number:
            result = "Dealer wins!"
            stats["dealer_wins"] += 1
        elif dealer_number < hand_number:
            result = "You win!"
            stats["player_wins"] += 1
        elif dealer_number == hand_number:
            result = "It's a tie! No one wins!"
            stats["ties"] += 1
    elif dealer_number == 21:
        result = "Dealer wins!"
        stats["dealer_wins"] += 1

    print(f"""\nDealer's hand: {dealer_number}
Your hand is: {hand_number}

{result}""")

    start_game(x, stats)

def start_game(x, stats):
    print(f"\nSTART GAME #{x}")
    card_number = rng.next_int(13) + 1
    hand_number = 0

    if card_number > 10:
        hand_number += 10
    else:
        hand_number += card_number

    x += 1
    player_card(card_number, hand_number, x, stats)

start_game(1, stats)