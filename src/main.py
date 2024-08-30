import os
from dotenv import load_dotenv
load_dotenv()

from swarms import OpenAIChat

# Get the API key from the environment variables
api_key = os.environ.get("OPENAI_API_KEY")

# Initialize the OpenAIChat model
model = OpenAIChat(
    openai_api_key=api_key, model_name="gpt-4o-mini", temperature=0.1
)

print("Environment set up and model initialized successfully!")
