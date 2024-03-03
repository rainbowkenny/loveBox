import config
from openai import OpenAI
import re

aikey=config.OPEN_AI_KEY
client = OpenAI(api_key=aikey)
def clean_responses(raw_responses):
    print("raw:")
    print(raw_responses)
    strings = raw_responses.split("\n")
    print("strings:")
    print(strings)
    filtered_array = [string for string in strings if string]
    for i in range(len(filtered_array)):
        filtered_array[i] =re.sub(r'^\d*\.\s*', '',filtered_array[i])
    return filtered_array
    
def generate_sentences(user_prompt):
    completion = client.chat.completions.create(
      model="gpt-4-turbo-preview",
      messages=[
        {"role": "system", "content":user_prompt},
        {"role": "user", "content":user_prompt}
      ],
      n = 1,
      temperature = 0.7
    )
    responses = completion.choices[0].message.content
    cleaned_responses = clean_responses(responses)
    print("cleaned_responses:")
    print(cleaned_responses)
    return cleaned_responses


