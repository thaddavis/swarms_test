import os
import asyncio
from dotenv import load_dotenv
load_dotenv()

from swarms_local.swarms.structs import Agent
from swarms_local.swarms.models import Anthropic
from swarms_local.swarms.structs.rearrange import AgentRearrange

llm = Anthropic(anthropic_api_key=os.getenv("ANTHROPIC_API_KEY"), streaming=True)

async def main():

  # Initialize agents for individual tasks
  agent1 = Agent(
      agent_name="Blog generator",
      system_prompt="Generate a blog post like stephen king",
      llm=llm,
      dashboard=False,
      streaming_on=True,
  )

  agent2 = Agent(
      agent_name="Summarizer",
      system_prompt="Summarize the blog post",
      llm=llm,
      dashboard=False,
      streaming_on=True,
  )

  flow = f"{agent1.name} -> {agent2.name}"

  agent_rearrange = AgentRearrange(
    [agent1, agent2], flow, verbose=False, logging=False
  )

  agent_rearrange.run(
    "Generate a blog post on how swarms of agents can help businesses grow."
  )

  # async for evt in agent1.astream_events("What is the capital of France? Answer in 100 to 200 words.", version="v1"):
  #   print(evt)

asyncio.run(main())


# flow = f"{agent1.name} -> {agent2.name}"
