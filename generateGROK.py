from openai import AsyncOpenAI
from config import AI_TOKEN_GROK

client = AsyncOpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=AI_TOKEN_GROK,
)


async def ai_generate2(text: str):
  completion2 = await client.chat.completions.create(
    model="x-ai/grok-4.1-fast",
    messages=[
      {
        "role": "user",
        "content": text
      }
    ]
  )
  print(completion2)
  return completion2.choices[0].message.content