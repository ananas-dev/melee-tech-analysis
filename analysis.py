# File --analysis.py--

import numpy as np
import pandas as pd


## CHARACTER ##

#def characters(game, port):
#    characters = [x.character for x in game.start.players if x != None]
#    return(characters[port])

## DATA FRAME ##
class Data:
    def __init__(self, game, port, port2):
        self.game = game
        self.port = port
        self.port2 = port2

    def Stage(self):
        stage = self.game.start.stage
        return(stage)

    def ProcessData(self):
        state = np.array([int(x.ports[self.port].leader.post.state)
            for x in self.game.frames])

        position_x = np.array([int(x.ports[self.port].leader.post.position.x)
            for x in self.game.frames])

        position_y = np.array([int(x.ports[self.port].leader.post.position.y)
            for x in self.game.frames])

        damage = np.array([int(x.ports[self.port].leader.post.damage)
            for x in self.game.frames])
        
        stocks = np.array([int(x.ports[self.port].leader.post.stocks)
            for x in self.game.frames])

        position_x_op = np.array([int(x.ports[self.port2].leader.post.position.x)
            for x in self.game.frames])

        position_y_op = np.array([int(x.ports[self.port2].leader.post.position.y)
            for x in self.game.frames])
        
        last_attack_landed_op = []
        for x in self.game.frames:
            if x.ports[self.port2].leader.post.last_attack_landed == None:
                 last_attack_landed_op.append(0)
            else:
                last_attack_landed_op.append((x.ports[self.port2].leader.post.last_attack_landed).value)
            

        df = pd.DataFrame({'state':state, 'position_x':position_x,
            'position_y':position_y, 'damage':damage, 'stocks':stocks,
            'position_x_op':position_x_op, 'position_y_op':position_y_op,
            'last_attack_landed_op':last_attack_landed_op})
        return(df)
