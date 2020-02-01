# File --analysis.py--

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

## GENERAL DATA ##

def data(game):
    p1_data=[]
    p2_data=[]
    p3_data=[]
    p4_data=[]
    for frames in game.frames:
        if frames.ports[0] != None:
            p1_frames = frames.ports[0].leader 
            p1_data.append(p1_frames.post.state)
        if frames.ports[1] != None:
            p2_frames = frames.ports[1].leader
            p2_data.append(p2_frames.post.state)
        if frames.ports[2] != None:
            p3_frames = frames.ports[2].leader
            p3_data.append(p3_frames.post.state)
        if frames.ports[3] != None:
            p4_frames = frames.ports[3].leader
            p4_data.append(p4_frames.post.state)
    data_long = [p1_data, p2_data, p3_data, p4_data]
    data = []
    for x in data_long:
        rm_consecutives = [i[0] for i in groupby(x)]
        data.append(rm_consecutives)
    return(data)

## ATTACKS ##

def attacks(game):
    p1_attacks=[]
    p2_attacks=[]
    p3_attacks=[]
    p4_attacks=[]
    for frames in game.frames:
        if frames.ports[0] != None:
            p1_frames = frames.ports[0].leader 
            p1_attacks.append(p1_frames.post.last_attack_landed)
        if frames.ports[1] != None:
            p2_frames = frames.ports[1].leader
            p2_attacks.append(p2_frames.post.last_attack_landed)
        if frames.ports[2] != None:
            p3_frames = frames.ports[2].leader
            p3_attacks.append(p3_frames.post.last_attack_landed)
        if frames.ports[3] != None:
            p4_frames = frames.ports[3].leader
            p4_attacks.append(p4_frames.post.last_attack_landed)
    attacks_long = [p1_attacks, p2_attacks, p3_attacks, p4_attacks]
    attacks = []
    for x in attacks_long:
        rm_consecutives = [i[0] for i in groupby(x)]
        attacks.append(rm_consecutives)
    return(attacks)

