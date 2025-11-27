from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="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",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)