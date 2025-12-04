"""
Author: Masoumeh Tafvizi
Date: 2026-02-04
Description: A simple Rock, Paper, Scissors game
"""

import random
from typing import List, Tuple, Dict

class RockPaperScissors:
    """Main class for the rock paper scissors game
    """
    def __init__(self,name: str):
        self.name: str = name
        self.choices: List[str] = ['rock', 'paper', 'scissors']
         
    def get_player_choice(self) -> str:
        user_choice: str = input("Please choose r(rock), p(paper), or s(scissors): ").lower()
        if user_choice in ['r', 'p', 's']:
            mapping: Dict[str, str] = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
            user_choice: str = mapping[user_choice]
            return user_choice
        print("Invalid choice. Please try again.")
        return self.get_player_choice()
    
    def get_computer_choice(self) -> str:
        """Get computer's random choice
        """
        return random.choice(self.choices)
    
    def determine_winner(self, player: str, computer: str) -> str:
        """Determine the winner of the game 

        :param player: the player's choice  
        :param computer: the computer's choice
        :return: the result of the game
        """
        if player == computer:
            return "It's a tie!"
        win_combinations: List[Tuple[str, str]] = [("rock","scissors"),("scissors","paper"),("paper","rock")]
        for win_combination in win_combinations:
            if (player, computer) == win_combination:
                return f"{self.name} , you won!"
        return "Computer wins!"              
    
    def play(self):
        """Play a round of Rock, Paper, Scissors
        _Get the user's choice
        _Get the computer's choice
        _Determine the winner
        _Print the result
        """
        player_choice: str = self.get_player_choice()
        computer_choice: str = self.get_computer_choice()
        print(f"{self.name} chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")
        result: str = self.determine_winner(player_choice, computer_choice)
        print(result)
        
        
if __name__ == "__main__":
    player_name: str = input("Enter your name: ")
    print(f"'{player_name}' welcome to Rock, Paper, Scissors!")
    game: RockPaperScissors = RockPaperScissors(player_name)
    
    while True:
        game.play()
        continue_game: str = input("Do you want to play again? Please enter any for continue , Q/q to quit: ")
        if continue_game.lower() == 'q':
            print("Thanks for playing!")
            break