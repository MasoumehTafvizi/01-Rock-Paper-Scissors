import random

class RockPaperScissors:
    def __init__(self,name):
        self.name = name
        self.choices = ['rock', 'paper', 'scissors']
         
    def get_player_choice(self):
        user_choice = input("Please choose r(rock), p(paper), or s(scissors): ").lower()
        if user_choice in ['r', 'p', 's']:
            mapping = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
            user_choice = mapping[user_choice]
            return user_choice.lower()
        print("Invalid choice. Please try again.")
        return self.get_player_choice()
    
    def get_computer_choice(self):
        return random.choice(self.choices)
    
    def determine_winner(self, player, computer):
        if player == computer:
            return "It's a tie!"
        win_combinations = {("rock","scissors"),("scissors","paper"),("paper","rock")}
        for win_combination in win_combinations:
            if (player, computer) == win_combination:
                return f"{self.name} , you won!"
        return "Computer wins!"              
    
    def play(self):
        player_choice = self.get_player_choice()
        computer_choice = self.get_computer_choice()
        print(f"{self.name} chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")
        result = self.determine_winner(player_choice, computer_choice)
        print(result)
        
        
if __name__ == "__main__":
    player_name = input("Enter your name: ")
    print(f"'{player_name}' welcome to Rock, Paper, Scissors!")
    game = RockPaperScissors(player_name)
    
    while True:
        game.play()
        continue_game = input("Do you want to play again? Please enter any for continue , Q/q to quit: ")
        if continue_game.lower() == 'q':
            print("Thanks for playing!")
            break