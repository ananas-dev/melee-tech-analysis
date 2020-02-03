# File --main.py--

from slippi import *
import analysis
import algorithms

## MAIN ##

def main():
    # Title
    print('\n -- SLIPPI ANALYSIS TEST --')
    # Sets the path of the .slp file
    path = 'games/test.slp'
    game = Game(path)
    print('\npath of the .slp file:', path)
    # Sets the port
    port = 2 #between 0 and 3
    # Checks the character
    characters = analysis.characters(game)
    print("\ncharacter:", characters[port])
    #TEST
    df = analysis.data(game, 2)
    df = df.loc[df['state'].shift(-1) != df['state']]
    df = df.loc[df['state'] == 199]
    print(df)
    df.to_csv('test.csv')

if __name__ == '__main__':
    main()
