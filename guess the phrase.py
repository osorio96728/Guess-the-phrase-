#This program is to play a little guess game, the instructions are clear you should guess the color
import json

print ('********************************************************************************************\n'
       '********************************************************************************************\n'
       '*********************** WELCOME TO GUESS THE PHRASE: THE GAME *******************************\n'
       '********************************************************************************************\n'
       '********************************************************************************************\n')
#The instructions are simple, you'll guess a phrase and depending if its a vowel or a consonant it will pay you a
# price.

print ('Instructions: each there are two sets of players, the computer and the human. Each starts with\n'
       'zero points, each vowel will cost 500 points, and each consonant will cost 1500.\n\n'
       '                                   GOOD LUCK')
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'
VOWEL_COST = 250

def __init__(self, name, difficulty):
       self.name = name
       self.prizeMoney = 0
       self.prizes = []
       self.difficutly = difficulty

def addMoney (self, amt):
       self.prizeMoney += amt

def goBankrupt (self):
       self.prizeMoney = 0

def addPrize (self, prize):
       self.prizes.append(prize)

def __str__ (self):
       return "{} (${})".format(self.name,self.prizeMoney)

def getMove (self,category, obscuredPhrase, guessed):
       print ("{} has (${})".format(self.name,self.prizeMoney))

       print ('Category:', category)
       print ("Phrase:", obscuredPhrase)
       print ("Guessed:", guessed)

       theChoose = str(input("Guess a letter, phrase, or type 'exit' or 'pass':"))
       return theChoose

def smartCoinFlip (self):
       rand_number = random.randint (1, 10)
              if rand_number > self.difficulty:
                  return True

              elif
                  return False
def getPossibleLetters (self, guessed):
       CanBeGuessed = []
       for letter in LETTERS:
              if letter not in guessed and letter not in VOWELS :
                     CanBeGuessed.append(letter)
              elif letter not in guessed and letter in VOWELS:
                     if self.prizeMoney > VOWEL_COST:
                            CanBeGuessed.append(letter)

       return CanBeGuessed
def getMove (self, category, obscuredPhrase, guessed):
       CanBeGuessed = self.getPossibleletters (guessed)
       if CanBeGuessed ==[]:
              return 'pass'
       else:
              the_value = self.smartCoinFlip()
              if the_value == True:
                     i = len(self.SORTED_FREQUENCIES)-1
                     while (0 <= i <= len(self.SORTED_FREQUENCIES)-1)
                            if self.SORTED_FREQUENCIES [i] in CanBeGuessed:
                                   return self.SORTED_FREQUENCIES [i]
                            else:
                                   i-=1
                                   continue
                     else:
                            rand_letter = random.choice(CanBeGuessed)
                            return rand_letter
def getNumberBetween (prompt, min, max):
       userinp = input(prompt)

       while True:
              n = int(userinp)
              if n< min:
                     errmessage = 'Must be atleast {}'.format (min)
              elif n> max:
                     errmessage = 'Must be at most {}'.format(max)
              else:
                     return n
              except ValueError:
              errmessage = "{} is not a number.".format(userinp)


              userinp = input ("{}\n{}".format (errmessage, prompt))


def spinWheel ():
       with open ("wheel.json", "r") as f:
              wheel = json.loads(f.read())
              return random.choice(wheel)
def getRandomCategoryAndPhrase():
       with open("phrases.json","r") as f:
              phrases = json.loads(f.read())


              category = random.choice(list(phrases.keys()))
              phrase = random.choice(phrases[category])
              return (category, phrase.upper())



  def obscurePhrase (phrase, guessed):
         rv = ''
         for s in phrase:
                if (s in LETTERS) and (s not in guessed):
                       rv = rv + '_'
                else:
                       rv = rv + s

         return rv

  def showBoard (category, obscuredPhrase, guessed):
         return """
  Category: {}
  Phrase: {}
  Guessed: {}""".format(category, obscuredPhrase, ',',join(sorted(guessed)))


print ('='*15)
print ('GUESS THE WORD')
print ('='*15)
print ('')

num_human = getNumberBetween('How many human players?', 0, 10)


num_computer = getNumberBetween('How many computer players?', 0, 10)

if num_computer >= 1:
       difficulty = getNumberBetween('What difficulty for the computers? (1-10')

players = human_players + computer_players


if len(players) == 0:
       print ('We need players to play!')
       raise Exception ('Not enough players')


category, phrase = getRandomCategoryAndPhrase()

guessed =[]


playerIndex =0

winner = False

def requestPlayerMove(player, category, guessed):
    while True:
        time.sleep(0.1)

        move = player.getMove(category, obscurePhrase(phrase, guessed), guessed)
        move = move.upper()
        if move == 'EXIT' or move == 'PASS':
                return move
                       elif len(move) == 1:
                       if move not in LETTERS: 
                                print('Guesses should be letters. Try again.')
                                continue
                       elif move in guessed:
                            print('{} has already been guessed. Try again.'.format(move))
                            continue
                       elif move in VOWELS and player.prizeMoney < VOWEL_COST:
                            print('Need ${} to guess a vowel. Try again.'.format(VOWEL_COST))
                            continue
                        else:
                            return move
                else:
                     return move

while True:
    player = players[playerIndex]
    wheelPrize = spinWheel()

    print('')
    print('-'*15)
    print(showBoard(category, obscurePhrase(phrase, guessed), guessed))
    print('')
    print('{} spins...'.format(player.name))
    time.sleep(2)
    print('{}!'.format(wheelPrize['text']))
    time.sleep(1)
    if wheelPrize['type'] == 'bankrupt':
            player.goBankrupt()
    elif wheelPrize['type'] == 'loseturn':
        pass
    elif wheelPrize['type'] == 'cash':
        move = requestPlayerMove(player, category, guessed)
        if move == 'EXIT':
            print('Until next time!')
            break
        elif move == 'PASS':
            print('{} passes'.format(player.name))
        elif len(move) == 1:
            guessed.append(move)

            print('{} guesses "{}"'.format(player.name, move))

            if move in VOWELS:
                player.prizeMoney -= VOWEL_COST

            count = phrase.count(move)
            if count > 0:
                    if count == 1:
                    print("There is one {}".format(move))
                else:
                    print("There are {} {}'s".format(count, move))


                player.addMoney(count * wheelPrize['value'])
                if wheelPrize['prize']:
                    player.addPrize(wheelPrize['prize'])


                if obscurePhrase(phrase, guessed) == phrase:
                    winner = player
                    break

                continue
             elif count == 0:
                            print("There is no {}".format(move))
             else:
            if move == phrase:
                winner = player


                player.addMoney(wheelPrize['value'])
                if wheelPrize['prize']:
                    player.addPrize(wheelPrize['prize'])

                    break

                 else:
                                print('{} was not the phrase'.format(move))

                playerIndex = (playerIndex + 1) % len(players)

if winner:

    print('{} wins! The phrase was {}'.format(winner.name, phrase))
    print('{} won ${}'.format(winner.name, winner.prizeMoney))
    if len(winner.prizes) > 0:
        print('{} also won:'.format(winner.name))
        for prize in winner.prizes:
            print('    - {}'.format(prize))
else:
    print('Nobody won. The phrase was {}'.format(phrase))