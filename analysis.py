# File --analysis.py--

import numpy as np
import pandas as pd


## CHARACTER ##

#def characters(game, port):
#    characters = [x.character for x in game.start.players if x != None]
#    return(characters[port])

## STAGE ##

def stage(game):
    stage = game.start.stage
    return(stage)

## DATA FRAME ##
class df():
    def data(game, port, port2):
        state = np.array([x.ports[port].leader.post.state 
            for x in game.frames if x.ports[port] != None])
        position = np.array([x.ports[port].leader.post.position 
            for x in game.frames if x.ports[port] != None])
        position_op = np.array([x.ports[port2].leader.post.position 
            for x in game.frames if x.ports[port2] != None])
        last_attack_landed_op = np.array(
            [x.ports[port2].leader.post.last_attack_landed
            for x in game.frames if x.ports[port2] != None])
        df = pd.DataFrame({'state':state, 'position':position,
            'position_op':position_op,
            'last_attack_landed_op':last_attack_landed_op})
        return(df)

