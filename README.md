# GBMusicParser
Nintendo Game Boy music assembly files parser into musicxml format

This python code will get an file.asm from the disassembly of a Game Boy game
and convert it into the ost music sheet that can be shown at free software tools
like musescore.

The program is first focused at pokemon games. Slight variations appear in these
types of files, but those variations could be solved with small fixes.

The project has several phases
Phase 1: just get the music sheet from the 3 channels the hardware uses.

Phase 2: further improvements with tempo, dynamics, etc.

Phase 3: higher level abstraction: use of codas, repeat signs, key signature selection...


How to use:
1) Run main.py using Python.
2) A dialog will be opened to allow you to select the assembly file with the music data.
3) A .musicxml file will be created in the directory where the script was executed.
4) Try to open it with the music software. Sometimes musescore detects some issues but can be still forced to load it.

Not all parsing functionality is prepared yet; in those cases a final error is added in the output file.
