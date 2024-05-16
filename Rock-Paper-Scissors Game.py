import random

def play_again():
  """Asks the user if they want to play another round."""
  answer = input("Do you want to play again? (y/n): ").lower()
  return answer == 'y'

def determine_winner(user_choice, computer_choice):
  """Determines the winner based on user and computer choices."""
  # Tie condition
  if user_choice == computer_choice:
    return "Tie"
  # Winning conditions
  elif user_choice == "rock":
    if computer_choice == "scissors":
      return "Win"
    else:
      return "Lose"
  elif user_choice == "paper":
    if computer_choice == "rock":
      return "Win"
    else:
      return "Lose"
  elif user_choice == "scissors":
    if computer_choice == "paper":
      return "Win"
    else:
      return "Lose"
  else:
    return "Invalid Input"  # Handle unexpected user input

def main():
  """Main function to run the game."""
  user_score = 0
  computer_score = 0
  while True:
    # User input
    user_choice = input("Choose rock, paper, or scissors: ").lower()

    # Computer choice
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    # Determine the winner
    result = determine_winner(user_choice, computer_choice)

    # Display results
    print(f"\nYou chose: {user_choice.capitalize()}")
    print(f"Computer chose: {computer_choice.capitalize()}")
    print(f"Result: {result}")

    # Update scores (optional)
    if result == "Win":
      user_score += 1
    elif result == "Lose":
      computer_score += 1

    # Show scores (optional)
    print(f"\nYour score: {user_score}")
    print(f"Computer score: {computer_score}")

    # Play again prompt
    if not play_again():
      break

  print("\nThanks for playing!")

if __name__ == "__main__":
  main()
