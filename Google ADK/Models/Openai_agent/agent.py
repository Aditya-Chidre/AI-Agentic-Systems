from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm
from dotenv import load_dotenv
load_dotenv()
import os

api_key = os.getenv("OPENAI_API_KEY")

openai_model = LiteLlm(model="openai/gpt-5-nano",
                       api_key=api_key
                       )

root_agent = LlmAgent(
    model=openai_model,
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge'
)

