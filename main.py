import random

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

user_input = input("What do you choose?Type 0 for rock, 1 for paper, 2 for scissors")

if user_input == "0":
    print(rock)
elif user_input == "1":
    print(paper)
else :
    print(scissors)

print("Computer chose:")

o1 = [rock, paper, scissors]

numbers = len(o1)
random_choice = random.randint(0, numbers - 1)

print(o1[random_choice])

if user_input == "0" and o1[random_choice] == o1[0]:
    print("Draw")
elif user_input == "0" and o1[random_choice] == o1[1]:
    print("You lose")
elif user_input == "0" and o1[random_choice] == o1[2]:
    print("You win")
elif user_input == "1" and o1[random_choice] == o1[0]:
    print("You win")
elif user_input == "1" and o1[random_choice] == o1[1]:
    print("Draw")
elif user_input == "1" and o1[random_choice] == o1[2]:
    print("You lose")
elif user_input == "2" and o1[random_choice] == o1[0]:
    print("You lose")
elif user_input == "2" and o1[random_choice] == o1[1]:
    print("You win")
else:
    print("Draw")


