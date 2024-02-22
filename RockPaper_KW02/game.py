import random
import json


def load_statistics(filepath):
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "win": {"rock": 0, "paper": 0, "scissors": 0, "lizard": 0, "spock": 0},
            "tie": {"rock": 0, "paper": 0, "scissors": 0, "lizard": 0, "spock": 0},
            "lose": {"rock": 0, "paper": 0, "scissors": 0, "lizard": 0, "spock": 0},
        }


def save_statistics(statistics, filepath):
    with open(filepath, "w") as f:
        json.dump(statistics, f, indent=4)


def print_statistics(statistics):
    print(json.dumps(statistics, indent=4))


def play(statistics):
    choices = ["rock", "paper", "scissors", "lizard", "spock"]
    outcomes = {
        ("rock", "scissors"): "win",
        ("rock", "lizard"): "win",
        ("rock", "paper"): "lose",
        ("rock", "spock"): "lose",
        ("paper", "rock"): "win",
        ("paper", "spock"): "win",
        ("paper", "scissors"): "lose",
        ("paper", "lizard"): "lose",
        ("scissors", "paper"): "win",
        ("scissors", "lizard"): "win",
        ("scissors", "spock"): "lose",
        ("scissors", "rock"): "lose",
        ("lizard", "spock"): "win",
        ("lizard", "paper"): "win",
        ("lizard", "scissors"): "lose",
        ("lizard", "rock"): "lose",
        ("spock", "scissors"): "win",
        ("spock", "rock"): "win",
        ("spock", "lizard"): "lose",
        ("spock", "paper"): "lose",
    }

    player_choice = input("Choose rock, paper, scissors, spock or lizard: ").lower()
    computer_choice = random.choice(choices)
    print(f"Computer chose {computer_choice}")

    if player_choice == computer_choice:
        result = "tie"
    else:
        result = outcomes.get((player_choice, computer_choice), "invalid")

    statistics[result][player_choice] += 1
    return result
