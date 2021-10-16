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
