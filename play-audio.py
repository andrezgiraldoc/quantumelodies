from mingus.midi import fluidsynth
import mingus.core.notes as notes
from mingus.containers import Note, Bar
import time

notes.is_valid_note("C")
fluidsynth.init("FreePatsGM-20210329.sf2")
n = Note("C-3")
# n.channel = 5
# n.velocity = 70
# fluidsynth.play_Note(n)
# time.sleep(1)

notes = ["C-4", "D-4", "E-4", "F-4", "G-4", "A-4", "B-4", "C-5"]
for note in notes:
    fluidsynth.play_Note(Note(note))
    time.sleep(1)
