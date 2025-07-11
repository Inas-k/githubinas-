import random

choices = ["rock", "paper", "scissors"]

def get_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

while True:
    print("\n--- Rock Paper Scissors ---")
    player_choice = input("Choose rock, paper, or scissors (or 'exit' to quit): ").lower()
    if player_choice == "exit":
        break
    if player_choice not in choices:
        print("Invalid choice. Try again.")
        continue
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    print(get_winner(player_choice, computer_choice))
