from openai import OpenAI

client = OpenAI(
  api_key="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")

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "write a haiku about ai"}
  ]
)

print(completion.choices[0].message);

