import random
def play_game():
    
  user_choice = input("Choose rock, paper or scissors: ")
  
  computer_choice = random.choice(["rock", "paper", "scissors"])

  if user_choice == computer_choice:
    print("Tie!")
  elif user_choice == "rock" and computer_choice == "paper":
    print("You lose!")
  elif user_choice == "rock" and computer_choice == "scissors":
    print("You win!")
  elif user_choice == "paper" and computer_choice == "rock":
    print("You win!")
  elif user_choice == "paper" and computer_choice == "scissors":
    print("You lose!")
  elif user_choice == "scissors" and computer_choice == "rock":
    print("You lose!")
  elif user_choice == "scissors" and computer_choice == "paper":
    print("You win!")
    
  play_again = input("Do you want to play again? (y/n) ")
  if play_again == "y":
    play_game()

play_game()