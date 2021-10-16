# -*- coding: utf-8 -*-
"""
Function that processes the asm file and parses it into *.musicxml format.
In this first phase, only notes are processed.
"""

from openAndLoadAsmFile import open_asmFile
from openAndLoadAsmFile import close_file
from writeLines import write_output_lines
from printNoteOntoFile import printNote
import musicProcessingFunctions as mp
import musicCheckingFunctions as mc
import genericMusicXMLFileInfo as mxml

[srcData, filepath] = open_asmFile()
songName = filepath.split("/")[-1].split(".")[0]

# Open output file
fileID = open('./OutputFile.musicxml', 'w')

# Parameter that saves the current octave
octave = 0

# Parameter that saves the current note duration
duration = 0

# Parameter that saves the current position inside a bar
# Each quarter equals a duration of 60, the bar limit in 4/4 is 240
current_x = 0

# Parameter that gets the current bar we are writing
measure_count = 1

# Couple of parameters to track the current channel we are parsing
first_channel = True
second_channel = True

# Print the header 
mxml.print_FileHeader(fileID, songName)

for line in srcData:
    # Because the tempo is declared after initializing the first channel, the 
    # flag is set to false before entering the check_tempo function, and
    # therefore, the logic seems a little weird with the first_channel parameter
    if mc.check_new_channel(line):
        if first_channel:
            first_channel = False
            # flag used to write the tempo
        elif second_channel:
            second_channel = False
            mxml.print_partIntro(fileID,"P2")
        else:
            mxml.print_partIntro(fileID,"P3")
        measure_count = 1
        
    # Tempo setting
    if mc.check_tempo(line):
        tempo = 18800/int(mp.get_tempo(line))
        if not first_channel:
            mxml.print_part1Intro(fileID,tempo)
        else:
            write_output_lines(fileID,"### Big Error with Tempo and Channel 0 ###")
            break
        
    elif mc.check_callchannel(line):
        write_output_lines(fileID,"### Error: subchannels are not compatible yet ###")
        break
    
    # Save current octave in use in a separate variable
    elif mc.check_octave(line):
        octave = mp.get_octave(line)
    
    # Add new note to the xml
    elif mc.check_note(line):
        # If a new bar is being started and it's not the first one (that has special fields)
        if current_x == 0 and measure_count != 1:
            write_output_lines(fileID,'    <measure number="%d" width="250.00">\n'%measure_count)
            
        # noteFull is a list of 3 elements: octave, note and duration
        noteFull = mp.get_noteFull(octave,line)
        duration = int(noteFull[2])
        
        # printNote can manage the following durations: 1, 2, 3, 4, 6, 7, 8, 12, 14, 16
        # Other durations need a tied double note to be processed
        # After each printNote, a check that no strange value has entered the data will be done.
        
        if duration in [5, 9, 13, 15]:
            # The note will be separated in 2 tied notes: 16th and the remainder.
            aux = noteFull.copy()
            aux[2] = "1"
            returnedValue = printNote(fileID,aux,current_x,mp.get_ypos(noteFull),1)
            current_x = current_x + 15 #temp end position loaded
            
            if returnedValue == 1:
                write_output_lines(fileID,"### Error: Notelength not recognized ###")
                break
            
            # 2nd part of the note: quarter, half, dotted half or double dotted half
            aux[2] = str(int(noteFull[2]) - 1)
            returnedValue = printNote(fileID,aux,current_x,mp.get_ypos(noteFull),-1)
            current_x = current_x + int(aux[2])*15 #end position loaded
            
            if returnedValue == 1:
                write_output_lines(fileID,"### Error: Notelength not recognized ###")
                break
            
        elif duration in [10, 11]: # cases not possible with a 16th plus a standard symbol
            # The note will be separated in 2 tied notes: half and other note.
            aux = noteFull.copy()
            aux[2] = "8"
            returnedValue = printNote(fileID,aux,current_x,mp.get_ypos(noteFull),1)
            current_x = current_x + 120 #temp end position loaded
            
            if returnedValue == 1:
                write_output_lines(fileID,"### Error: Notelength not recognized ###")
                break
            
            # 2nd part of the note: either 8th or dotted 8th
            aux[2] = str(int(noteFull[2]) - 8)
            returnedValue = printNote(fileID,aux,current_x,mp.get_ypos(noteFull),-1)
            current_x = current_x + int(aux[2])*15 #end position loaded
            
            if returnedValue == 1:
                write_output_lines(fileID,"### Error: Notelength not recognized ###")
                break
            
        else:
            # A single symbol is enough to represent this note.
            returnedValue = printNote(fileID,noteFull,current_x,mp.get_ypos(noteFull),0)
            current_x = current_x + int(noteFull[2])*15 #end position loaded
            
            if returnedValue == 1:
                write_output_lines(fileID,"### Error: Notelength not recognized ###")
                break
        
        # In the default beat of 4/4, a bar is finished when the position marker
        # reaches 240. If so, close the bar and prepare the start of the following one
        if current_x == 240:
            write_output_lines(fileID,'      </measure>\n')
            measure_count = measure_count + 1
            current_x = 0
#        elif current_x > 240:
#            write_output_lines(fileID,"### Error: Bar not finished correctly due to a unmanaged cause. ###")
 #           break

# Print the xml closure 
mxml.print_endxml(fileID)

# Close the file
close_file(fileID)