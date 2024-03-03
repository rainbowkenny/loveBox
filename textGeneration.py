import config
import openai
openai.api_key=config.OPEN_AI_KEY

def generate_love_sentence(prmpt):
    # Use OpenAI's GPT-3 to generate a love sentence
    # response = openai.ChatCompletion.create(
    completion = openai.completions.create(
      model="gpt-3.5-turbo-instruct",
      # model="gpt-4-turbo-preview",
      # model="gpt-4",
      prompt=prmpt,
      max_tokens=1000,
      temperature=0.7
    )
    return completion.choices[0].text.strip()
