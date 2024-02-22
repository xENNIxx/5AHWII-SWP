from collections import Counter
import numpy as np
import random

draw_count = 5
card_symbols = 13
colors = 4


def create_deck(d_count, c_symbols, col):
    draw_count = d_count
    card_symbols = c_symbols
    colors = col
    return list(range(0, (card_symbols * colors) - 1))  # generate Carddeck


def draw_cards(deck):
    random.shuffle(deck)
    return deck[:draw_count]


def get_color(card):
    return card // card_symbols


def get_symbol(card):
    return card % card_symbols


def check_royal_flush(drawn_cards):
    color = get_color(drawn_cards[0])
    for card in drawn_cards[1:]:
        if get_color(card) != color:
            return False

    royal_symbols = np.arange(card_symbols - draw_count - 1, card_symbols - 1)
    for card in drawn_cards:
        if get_symbol(card) not in royal_symbols:
            return False
    return True


def check_straight_flush(drawn_cards):
    color = get_color(drawn_cards[0])
    for card in drawn_cards[1:]:
        if get_color(card) != color:
            return False

    return check_straight(drawn_cards)


def check_flush(drawn_cards):
    color = get_color(drawn_cards[0])
    for card in drawn_cards[1:]:
        if get_color(card) != color:
            return False
    return True


def check_straight(drawn_cards):
    symbols = [get_symbol(card) for card in drawn_cards]
    symbols.sort()
    for i in range(len(symbols) - 1):
        if symbols[i + 1] - symbols[i] != 1:  # check if only 1 difference
            return False
    return True


def check_full_house(drawn_cards):
    return check_3_of_kind(drawn_cards) and check_pair(drawn_cards)


def check_4_of_kind(drawn_cards):
    symbols = [get_symbol(card) for card in drawn_cards]
    symbol_counts = Counter(symbols)  # counts same symbols
    return 4 in symbol_counts.values()


def check_3_of_kind(drawn_cards):
    symbols = [get_symbol(card) for card in drawn_cards]
    symbol_counts = Counter(symbols)
    return 3 in symbol_counts.values()


def check_2_pairs(drawn_cards):
    symbols = [get_symbol(card) for card in drawn_cards]
    symbol_counts = Counter(symbols)
    pairs = list(symbol_counts.values()).count(2)
    return pairs == 2


def check_pair(drawn_cards):
    symbols = [get_symbol(card) for card in drawn_cards]
    symbol_counts = Counter(symbols)
    return 2 in symbol_counts.values()


def check_combination(drawn_cards):
    if check_royal_flush(drawn_cards):
        return "royal_flush"
    elif check_straight_flush(drawn_cards):
        return "straight_flush"
    elif check_4_of_kind(drawn_cards):
        return "4_of_kind"
    elif check_full_house(drawn_cards):
        return "full_house"
    elif check_flush(drawn_cards):
        return "flush"
    elif check_straight(drawn_cards):
        return "straight"
    elif check_3_of_kind(drawn_cards):
        return "3_of_kind"
    elif check_2_pairs(drawn_cards):
        return "2_pairs"
    elif check_pair(drawn_cards):
        return "pair"
    else:
        return "highcard"


def count_wins(iterations, deck):
    combinations = {
        "royal_flush": 0,
        "straight_flush": 0,
        "4_of_kind": 0,
        "full_house": 0,
        "flush": 0,
        "straight": 0,
        "3_of_kind": 0,
        "2_pairs": 0,
        "pair": 0,
        "highcard": 0,
    }
    for i in range(iterations):
        drawn_cards = draw_cards(deck)
        drawn_cards.sort()

        # count hands
        combination = check_combination(drawn_cards)
        combinations[combination] += 1

    return combinations


def print_percent(combinations):
    for key in combinations:
        print(key)
        print(combinations[key] / len(combinations) * 100)
