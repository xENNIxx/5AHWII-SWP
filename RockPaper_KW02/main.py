import game


def main():
    print("Welcome to Rock, Paper, Scissors, Lizard, Spock!")
    statistics = game.load_statistics("game_statistics.json")
    player, computer = 0, 0
    mode = input("Do you want to play or view statistics? (p/s)?")
    while mode not in ["p", "s"]:
        mode = input("Please enter p or s: ")
    if mode == "s":
        print(game.print_statistics(statistics))
        return
    rounds = input("How many rounds do you want to play? ")
    while not rounds.isdigit():
        rounds = input("Please enter a number: ")
    rounds = int(rounds)
    while rounds <= 0:
        rounds = int(input("Please enter a positive number: "))

    for i in range(rounds):
        result = game.play(statistics)
        if result == "win":
            print("You win!")
            player += 1
        elif result == "lose":
            print("You lose!")
            computer += 1
        else:
            print("It's a tie!")
    print(f"Player: {player} Computer: {computer}")

    game.save_statistics(statistics, "game_statistics.json")


if __name__ == "__main__":
    main()
