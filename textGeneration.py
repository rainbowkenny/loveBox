import config
from openai import OpenAI
import re

aikey=config.OPEN_AI_KEY
client = OpenAI(api_key=aikey)
def generate_love_sentence(prmpt):
    completion = client.chat.completions.create(
      model="gpt-4-turbo-preview",
      messages=[
        {"role": "system", "content":prmpt},
        {"role": "user", "content": "Tell me 5 jokes!"}
      ],
      n = 1,
      temperature = 0.7
    )
    responses = completion.choices[0].message.content
    strings = responses.split("\n")[1:-1]
    filtered_array = [string for string in strings if string]
    sentence = filtered_array[0]
    result =re.sub(r'^\d*\.\s*', '',sentence)

    return result 


