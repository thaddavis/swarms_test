import os
import asyncio
from dotenv import load_dotenv
load_dotenv()

from swarms.models import Anthropic

# Initialize an instance of the Anthropic class
model = Anthropic(anthropic_api_key=os.getenv("ANTHROPIC_API_KEY"), streaming=True)

async def main():

  async for evt in model.astream_events("What is the capital of France? Answer in 100 to 200 words.", version="v1"):
    print(evt)

asyncio.run(main())