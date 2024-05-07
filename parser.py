def parse_lab_file(filename):
    chords = []
    with open(filename, 'r') as file:
        for line in file:
            start, end, chord = line.strip().split("\t")
            chords.append((float(start), float(end), chord))
    return chords

# Example usage
lab_file = 'source/dont_lazy.lab'
chords = parse_lab_file(lab_file)
for chord in chords:
    print(chord)
    print(chord[2])
