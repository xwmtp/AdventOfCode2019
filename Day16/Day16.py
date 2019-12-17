# https://adventofcode.com/2019/day/16

import numpy as np
import math
import time

f = open("Input16.txt")
inputs = f.read()
f.close()

input_signal = [int(d) for d in str(inputs)]

test_signal = [1,2,3,4,5,6,7,8]



class FFT:

    def __init__(self):
        self.base_pattern = [0, 1, 0, -1]
        self.patterns = dict()

    def get_pattern(self, i, length):
        if i not in self.patterns.keys():
            pattern = list(np.repeat(self.base_pattern, i+1))
            if len(pattern) - 1 < length:
                pattern = pattern * math.ceil(length / (len(pattern) - 1))
            self.patterns[i] = pattern[1:]
        return self.patterns[i]
            

    def last_digit(self, i):
        return int(str(i)[-1])

    def run_fft(self, signal, phases):
        for i in range(phases):
            now = time.time()
            signal = self.fft_phase(signal)
            print(i+1, round(time.time() - now,4), signal)
        return signal

    def fft_phase(self, signal):
        phase_output = []
        length = len(signal)
        for i in range(length):
            pattern = self.get_pattern(i, length)
            new_num = sum([signal[i] * pattern[i] for i in range(length)])
            phase_output.append(self.last_digit(new_num))
        return phase_output


fft = FFT()
#fft.run_fft(input_signal, 100)



class FFT_offset:

    def __init__(self):
        self.base_pattern = [0, 1, 0, -1]
        self.patterns = dict()

    def run_fft(self, signal, phases):
        offset = self.list_to_int(signal[:7])
        print('offset:', offset)
        signal = signal[offset:]

        for i in range(phases):
            signal = self.fft_phase(signal)
            print(i+1, signal[:30])
        return signal

    def fft_phase(self, signal):
        new_signal = signal.copy()
        sum = 0
        for i in reversed(range(len(signal))):
            sum += signal[i]
            new_signal[i] = self.last_digit(sum)

        return new_signal

    def last_digit(self, i):
        return int(str(i)[-1])

    def list_to_int(self, lst):
        return int(''.join([str(s) for s in lst]))

print('h')
signal = input_signal * 10000
test_signal   = [int(i) for i in '03036732577212944063491565474664'] * 10000
test_signal_2 = [int(i) for i in '02935109699940807407585447034323'] * 10000
#signal=test_signal_2

offset = signal[:7]

fft_offset = FFT_offset()
print(len(signal))
final = fft_offset.run_fft(signal, 100)
print(len(final))
print(final[:30])
print(fft_offset.list_to_int(final[:8]))

# 4877678 too low