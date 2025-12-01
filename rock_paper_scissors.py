"""
Rock, Paper, Scissors Game

A Python-based implementation of the popular game "Rock, Paper, Scissors".
Play against the computer which makes its moves based on random choice.
"""

import random


VALID_CHOICES = ["rock", "paper", "scissors"]


def get_computer_choice():
    """Generate a random choice for the computer."""
    return random.choice(VALID_CHOICES)


def determine_winner(player_choice, computer_choice):
    """
    Determine the winner of a round.

    Args:
        player_choice: The player's choice (rock, paper, or scissors)
        computer_choice: The computer's choice (rock, paper, or scissors)

    Returns:
        A string indicating the result: "win", "lose", or "tie"
    """
    if player_choice == computer_choice:
        return "tie"

    winning_combinations = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

    if winning_combinations[player_choice] == computer_choice:
        return "win"
    return "lose"


def get_player_choice():
    """Get and validate the player's choice."""
    while True:
        choice = input("Enter your choice (rock, paper, scissors) or 'quit' to exit: ").lower().strip()
        if choice == "quit":
            return None
        if choice in VALID_CHOICES:
            return choice
        print(f"Invalid choice. Please choose from: {', '.join(VALID_CHOICES)}")


def display_result(player_choice, computer_choice, result):
    """Display the result of a round."""
    print(f"\nYou chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")

    if result == "tie":
        print("It's a tie!")
    elif result == "win":
        print("You win!")
    else:
        print("You lose!")


def play_game():
    """Main game loop."""
    print("=" * 40)
    print("Welcome to Rock, Paper, Scissors!")
    print("=" * 40)

    wins = 0
    losses = 0
    ties = 0

    while True:
        player_choice = get_player_choice()

        if player_choice is None:
            break

        computer_choice = get_computer_choice()
        result = determine_winner(player_choice, computer_choice)

        display_result(player_choice, computer_choice, result)

        if result == "win":
            wins += 1
        elif result == "lose":
            losses += 1
        else:
            ties += 1

        print(f"\nScore - Wins: {wins}, Losses: {losses}, Ties: {ties}\n")

    print("\n" + "=" * 40)
    print("Thanks for playing!")
    print(f"Final Score - Wins: {wins}, Losses: {losses}, Ties: {ties}")
    print("=" * 40)


if __name__ == "__main__":
    play_game()
