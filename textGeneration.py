import config
from openai import OpenAI
import re

aikey=config.OPEN_AI_KEY
client = OpenAI(api_key=aikey)
def clean_responses(raw_responses):
    strings = raw_responses.split("\n")[1:-1]
    filtered_array = [string for string in strings if string]
    for i in range(len(filtered_array)):
        filtered_array[i] =re.sub(r'^\d*\.\s*', '',filtered_array[i])
    return filtered_array
    
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
    result = clean_responses(responses)[0]
    return result 


