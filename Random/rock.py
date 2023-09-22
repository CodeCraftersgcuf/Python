import random 

def get_choices():
   player_choice= input("Enter a choice: ")
   options =["rock","paper","scissor"]
   computer_choice=random.choice(options)
   choices={"player":player_choice,"computer":computer_choice}
   return choices 

def check_win(player, computer):
	print(f"you Chose {player}, computer chose {computer}")
	if player==computer:
		return "Its a tie! "
	elif player=="rock":
		if computer=="`scissor":
			return "Rock Smashes, You win!"
		else:
			return "paper Covers Rock! You lose."
	elif player=="paper":
		if computer=="rock":
			return "Paper Covers Rock, You win!"
		else:
			return "scissor Cut Paper ! You lose."	
	elif player=="scissor":
		if computer=="paper":
			return "scissor cuts paper, You win!"
		else:
			return "Rock Smashes scissor! You lose."	

choices = get_choices()
result =check_win(choices["player"], choices["computer"])
print(result)