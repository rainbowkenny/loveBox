import pyttsx3
import openai

# Set up OpenAI API
openai.api_key = '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'

# Initialize the TTS engine
engine = pyttsx3.init()

def generate_love_sentence(prmpt):
    # Use OpenAI's GPT-3 to generate a love sentence
    # response = openai.ChatCompletion.create(
    completion = openai.completions.create(
      model="gpt-3.5-turbo-instruct",
      prompt=prmpt,
      max_tokens=30,
      temperature=1,
      n = 2
    )
    for i in range(len(completion.choices)):
        print(f"{i}: {completion.choices[i].text.strip()}")
    return completion.choices[0].text.strip()

def speak(text):
    # Use TTS engine to speak the generated text
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    # Example usage
    user_prompt = "Generate a short romantic love sentence for my partner "
    # user_prompt = "Generate a few short romantic love sentences for my partner "
    love_sentence = generate_love_sentence(user_prompt)
    # print("Generated love sentence:", love_sentence)
    # speak(love_sentence)
