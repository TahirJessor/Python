import random

valid = False
p_score = 0
c_score = 0
comp_options = ["rock", "paper", "scissors"]
while True:
	user_round = int(input("How many rounds do you want to play? "))
	if user_round > 0:
		break
	else:
		print("Invalid rounds!")

for round in range(1, user_round+1):
	print(f"Round {round}:")
	while True:
		choice = input("Enter your choice: ").lower()
		if choice == 'rock' or choice == 'paper' or choice == 'scissors':
			break
		else:
			print("Invalid choice!")
	comp_choice = comp_options[random.randint(0,2)]
	print(f"Player: {choice} , Computer: {comp_choice}")
	if choice == 'rock' and comp_choice == 'paper':
		print("Computer scores!")
		c_score += 1
	elif choice == 'paper' and comp_choice == 'rock':
		print("Player scores!")
		p_score += 1	
	elif choice == 'paper' and comp_choice == 'scissors':
		print("Computer scores!")
		c_score += 1
	elif choice == 'scissors' and comp_choice == 'paper':
		print("Player scores!")
		p_score += 1
	elif choice == 'rock' and comp_choice == 'scissors':
		print("Player scores!")
		p_score += 1
	elif choice == 'scissors' and comp_choice == 'rock':
		print("Computer scores!")
		c_score += 1
	else:
		print("No one scored.")
	round += 1
print()
print(f"Player's score: {p_score}")
print(f"Computer's score: {c_score}")	
if p_score > c_score:
	print("the Player wins!")
elif c_score > p_score:
	print("the Computer wins!")
else:
	print("the Game is tied!")