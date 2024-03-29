# Rock-paper-scissors-lizard-Spock 
# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors
# and calculate the winner of the game
import random


# helper functions
def number_to_name(number):    
    # converts number to a name using if/elif/else    
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'

    
def name_to_number(name):    
    # converts name to number using if/elif/else    
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4


def rpsls(name):
    # converts name to player_number using name_to_number
    player_number = name_to_number(name)
    
    # computes random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)        
    
    # computes difference of player_number and comp_number and uses mod five
    # if diff 1 or 2 player wins
    # if diff 3 or 4 computer wins
    # if diff 0 no one wins
    diff = (player_number - comp_number) % 5
        
    
    # using if/elif/else to determine winner    
    if diff == 1 or diff == 2:
        winner = 'Player'
    if diff == 3 or diff == 4:
        winner = 'Computer'
    
    
    # prints results
    print "Player choose: ", number_to_name(player_number)
    print "Computer choose: ", number_to_name(comp_number) 
    if diff:   
        print winner, "wins!\n"
    else:
        print "We have a tie!\n"
 

# test
if __name__=='__main__': 
    rpsls("rock")
    rpsls("Spock")
    rpsls("paper")
    rpsls("lizard")
    rpsls("scissors")
