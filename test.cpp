#include "Chord-Detector-and-Chromagram/src/Chromagram.h"
#include "Chord-Detector-and-Chromagram/src/ChordDetector.h"
#include <iostream>
#include <fstream>
#include <vector>

int main() {
    // Assuming the audio file is in a raw PCM format and has been converted to double samples
    std::ifstream file("audio.pcm", std::ios::binary);
    if (!file.is_open()) {
        std::cerr << "Error opening audio file." << std::endl;
        return 1;
    }

    // Reading file into a buffer
    std::vector<short> buffer((std::istreambuf_iterator<char>(file)),
                               std::istreambuf_iterator<char>());

    // The Chromagram class expects an array of double samples
    std::vector<double> audio(buffer.size());
    for (size_t i = 0; i < buffer.size(); ++i) {
        audio[i] = buffer[i];
    }

    // Initialize Chromagram and ChordDetector
    Chromagram chromagram(100, 44100);
    ChordDetector chordDetector;

    // Processing the buffer in chunks
    for (size_t i = 0; i < audio.size(); i += 100) {
        // Ensure not to overflow the buffer
        if (i + 100 > audio.size()) break;

        // Process the audio frame
        chromagram.processAudioFrame(&audio[i]);

        // Check if the Chromagram is ready and detect the chord
        if (chromagram.isReady()) {
            std::vector<double> chroma = chromagram.getChromagram();
            chordDetector.detectChord(chroma);

            // Output the detected chord
            std::cout << "Detected Chord: Root note = " << chordDetector.rootNote 
                      << ", Quality = " << chordDetector.quality << std::endl;
        }
    }

    return 0;
}
