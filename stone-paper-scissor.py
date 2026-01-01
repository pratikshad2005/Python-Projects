import random
 
# List of valid choices
choices = ["rock", "paper", "scissor"]
 
print("Welcome to the Rock-Paper-Scissors Game!")
print("Instructions: Enter rock, paper, or scissors.\n")
 
while True:
    user_choice = input("Enter your choice (rock, paper, scissor): ").lower()

    if user_choice in ["rock", "paper", "scissor"]:
        print("You chose:", user_choice)
        break
    else:
        print("Invalid choice! Please choose rock, paper, or scissor.")

computer_choice = random.choice(choices)
print("Computer chose:", computer_choice)

if user_choice == computer_choice:
    print("It's a tie!")
elif (
        (user_choice == "rock" and computer_choice == "scissor") or
        (user_choice == "scissor" and computer_choice == "paper") or 
        (user_choice == "paper" and computer_choice == "rock")     
):
    print("You Win!")
else:
    print("computer wins!")