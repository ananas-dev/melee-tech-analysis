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
    # Checks the character
    characters = analysis.characters(game)
    print("\ncharacter:", characters[2])
    # Init variables
    landed_lasers = 0
    # Gets landed attacks
    attacks = analysis.attacks(game)
    # Checks the number of neutralB 
    for x in attacks[2]:
        if x == 18:
            landed_lasers = landed_lasers+1
    print('\nlanded lasers:', landed_lasers, '\n')
    # Tests
    #data = analysis.data(game)
    #print(data[0])

if __name__ == '__main__':
    main()
