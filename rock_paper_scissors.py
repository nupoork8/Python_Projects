import random

# ASCII Art
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# -- user input for choices ---
game_images = [rock , paper , scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n"))
print(game_images[user_choice])

# -- computer choice -- 
computer_choice = random.randint(0,2)
print("computer choose : ")
print(game_images[computer_choice])

# --- check conditions and print results accordingly  --- 
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw!")


# What is random.randint?

# 👉 It is a function from Python’s random module
# 👉 Used to generate a random number    
# It gives a random number between start and end (inclusive)

# Think like this:
# You = user input
# Computer = random choice

# 👉 That’s how games work

# 🔥 Real-life analogy:

# It’s like:

# Rolling a dice 🎲
# You don’t know what number will come

# random.randint(0, 2)

# includes both 0 and 2

# 👉 So possible values = 0, 1, 2

# random → module
# randint() → function
# Purpose → generate random number
# Used in games, simulations, testing