import random
user = input("Enter your choice rock, paper, scissors:\n")
computer_choice = ["rock","paper","scissors"]
computer = random.choice(computer_choice)
print(f"Computer choose {computer}")
# Rock
rock= """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
ascii_art = {
    "rock": rock,
    "paper": paper,
    "scissors": scissors
}
print(f"\nYou chose: {user}")
print(ascii_art[user])        # Print user's ASCII art

print(f"Computer chose: {computer}")
print(ascii_art[computer])    # Print computer's ASCII art

if user == computer:
    print("This is a tie.")
elif user == "rock" and computer =="paper":
    print("You Win !!!")
elif user == "rock" and computer =="scissors":
    print("You Win !!!")
elif user == "paper" and computer == "scissors":
    print("You lose -_-")
elif user == "paper" and computer == "rock":
    print("You Win !!!")
elif user =="scissors" and computer == "rock":
    print("You lose -_-")
elif user == "scissors" and computer =="paper":
    print("You win !!!")




