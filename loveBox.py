import simpleaudio as sa
from gpiozero import LED,PWMLED,Button
from signal import pause
import time
from textToSpeech import text_to_wav
from textGeneration import generate_love_sentence

led_pin ="8" 
button_pin ="10" 
led = PWMLED("BOARD"+led_pin,initial_value=0)
WORK_DIR = '/home/shuojin/Documents/love/'


def play_wav_file(file_path):
    # Load the audio file
    wave_obj = sa.WaveObject.from_wave_file(file_path)

    # Play the audio file
    play_obj = wave_obj.play()

    # Wait for the playback to finish
    play_obj.wait_done()

def doEverything():
    led.pulse()
    # user_prompt = "生成一段简短的土味情话,不超过50个字"
    # user_prompt = "I'm 15 year old. Tell me a great joke."
    user_prompt = "Say something encouraging! A little different everytime"
    # voice = "cmn-CN-Wavenet-B"
    voice = "en-GB-Neural2-A"
    print("thinking....")
    love_sentence = generate_love_sentence(user_prompt)
    print(love_sentence)
    wav_file_path = WORK_DIR+voice+'.wav'
    text_to_wav(voice, love_sentence,wav_file_path)
    play_wav_file(wav_file_path)
    led.off()

led.blink()
button = Button("BOARD"+button_pin,hold_repeat=True)
button.when_pressed = doEverything
pause()
