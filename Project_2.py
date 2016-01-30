# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# initialize global variables used in your code here
num_range = 100
secret_number = 0
noOfguesses = 0

# helper function to start and restart the game
def new_game():
    
    # remove this when you add your code    
    # pass
    print
    print "New Game.", "Range is from 0 to", num_range
    
    global secret_number
    secret_number = random.randrange(0, num_range)
    # print secret_number
    
    global noOfGuesses
    #finding max noOfGuesses using math.ceil and math.log functions
    noOfGuesses = int(math.ceil(math.log(num_range, 2)))
    #if num_range == 100:
    #    noOfGuesses = 7
    #else:
    #    noOfGuesses = 10
    print "Number of remaining guesses is", noOfGuesses


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    
    # remove this when you add your code    
    # pass
    
    global num_range
    num_range = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    
    # pass

    global num_range
    num_range = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    
    # remove this when you add your code
    # pass
    
    # printing a blank line
    print
    
    guessedNo = int(guess)
    print "Guess was", guessedNo
    
    global noOfGuesses
    noOfGuesses -= 1
    print "Number of remaining guesses is", noOfGuesses
    
    if secret_number == guessedNo:
        print "Correct!"
        new_game()
    elif noOfGuesses == 0:
        print "You ran out of guesses.", "The number was", secret_number
        new_game()
    elif guessedNo > secret_number:
        print "Lower!"
    else:
        print "Higher!"        

# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Guess", input_guess, 200)

# call new_game 
new_game()
frame.start()


# always remember to check your completed program against the grading rubric
