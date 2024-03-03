import simpleaudio as sa
from gpiozero import LED,PWMLED,Button
from signal import pause
import time
import random
from textToSpeech import text_to_wav
from textGeneration import generate_sentences

led_pin ="8" 
button_pin ="10" 
led = PWMLED("BOARD"+led_pin,initial_value=0)
WORK_DIR = '/home/shuojin/Documents/love/'
# voice = "cmn-CN-Wavenet-B"
voice = "en-GB-Neural2-A"
file_extension = '.wav'
wav_file_path = WORK_DIR+voice
NUM_AUDIO_FILES = 100
audioID = 0


def play_wav_file(file_path):
    # Load the audio file
    wave_obj = sa.WaveObject.from_wave_file(file_path)
    # Play the audio file
    play_obj = wave_obj.play()
    # Wait for the playback to finish
    play_obj.wait_done()

def loadAudioFiles():
    led.pulse()
    # user_prompt = "生成一段简短的土味情话,不超过50个字"
    # user_prompt = "I'm 15 year old. Tell me a great joke."
    user_prompt = f"tell me {NUM_AUDIO_FILES} jokes, each in a line"
    sentences = generate_sentences(user_prompt)
    print("sentences")
    for i in range(len(sentences)):
        print(sentences[i])
        text_to_wav(voice, sentences[i],wav_file_path+str(i)+file_extension)
    led.blink()

def randomNum():
    timestamp = int(time.time())
    random.seed(timestamp)
    random_number = random.randint(0, NUM_AUDIO_FILES-1)
    return random_number

def playAudio():
    global audioID
    led.pulse()
    play_wav_file(wav_file_path+str(audioID)+file_extension)
    print(audioID)
    audioID += 1
    audioID %= NUM_AUDIO_FILES
    led.blink()

audioID = randomNum()
button = Button("BOARD"+button_pin,hold_repeat=True)
button.when_pressed = playAudio
# button.when_held = loadAudioFiles
led.blink()
pause()
