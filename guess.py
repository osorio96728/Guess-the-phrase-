import random

name = input("enter a nickname here:")
word = ['rainbow', 'cellular', 'youtube', 'lightning',
                'math', 'paper', 'letters', 'poke', 'sushi']
words = random.choice(word)

print ("Good Luck", name)



print("guess the characters")

guesses = ''

turns = 12

while turns >0 :
    failed =0

    for char in word:

        if char in guesses:
            print (char)
        else :
            print("_")


            failed += 1

        if failed == 0:

            print("You wiiiiinnnn!!")

            print("The word is: ", word)
            break

        guess = input ("guess a character: ")
        guesses += guess

        if guess not in word:
            turns -= 1

            print ("Wrong")

            print ("You have", + turns, "to try again")

            if turns == 0:
                print ("You loose :(")





