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
