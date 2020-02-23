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
    df_final = pd.DataFrame()
    count = 0
    for f in files:
        count = count + 1
        print(count,'/',len(files))
        game = Game(str(path) + '/' + str(f))
        #print(game.start.players)
        #print(GetNametag(game))
        try:
            port = GetPorts(game)[GetNametag(game).index('ＷＩＺＹ')]
        except ValueError:
            print("Error: the player insn't in this file:",f)
            exit()
        port2 = GetPorts(game)[1 - port]
        data = analysis.Data(game, port, port2)
        df = data.ProcessData()
        df = df.loc[df['state'].shift(-1) != df['state']]
        df = df.loc[df['state'].isin([199, 200, 201])]
        df_final = df_final.append(df)
    df_final = df_final.sort_values(by=['state'])
    df_final = df_final.reset_index(drop=True)
    df_final.to_csv('data.csv')
    df_final.to_csv('data.txt', header=None, index=None)
    df_final_names = list(df.columns.values)
    with open('data_names.txt', 'w') as f:
        f.write(",".join(df_final_names))

if __name__ == '__main__':
    main('database')


