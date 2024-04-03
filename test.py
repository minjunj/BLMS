import autochord
autochord.recognize('source/wilight.wav', lab_fn='chords.lab')
# This gives out a list of tuples in the format:
#  (chord start, chord end, chord name)
# e.g.
# [(0.0, 5.944308390022676, 'D:maj'),
#  (5.944308390022676, 7.476825396825397, 'C:maj'),
#  (7.476825396825397, 18.250884353741498, 'D:maj'),
#  (18.250884353741498, 19.736961451247165, 'C:maj')
#  ...
#  (160.49632653061224, 162.30748299319728, 'N')]