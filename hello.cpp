// #include <iostream>
// #include "Chord-Detector-and-Chromagram/src/ChordDetector.h"

#include "Chord-Detector-and-Chromagram/src/Chromagram.h"
#include "Chord-Detector-and-Chromagram/src/ChordDetector.h"
#include <iostream>
#include <vector>

int main() {
    // Initialize Chromagram and ChordDetector
    int sampleRate = 44100; // Standard sample rate
    int frameSize = 4096; // Size of the audio frame to analyze
    Chromagram chromagram(frameSize, sampleRate);
    ChordDetector chordDetector;

    // Example audio buffer; in a real application, this should be filled with actual audio data
    std::vector<float> audioBuffer(frameSize, 0); // Initialize with zeroes for the sake of example

    // Process the audio buffer to update the chromagram
    chromagram.processAudioFrame(&audioBuffer[0]);
    
    // If enough samples have been processed, detect the chord
    if (chromagram.isReady()) {
        chromagram.calculateChromagram();
        std::vector<double> chroma = chromagram.getChromagram();
        
        // Detect the chord
        chordDetector.detectChord(chroma);
        
        // Output the detected chord
        std::cout << "Detected Chord: " << chordDetector.rootNote << " " << chordDetector.quality << std::endl;
    } else {
        std::cout << "Not enough data to detect chord." << std::endl;
    }

    return 0;
}
