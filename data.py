# File --data.py--
from os import listdir
from os.path import isfile, join
import numpy as np
import pandas as pd
from slippi import Game
import analysis


def GetPorts(game):
    return [x for x in range(0, 4) if game.frames[1].ports[x] != None]


def GetNametag(game):
    return [x.tag for x in game.start.players if x != None]
    

def main(path):
    files = [f for f in listdir(path) if isfile(join(path, f))]
    #print(files)
    df_data = pd.DataFrame()
    for f in files:
        print(f)
        game = Game(str(path) + '/' + str(f))
        print(GetNametag(game))
        try:
            port = GetPorts(game)[GetNametag(game).index('ＪＯＥＹ')]
        except ValueError:
            port = GetPorts(game)[GetNametag(game).index('８')]
        port2 = GetPorts(game)[1 - port]
        data = analysis.Data(game, port, port2)
        df = data.ProcessData()
        df = df.loc[df['state'].shift(-1) != df['state']]
        df = df.loc[df['state'].isin([199, 200, 201])]
        df_data = df_data.append(df)

    df_data.to_csv('test.csv')
    df_data.to_csv('test.txt', header=None, index=None)


if __name__ == '__main__':
    main('dataset')