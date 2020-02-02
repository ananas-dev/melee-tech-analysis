# File --main.py--

from slippi import *
import analysis

## MAIN ##

def main():
    # Title
    print('\n -- SLIPPI DATA ANALYSIS TEST --')
    # Sets the path of the .slp file
    path = 'games/test.slp'
    game = Game(path)
    print('\npath of the .slp file:', path)
    # Sets the port
    port = 2 #between 0 and 3
    # Checks the character
    characters = analysis.characters(game)
    print("\ncharacter:", characters[port])
    # Init variables
    landed_lasers = 0
    neutral_techs = 0
    forward_techs = 0
    backward_techs = 0
    # Gets landed attacks
    attacks = analysis.attacks(game)
    # Checks the number of neutralB 
    for x in attacks[port]:
        if x == 18:
            landed_lasers = landed_lasers+1
    print('\nlanded lasers:', landed_lasers,)
    # Tests
    data = analysis.data(game)
    for x in data[port]:
        if x == 199:
            neutral_techs = neutral_techs+1
        elif x == 200:
            forward_techs = forward_techs+1
        elif x == 201:
            backward_techs = backward_techs+1
    print("\nneutral techs:",neutral_techs)
    print("forward techs:",forward_techs)
    print("backward techs:",backward_techs, '\n')
    #print(data[0])

if __name__ == '__main__':
    main()
