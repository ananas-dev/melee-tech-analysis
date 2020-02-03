# File --analysis.py--

import pandas as pd
from itertools import groupby

## CHARACTER ##

def characters(game):
    characters = []
    for players in game.start.players:
        if players == None:
            character = None
        else:
            character = players.character
        characters.append(character)
    return(characters)

## STAGE ##

def stage(game):
    stage = game.start.stage
    return(stage)

## DATA FRAME ##

def data(game, player):
    p1_state=[]
    p1_position=[]
    p2_state=[]
    p2_position=[]
    p3_state=[]
    p3_position=[]
    p4_state=[]
    p4_position=[]
    for frames in game.frames:
        if frames.ports[0] != None:
            p1_frames = frames.ports[0].leader 
            p1_state.append(p1_frames.post.state)
            p1_position.append(p1_frames.post.position)
        if frames.ports[1] != None:
            p2_frames = frames.ports[1].leader
            p2_state.append(p2_frames.post.state)
            p2_position.append(p1_frames.post.position)
        if frames.ports[2] != None:
            p3_frames = frames.ports[2].leader
            p3_state.append(p3_frames.post.state)
            p3_position.append(p1_frames.post.position)
        if frames.ports[3] != None:
            p4_frames = frames.ports[3].leader
            p4_state.append(p4_frames.post.state)
            p4_position.append(p1_frames.post.position)
    state = [p1_state, p2_state, p3_state, p4_state]
    position = [p1_position, p2_position, p3_position, p4_position]
    index = {'state':state[player], 'position':position[player]}
    df = pd.DataFrame(index)
    return(df)
