#Guesser Program

def main():
	print ("Guess a number between 1 and 100.")
	randomNumber = 35

	userGuess = input("Your guess: ")
	if userGuess == randomNumber:
		print ("You got it!")
	else:
		print ("That's not dumbass.")

if __name__ == "__main__":
	main()
