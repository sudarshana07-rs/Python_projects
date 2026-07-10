import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def get_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    
    beats = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }
    
    if beats[player] == computer:
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("=== Rock Paper Scissors ===")
    print("Type 'quit' to exit\n")
    
    while True:
        player_choice = input("Enter rock, paper, or scissors: ").lower().strip()
        
        if player_choice == 'quit':
            print("Thanks for playing!")
            break
        
        if player_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice, try again.\n")
            continue
        
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        result = get_winner(player_choice, computer_choice)
        print(result, "\n")

if __name__ == "__main__":
    play_game()
