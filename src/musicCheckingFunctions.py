# -*- coding: utf-8 -*-
"""
This scrip defines several useful checking functions.
"""

def check_notetype(line):
    if "notetype" in line:
        return True
    else:
        return False

def check_tempo(line):
    if "tempo" in line:
        return True
    else:
        return False
    
def check_volume(line):
    if "volume" in line:
        return True
    else:
        return False
    
def check_duty(line):
    if "duty" in line:
        return True
    else:
        return False

def check_new_channel(line):
    if "_Ch" in line:
        return True
    else:
        return False
    
def check_new_branch(line):
    if "_branch_" in line:
        return True
    else:
        return False
    
def check_loopchannel(line):
    if "loopchannel" in line:
        return True
    else:
        return False

def check_octave(line):
    if "octave " in line:
        return True
    else:
        return False

def check_note(line):
    if ( "A_ " in line or "A# " in line 
        or "B_ " in line 
        or "C_ " in line or "C# " in line 
        or "D_ " in line or "D# " in line 
        or "E_ " in line 
        or "F_ " in line or "F# " in line 
        or "G_ " in line or "G# " in line 
        or "rest " in line):
        return True
    else:
        return False
    
def check_sharpNote(noteFull):
    if "#" in noteFull[1]:
        return True
    else:
        return False
    
def check_callchannel(line):
    if "callchannel " in line:
        return True
    else:
        return False  
