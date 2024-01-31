import random
cpu = random.randint(1,3)
user = input("Enter rock, paper, or scissors to try and beat the computer: ")
if cpu == 1:
	if user == ("rock"):
		print("It's a tie :/")
	elif user == ("paper"):
		print("You win !!")
	else:
		print("You lose :(")
if cpu == 2:
	if user == ("rock"):
		print("You lose :(")
	elif user == ("paper"):
		print("It's a tie :/")
	else:
		print("You win !!")
if cpu == 3:
	if user == ("rock"):
		print("You win !!")
	elif user == ("paper"):
		print("You lose :(")
	else:
		print("It's a tie :/")
