# import pygame
import simpleaudio as sa
def play_wav_file(file_path):
    # Load the audio file
    wave_obj = sa.WaveObject.from_wave_file(file_path)

    # Play the audio file
    play_obj = wave_obj.play()

    # Wait for the playback to finish
    play_obj.wait_done()
# Specify the path to your WAV file
wav_file_path = 'cmn-CN-Wavenet-B.wav'

# Play the WAV file
play_wav_file(wav_file_path)
# pygame.init()
# my_sound=pygame.mixer.Sound('cmn-CN-Wavenet-B.wav')
# my_sound.play()

