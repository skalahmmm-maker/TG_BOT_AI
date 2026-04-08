from openai import AsyncOpenAI
from config import AI_TOKEN_DEEP

client = AsyncOpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=AI_TOKEN_DEEP,
)


async def ai_generate(text: str):
  completion = await client.chat.completions.create(
    model="deepseek/deepseek-chat",
    messages=[
      {
        "role": "user",
        "content": text
      }
    ]
  )
  print(completion)
  return completion.choices[0].message.content