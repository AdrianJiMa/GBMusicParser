# -*- coding: utf-8 -*-
"""
Function that prints a note into *.musicxml format.
"""

# Load defined functions
from writeLines import write_output_lines
from musicCheckingFunctions import check_sharpNote

def printNote(fileID,noteFull,x,y,tiedNotes):
    if "rest" in noteFull[1]:
        write_output_lines(fileID,'      <note>\n')
        write_output_lines(fileID,"        <rest/>\n")
    else:
        # If the note is not silence, fill info about note and octave
        write_output_lines(fileID,'      <note default-x="%s" default-y="%6.2f">\n'%(x,y))
        write_output_lines(fileID,'        <pitch>\n')
        write_output_lines(fileID,"          <step>%s</step>\n"%noteFull[1][0])
        if check_sharpNote(noteFull):
            write_output_lines(fileID,"          <alter>1</alter>\n")
        write_output_lines(fileID,"          <octave>%s</octave>\n"%noteFull[0])
        write_output_lines(fileID,"          </pitch>\n")
    
    # For both types, include the tag of how long it's played.
    write_output_lines(fileID,"        <duration>%s</duration>\n"%noteFull[2])
    
    # ligaduras de prolongación / Tie
    # If 0, no tie is necessary, so do nothing
    if tiedNotes == 1:
        write_output_lines(fileID,'        <tie type="start"/>\n')
    elif tiedNotes == -1:
        write_output_lines(fileID,'        <tie type="stop"/>\n')
    
    # Only 1 voice is available per channel
    write_output_lines(fileID,"        <voice>1</voice>\n")
    
    # Duration of note by name
    if noteFull[2] == "1":
        write_output_lines(fileID,"        <type>16th</type>\n")
    elif noteFull[2] == "2":
        write_output_lines(fileID,"        <type>eighth</type>\n")
    elif noteFull[2] == "3":
        write_output_lines(fileID,"        <type>eighth</type>\n")
        write_output_lines(fileID,"        <dot/>\n")
    elif noteFull[2] == "4":
        write_output_lines(fileID,"        <type>quarter</type>\n")
    elif noteFull[2] == "6":
        write_output_lines(fileID,"        <type>quarter</type>\n")
        write_output_lines(fileID,"        <dot/>\n")
    elif noteFull[2] == "7":
        write_output_lines(fileID,"        <type>quarter</type>\n")
        write_output_lines(fileID,"        <dot/>\n")
        write_output_lines(fileID,"        <dot/>\n")
    elif noteFull[2] == "8":
        write_output_lines(fileID,"        <type>half</type>\n")
    elif noteFull[2] == "12":
        write_output_lines(fileID,"        <type>half</type>\n")
        write_output_lines(fileID,"        <dot/>\n")
    elif noteFull[2] == "14":
        write_output_lines(fileID,"        <type>half</type>\n")
        write_output_lines(fileID,"        <dot/>\n")
        write_output_lines(fileID,"        <dot/>\n")
    elif noteFull[2] == "16":
        write_output_lines(fileID,"        <type>whole</type>\n")
    else:
        write_output_lines(fileID,"Notelength %s not recognized\n" %noteFull[2])
        return 1
    
    if "rest" in noteFull[1]:
        # Silence
        0 # do nothing
    else:
        # If octave is 5 or higher, plica/stem is going down
        if noteFull[0] == "5" or noteFull[0] == "6" or noteFull[0] == "7":
            write_output_lines(fileID,"        <stem>down</stem>\n")
        else:
            write_output_lines(fileID,"        <stem>up</stem>\n")
    
    # Code not necessary for correct behaviour, sharp is managed by "<alter>"
    # Logic for natural note after a sharp one, might be hard to do
    # "<accidental>natural</accidental>" -> becuadro (natural) note
    #if check_sharpNote(noteFull):
    #    write_output_lines(fileID,"        <accidental>sharp</accidental>\n")
        
    # ligaduras de prolongación / Tie
    if tiedNotes == 1:
        write_output_lines(fileID,'        <notations>\n')
        write_output_lines(fileID,'          <tied type="start"/>\n')
        write_output_lines(fileID,'          </notations>\n')
    elif tiedNotes == -1:
        write_output_lines(fileID,'        <notations>\n')
        write_output_lines(fileID,'          <tied type="stop"/>\n')
        write_output_lines(fileID,'          </notations>\n')
    
    # Close note tag
    write_output_lines(fileID,"        </note>\n")
    return 0