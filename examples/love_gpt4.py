# import openai
# import pyttsx3

# # Set up OpenAI API
# openai.api_key = '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'

# # Initialize the TTS engine
# engine = pyttsx3.init()

# def generate_love_sentence(prmpt):
#     # Use OpenAI's GPT-3 to generate a love sentence
#     # response = openai.ChatCompletion.create(
#     completion = openai.completions.create(
#       model="gpt-3.5-turbo-instruct",
#       prompt=prmpt,
#       max_tokens=30,
#       temperature=1
#     )
#     return completion.choices[0].text.strip()

# def speak(text):
#     # Use TTS engine to speak the generated text
#     engine.say(text)
#     engine.runAndWait()

# if __name__ == "__main__":
#     # Example usage
#     user_prompt = "Generate a short romantic love sentence for my partner "
#     love_sentence = generate_love_sentence(user_prompt)
#     print("Generated love sentence:", love_sentence)
#     speak(love_sentence)
from openai import OpenAI
aikey = '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'
client = OpenAI(api_key=aikey)

completion = client.chat.completions.create(
  model="gpt-4-turbo-preview",
  messages=[
    {"role": "system", "content": "I'm a 15yr old boy.You are a comedian"},
    # {"role": "user", "content": "Tell me a joke!"}
    {"role": "user", "content": "Tell me 5 jokes!"}
  ],
  n = 1,
  temperature = 1
)
responses = completion.choices[0].message.content

strings = responses.split("\n\n")[1:-1]

# Printing each joke separately
for entry in strings:
    print(entry.strip())

# for i in range(len(completion.choices)):
#     print(f"{i}: {completion.choices[i].message.content}")
# print(completion.choices[0].message.content)
# print(completion.choices[1].message.content)
