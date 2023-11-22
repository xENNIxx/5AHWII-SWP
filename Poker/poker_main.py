import poker_functions
import poker_plot


draw_count = 5
card_symbols = 13
colors = 4
iterations = 100000


def main():
    deck = poker_functions.create_deck(draw_count, card_symbols, colors)
    combinations = poker_functions.count_wins(iterations, deck)
    poker_functions.print_percent(combinations)
    poker_plot.poker_plot(combinations)


if __name__ == "__main__":
    main()
