#import libraries
import time
import board
import digitalio

#set up
#check which audio file handler the board is equipped with
try:
    from audiocore import WaveFile
except ImportError:
    from audioio import WaveFile

#check if the audio out is digital-to-analog, true analog voltage out,  or Pulse-Width-Modulated, pseudo-analog binary voltage out.
try:
    from audioio import AudioOut
except ImportError:
    try:
        from audiopwmio import PWMAudioOut as AudioOut
    except ImportError:
        print("NO audio out possible")
        pass  # not always supported by every board!

# CPX requires:
speaker_enable = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
speaker_enable.switch_to_output(value=True)

#more setup: open the file, load it into memory
wave_file = open("yikes.wav", "rb")
wave = WaveFile(wave_file)
audio = AudioOut(board.A0)

#loop
#a loop is too annoying to use with an audio file.
audio.play(wave) # start playing, non-blocking
# wait till finished
while audio.playing:
        pass
