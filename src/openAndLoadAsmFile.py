# -*- coding: utf-8 -*-
"""
This script reads the raw asm file and saves it into a variable.
"""

# Function to close an opened file
def close_file(dstfile):
    dstfile.close()

import tkinter as tk
from tkinter import filedialog

def open_asmFile():
    # Open dialog to choose the input asm file.
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()


    # Read file content and return it.
    srcfile = open(file_path, 'r')
    srcData = srcfile.readlines()
    close_file(srcfile)
    
    return [srcData, file_path]