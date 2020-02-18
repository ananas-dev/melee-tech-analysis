# File --main.py--

from slippi import Game
import analysis
import algorithms


## MAIN ##

def test():
    # Title
    print('\n -- SLIPPI ANALYSIS TEST --')
    # Sets the path of the .slp file
    game1 = Game('games/test.slp')
    game = Game('games/test2.slp')
    # stage
    stage = analysis.stage(game)
    print()
    print(stage)
    # Sets the port
    port = 2
    port2 =0 #between 0 and 3
    # Checks the character
    #characters = analysis.characters(game, port)
    #print("\ncharacter:", characters)
    #TEST
    df = analysis.data(game, port, port2)
    df = df.loc[df['state'].shift(-1) != df['state']]
    df = df.loc[df['state'].isin([199, 200, 201])]
    df.to_csv('test.csv')

def main():
    game = Game('games/test2.slp')
    port = 2
    port2 =0 #between 0 and 3
    df = analysis.df.data(game, port, port2)
    df = df.loc[df['state'].shift(-1) != df['state']]
    df = df.loc[df['state'].isin([199, 200, 201])]
    df.to_csv('test.csv')


if __name__ == '__main__':
    main()
