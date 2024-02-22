import functools
import time
import poker_functions as poker

times = {}
draw_count = 5
card_symbols = 13
colors = 4
iterations = 100


def time_calculator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        total_time = end_time - start_time

        if func.__name__ in times:
            times[func.__name__] += total_time / iterations
        else:
            times[func.__name__] = total_time / iterations

        print(f"Function {func.__name__} took {total_time} seconds")
        print(times)
        return result

    return wrapper


def main():
    deck = poker.create_deck(draw_count, card_symbols, colors)
    drawn_cards = poker.draw_cards(deck)
    drawn_cards.sort()
    for i in range(iterations):
        poker.check_royal_flush(drawn_cards)
        poker.check_straight_flush(drawn_cards)
        poker.check_4_of_kind(drawn_cards)
        poker.check_full_house(drawn_cards)
        poker.check_flush(drawn_cards)
        poker.check_straight(drawn_cards)
        poker.check_3_of_kind(drawn_cards)
        poker.check_2_pairs(drawn_cards)
        poker.check_pair(drawn_cards)


if __name__ == "__main__":
    main()
