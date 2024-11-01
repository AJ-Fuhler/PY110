import random
import time
import os

SUITS = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
         'Jack', 'Queen', 'King', 'Ace']
MAX_TOTAL = 21
MAX_TOTAL_DEALER_TURN = 17

def join_or(lst, delimiter=', ', final_delimiter='or'):
    result = ''

    for element in lst[:-2]:
        result += f'{element}{delimiter}'
    if len(lst) > 1:
        result += f'{lst[-2]} {final_delimiter} {lst[-1]}'
    elif len(lst) == 1:
        return str(lst[0])


    return result

def prompt(message):
    print(f'==> {message}')

def initialize_deck():
    deck = [f'{rank} of {suit}' for suit in SUITS
                         for rank in RANKS]
    random.shuffle(deck)

    return deck



def deal_cards(deck, num_cards):
    cards = []
    for _ in range(num_cards):
        card = deck[0]
        cards.append(card)
        deck.remove(card)

    return cards

def calculate_card_value(cards):
    card_values = []
    for card in cards:
        if card[0].isdigit() and not card[1].isdigit():
            card_values.append((card[0]))
        elif 'Ace' in card:
            card_values.append('Ace')
        else:
            card_values.append('10')

    return card_values

def display_player_cards(player_cards):
    player_card_vals = join_or(calculate_card_value(player_cards), ', ', 'and')
    prompt(f'You have: {player_card_vals}')

def display_dealer_cards(dealer_cards, hidden=True):
    dealer_card_vals = calculate_card_value(dealer_cards)
    if hidden:
        prompt(f'Dealer has: {dealer_card_vals[0]} and unknown card')
    else:
        prompt(f'Dealer has: {join_or(dealer_card_vals, ', ', 'and')}')



def calculate_total(cards):
    cards = calculate_card_value(cards)
    total = 0
    if 'Ace' in cards:
        ace_index = cards.index('Ace')
        cards.append(cards.pop(ace_index))
    for card in cards:
        if card == 'Ace':
            if total <= 10:
                total += 11
            else:
                total += 1
        else:
            total += int(card)

    return total

def busted(cards):
    return calculate_total(cards) > MAX_TOTAL

def get_valid_answer(valid_options):
    answer = input().strip().lower()
    while answer not in valid_options:
        prompt('Please choose a valid option')
        answer = input().strip().lower()

    return answer

def determine_winner(player_cards, dealer_cards):
    player_total = calculate_total(player_cards)
    dealer_total = calculate_total(dealer_cards)
    if player_total > dealer_total:
        return 'You'
    if player_total < dealer_total:
        return 'The dealer'

    return None

def display_totals(player_cards, dealer_cards):
    player_total = calculate_total(player_cards)
    dealer_total = calculate_total(dealer_cards)
    prompt(f'You had a total of {player_total}.')
    prompt(f'The dealer had a total of {dealer_total}.')



def display_winner(player_cards, dealer_cards):
    winner = determine_winner(player_cards, dealer_cards)
    if winner:
        prompt(f'{winner} won!')
    else:
        prompt('You tied!')



def play_twenty_one():
    while True:
        while True:
            os.system('clear')
            deck = initialize_deck()
            player_cards = deal_cards(deck, 2)
            dealer_cards = deal_cards(deck, 2)
            display_dealer_cards(dealer_cards)
            while True:
                display_player_cards(player_cards)
                prompt(f'Your total is {calculate_total(player_cards)}')
                if busted(player_cards):
                    break
                prompt('hit or stay? (h or s)')
                answer = get_valid_answer(['hit', 'stay', 'h', 's'])

                if answer in ['stay', 's'] or busted(player_cards):
                    break
                player_cards += deal_cards(deck, 1)

            if busted(player_cards):
                prompt('You busted! The dealer won!')
                time.sleep(1.5)
                break

            else:
                prompt('You chose to stay!')
                time.sleep(1.5)
                prompt(f'Your total is {calculate_total(player_cards)}')
                time.sleep(1.5)
                while True:
                    display_dealer_cards(dealer_cards, False)
                    prompt(f'Dealer total: {calculate_total(dealer_cards)}')
                    time.sleep(1.5)
                    if calculate_total(dealer_cards) >= MAX_TOTAL_DEALER_TURN:
                        break
                    dealer_cards += deal_cards(deck, 1)
                    time.sleep(1.5)

                if busted(dealer_cards):
                    prompt('The dealer busted! You won!')
                    time.sleep(1.5)
                    break
                else:
                    prompt('The dealer stayed.')
                    time.sleep(1.5)
                    display_totals(player_cards, dealer_cards)
                    display_winner(player_cards, dealer_cards)
                    time.sleep(1.5)
                    break

        prompt('Play again? (y or n)')
        answer = get_valid_answer(['y', 'n'])
        if answer == 'n':
            break


    prompt('Thanks for playing twenty one!')

play_twenty_one()