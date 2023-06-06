# test-sounddevice.py

import sounddevice as sd
import soundfile as sf


# sd.default.device= 'MacBook Pro Speakers'

data, fs = sf.read('macbook-charger-on.wav')
sd.play(data, fs)

