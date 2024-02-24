import openai
import simpleaudio as sa
from gpiozero import LED,PWMLED,Button
from signal import pause
import time
import google.cloud.texttospeech as tts
import config
openai.api_key=config.OPEN_AI_KEY
API_KEY=config.GOOGLE_CLOUD_KEY
led_pin ="8" 
ready_led_pin ="3" 
button_pin ="10" 
led = PWMLED("BOARD"+led_pin,initial_value=0)
led_ready = PWMLED("BOARD"+ready_led_pin,initial_value=.1)
def generate_love_sentence(prmpt):
    # Use OpenAI's GPT-3 to generate a love sentence
    # response = openai.ChatCompletion.create(
    completion = openai.completions.create(
      model="gpt-3.5-turbo-instruct",
      prompt=prmpt,
      max_tokens=1000,
      temperature=1
    )
    return completion.choices[0].text.strip()

def list_languages():
    client = tts.TextToSpeechClient(client_options={"api_key":API_KEY})
    response = client.list_voices()
    languages = unique_languages_from_voices(response.voices)

    print(f" Languages: {len(languages)} ".center(60, "-"))
    for i, language in enumerate(sorted(languages)):
        print(f"{language:>10}", end="\n" if i % 5 == 4 else "")

def list_voices(language_code=None):
    client = tts.TextToSpeechClient(client_options={"api_key":API_KEY})
    response = client.list_voices(language_code=language_code)
    voices = sorted(response.voices, key=lambda voice: voice.name)

    print(f" Voices: {len(voices)} ".center(60, "-"))
    for voice in voices:
        languages = ", ".join(voice.language_codes)
        name = voice.name
        gender = tts.SsmlVoiceGender(voice.ssml_gender).name
        rate = voice.natural_sample_rate_hertz
        print(f"{languages:<8} | {name:<24} | {gender:<8} | {rate:,} Hz")
def text_to_wav(voice_name: str, text: str):
    language_code = "-".join(voice_name.split("-")[:2])
    text_input = tts.SynthesisInput(text=text)
    voice_params = tts.VoiceSelectionParams(
        language_code=language_code, name=voice_name
    )
    audio_config = tts.AudioConfig(audio_encoding=tts.AudioEncoding.LINEAR16)

    client = tts.TextToSpeechClient(client_options={"api_key":API_KEY})
    response = client.synthesize_speech(
        input=text_input,
        voice=voice_params,
        audio_config=audio_config,
    )

    filename = f"{voice_name}.wav"
    with open(filename, "wb") as out:
        out.write(response.audio_content)
        print(f'Generated speech saved to "{filename}"')
def play_wav_file(file_path):
    # Load the audio file
    wave_obj = sa.WaveObject.from_wave_file(file_path)

    # Play the audio file
    play_obj = wave_obj.play()

    # Wait for the playback to finish
    play_obj.wait_done()

def doEverything():
    led.pulse()
    # print("press")
    user_prompt = "生成一段简短的土味情话,不超过50个字"
    voice = "cmn-CN-Wavenet-B"
    love_sentence = generate_love_sentence(user_prompt)
    print("Generated love sentence:", love_sentence)
    text_to_wav(voice, love_sentence)
    wav_file_path = 'cmn-CN-Wavenet-B.wav'
    play_wav_file(wav_file_path)
    led.off()

# led_ready.blink(on_time=.1,off_time=3,background=True)
button = Button("BOARD"+button_pin,hold_repeat=True)
button.when_pressed = doEverything
pause()
