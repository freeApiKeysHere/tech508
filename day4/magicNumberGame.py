import random
# User story 1
# As a user, I want to be able to guess a number and know if i got it correct or not, so that I can know if I won or not.
# Define/assign number to a variable called magic_number
# Ask user for input
# Check if this input matches magic_number
# Let the user know if the response was correct or not
# Allow the user 5 guesses

# User story 2
# As a user, I want to be able to guess a number and know if I need to go higher or lower.

# User story 3
# As a user, I don't want my guesses wasted if I enter something accidently as my guess which are not digits.

# User story 4
# As a user, after each guess, I would like to know how many guesses I have left.

# User story 5
# As a user, I would like the magic to be randomly generated each time I play so it is more fun.

# User story 6
# As a user, I would like to know the magic number at the end of the game if I still haven't guessed correctly and I've used up all my tries.
def magicNumGame(magic_number: int, counter: int, proximity: bool = False, wasted: bool = False, viewTries: bool = False, rndm: bool = False, showMagic: bool = False):
    if rndm:
        magic_number = random.randint(0, 999)
    while True:
        if wasted:
            try:
                x = int(input("The magic number is a whole number. Enter a your guess: "))
            except ValueError:
                print("Enter a valid number, this guess will not be counted")
                continue
        else:
            x = input("The magic number is a whole number. Enter a your guess: ")
        if x != magic_number:
            counter -= 1
            print("You guessed WRONG")
            if proximity:
                if x < magic_number:
                    print("Aim higher")
                else:
                    print("Aim lower")
            if viewTries:
                print(f"{counter} tries left...")
        else:
            print("WINNER!")
            break
        if counter <= 0:
            print("LOSER!")
            if showMagic == True:
                print(f"The magic number was: {magic_number}")
            break

# magicNumGame params:
# magic_number - int
#   required, defines the magic number to be guessed
#
# counter - int
#   required, defines the number of tries a user has
#
# proximity - bool
#   optional, default False, setting to True will prompt the user to guess higher or lower
#
# wasted - bool
#   optional, default False, setting to True will prevent 'invalid' guesses from decrementing the tries counter
#
# viewTries - bool
#   optional, default False, setting to True will show the user how many guesses they have remaining
#
# rndm - bool
#   optional, default False, setting to True will generate a random number between 0 and 999 as the magic_number
#
# showMagic - bool
#   optional, default False, setting to True will reveal magic_number after the user has used up their guesses

magicNumGame(180, 5, wasted=True)

