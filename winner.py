import random

# Accept the input
name1 = input("Enter the first name >> ")
name2 = input("Enter the second name >> ")
name3 = input("Enter the third name >> ")
winnersCircle = []
winnersCircle.append(name1)
winnersCircle.append(name2)
winnersCircle.append(name3)

# Progran will generate a random number in that range
winner = random.choice(winnersCircle)

# Accumulation to keep track of how many times the user makes
print()
print("Congratulations!The winner is: " + winner)