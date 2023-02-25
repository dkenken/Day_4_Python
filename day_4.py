# Exercises Day #4

# Random Module

import random

random_interger = random.randint(1, 20)
print(random_interger)

random_float = random.random()
print(random_float)

# You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".

random_possibility = random.randint(0, 1)

if random_possibility == 0:
    print("Heads")
else:
    print("Tails")

print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")

# My Own Exercise:
# Creating a program where family members will choose which country to visit by using the random module.

# Country list
# 1 = Haiti
# 2 = Japan
# 3 = Brazil
# 4 = Mexico
# 5 = France

random_country = random.randint(1, 5)

if random_country == 1:
    print("Congratulations, we are going to Haiti this summer!")
elif random_country == 2: 
    print('The winner of the day is: "Japan"! ')
elif random_country == 3:
    print("Alert, Alert, You habe won a trip to Brazil!")
elif random_country == 4:
    print("Vamos a Mexico, vamos, vamos!")
else:
    print('Excited? We are going to France, "Country of Love, they say"!' )

print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")

# List # Data structures

fruits = ["apple", "cherry", "watermelon", "banana"]
fruits[1] = "cherries"
print(fruits)

fruits.append("pineapple")
print(fruits)

fruits.extend(["mango", "orange", "grape", "peach"])
print(fruits)

# You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

names_count = len(names)

names_option = random.randint(0, names_count -1)
responsible_person = names[names_option]
print(responsible_person + ' is going to pay for the meal.')

# My Own Exercise

# create a program to pick the winner of a raffle from a list of names.

import random
individual = input("Write each name with a comma and a space in between.\n")
list_individual = individual.split(", ")

individual_count = len(list_individual)
individual_option = random.randint(0, individual_count - 1)
individual_winner= list_individual[individual_option]
print(individual_winner + ' is the winner of the raffle.')

print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")

# IndexErrors and Working with Nested Lists

dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach","Kale", "Tomatoes", "Celery", "Potatoes"]

germs = [fruits, vegetables]
print(germs)

# You are going to write a program that will mark a spot with an X.

row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

horizontal = int(position[0]) 
vertical = int(position[1])

selected_row = map[vertical - 1]
selected_row[horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")

print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")

# Create a Rocker, Paper, Scissors program

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

game_images = [rock, paper, scissors]
import random
user_choice = int(input("What do you choose? type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >= 3 or user_choice < 0:
  print("Invalid number, you lose!")
else:
  print(game_images[user_choice])
  computer_choice = random.randint(0,2)
  print('Computer chose:')
  print(game_images[computer_choice])
  if user_choice == 0 and computer_choice == 2:
    print("You Win!")
  elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
  elif computer_choice > user_choice:
    print("You lose!")
  elif user_choice > computer_choice:
    print("You win!")
  elif user_choice == computer_choice:
    print("Draw")
  elif computer_choice > user_choice:
    print("You lose!")
  elif user_choice >= 3 or user_choice < 0:
    print("Invalid number, you lose!")