import numpy as np
import pygame as py
import scipy.io.wavfile as wav
from scipy.io.wavfile import write


def interpolate_linearly(wave_table, index) :
    truncated_index = int(np.floor((index)))
    next_index = (truncated_index + 1) % wave_table.shape[0]

    next_index_weight = index - truncated_index
    truncated_index_weight = 1 - next_index_weight

    return truncated_index_weight * wave_table [truncated_index] + next_index_weight * wave_table[next_index]

def sawtooth(x) :
    return(x + np.pi) / np.pi % 2 - 1

def fade_in_out(signal, fade_length=1000) :
    fade_in = (1- np.cos(np.linspace(0,np.pi,fade_length))) * 0.5
    fade_out = np.flip(fade_in)

    signal[:fade_length] = np.multiply(fade_in, signal[:fade_length])
    signal[-fade_length:] = np.multiply(fade_out, signal[-fade_length:])

    return signal
sample_rate = 44100
def a() :
    sample_rate = 44100
    f = 261.63 #c4 note
    t = 3
    waveform = sawtooth

    wavetable_length = 64
    wave_table = np.zeros((wavetable_length,))

    for n in range(wavetable_length) :
        wave_table[n] = waveform(2*np.pi * n /
        wavetable_length)

    output = np.zeros((t * sample_rate,))

    index = 0
    index_increment = f * wavetable_length /sample_rate

    for n in range(output.shape[0]) :
        #output[n] = wave_table[int(np.floor(index))]
        output[n] = interpolate_linearly(wave_table, index)
        index += index_increment
        index %= wavetable_length
    
    gain = -20
    amplitude = 10 ** (gain / 20)
    output *= amplitude
    
    wav.write('sawtooth.wav', sample_rate, output.astype(np.float32))

def get_wave(freq, duration=2):
    amplitude = 4096
    t = np.linspace(0, duration, int(sample_rate * duration))
    wave = amplitude * np.sin(2 * np.pi * freq * t)

    return wave

def get_piano_notes():
    octave = ['C', 'c', 'D', 'd', 'E', 'F', 'f', 'G', 'g', 'A', 'a', 'B']
    base_freq = 261.63

    note_freqs = {octave[i]:base_freq*pow(2, (i/12)) for i in range(len(octave))}
    note_freqs[''] = 0.0

    return note_freqs

def get_song_data(music_notes):
    note_freqs = get_piano_notes()
    song = [get_wave(note_freqs[note]) for note in music_notes.split('-')]
    song = np.concatenate(song)

    return song.astype(np.int16)


def get_chord_data(chords):
    chords = chords.split('-')
    note_freqs = get_piano_notes()

    chord_data = []
    for chord in chords:
        data = sum([get_wave(note_freqs[note]) for note in list(chord)])
        chord_data.append(data)

    chord_data = np.concatenate(chord_data, axis = 0)

    return chord_data.astype(np.int16)

if __name__ == '__main__':
    music_notes = 'C-C-G-G-A-A-G--F-F-E-E-D-D-C--G-G-F-F-E-E-D--G-G-F-F-E-E-D--C-C-G-G-A-A-G--F-F-E-E-D-D-C'
    data = get_song_data(music_notes)
    data = data * (16300/np.max(data))

    write('song.wav', sample_rate, data.astype(np.int16))

    chords = 'CdG-GBD-aDF-FgC'
    data = get_chord_data(chords)
    data = data * (16300/np.max(data))
    data = np.resize(data, (len(data)*5,))
    
    write('borderline3.wav', sample_rate, data.astype(np.int16))
