import random 

words=["GIGABYTE", "AMD", "COMPUTER", "MOUSE"]
word=random.choice(words)

total_chances=7
guessed_word="-"*len(word)
while total_chances!=0:
    print(guessed_word)
    letter=input("Guess a letter: ").upper()
    if letter in word:
        for index in range(len(word)):
            if word[index]==letter:
                guessed_word=guessed_word[:index]+letter+guessed_word[index+1:]

            if guessed_word==word:
                print("Congratulations you guessed the word!!")
                break
        else:
            total_chances -=1
            print("Incorrect Guess:")
            print("The remaining guesses: ",total_chances)
else:
    print("Game over")

print("The Correct Word:",word)   