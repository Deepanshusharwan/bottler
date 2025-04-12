from openai import OpenAI

client = OpenAI(
  api_key="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"
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "write a haiku about ai"}
  ]
)

print(completion.choices[0].message);

