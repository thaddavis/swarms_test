import os

from dotenv import load_dotenv
load_dotenv()

from swarms.models import Anthropic

# Initialize an instance of the Anthropic class
model = Anthropic(anthropic_api_key=os.getenv("ANTHROPIC_API_KEY"), streaming=True)

# Using the run method

completion_1 = model.run("What is the capital of France? Answer in 100 to 200 words.")
print(completion_1)