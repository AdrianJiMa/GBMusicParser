# -*- coding: utf-8 -*-
"""
Function that writes a string line onto a file defined by its ID.
"""

def write_output_lines(dstfile,line):
    dstfile.write(str(line))
    # Writing to a file