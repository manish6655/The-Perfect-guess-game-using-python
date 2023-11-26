import random
randNumber = random.randint(1, 50)
userGuess = None
guesses = 0

while(userGuess != randNumber):
    userGuess = int(input("Enter your guesses: "))
    guesses += 1
    if(userGuess==randNumber):
        print("You guessed it right!")
    else:
        if(userGuess>randNumber):
            print("You guessed it wrong! Enter a smaller number")
        else:
            print("You guessed it wrong! Enter a larger number")

print(f"you guessed the number in {guesses} guesses")
with open("C:\stpython\project2\score.txt", "r") as f:
    Highscore = int(f.read())

if(guesses>Highscore):
    print("you have just broken the highscore!")
    with open("C:\stpython\project2\score.txt", "w") as f:
        f.write(str(guesses))
        