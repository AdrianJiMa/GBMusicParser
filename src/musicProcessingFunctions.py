# -*- coding: utf-8 -*-
"""
This scrip defines several useful processing functions.
"""
    
def get_branch_name(line):
    #print(line)
    return line

def get_tempo(line):
    txt = line.split(" ")
    return txt[-1]

def get_volume(line):
    txt = line.split(" ")
    txt = txt[-2].split(",")
    return txt[0]

def get_noteLength(line):
    txt = line.split(" ")
    txt = txt[-3].split(",")
    return txt[0]

def get_note(line):
    txt = line.split("\t")
    txt = txt[1].split(" ")
    return txt[-2]

def get_noteDuration(line):
    txt = line.split(" ")
    txt = txt[1].split("\n")
    return txt[0]

def get_octave(line):
    txt = line.split(" ")
    txt = txt[1].split("\n")
    return txt[0]

# noteFull is a list of 3 elements: octave, note and duration
def get_noteFull(octave,line):
    noteFull = []
    noteFull.append(octave)
    noteFull.append(get_note(line))
    noteFull.append(get_noteDuration(line))
    return noteFull

def get_loopchannelBranch(line):
    txt = line.split(", ")
    return txt[-1]

# Function that computes the height of the note given the name and octave
def get_ypos(noteFull):
    octave = int(noteFull[0])
    note = noteFull[1][0]
    
    ypos = -120 + 35 * (octave-2) # C note y_pos for every octave
    
    if note == "C":
        ypos = ypos
    elif note == "D":
        ypos = ypos + 5
    elif note == "E":
        ypos = ypos + 10
    elif note == "F":
        ypos = ypos + 15
    elif note == "G":
        ypos = ypos + 20
    elif note == "A":
        ypos = ypos + 25
    elif note == "B":
        ypos = ypos + 30

    return ypos