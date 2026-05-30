import os
from dotenv import load_dotenv
from langchain.agents import create_agent

load_dotenv()


os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

def get_weather(city: str) -> str:
    """Get the current weather for a given city."""
    return f"The weather in {city} is sunny"

agent = create_agent(
    model="google_genai:gemini-3.5-flash",
    tools=[get_weather],
    system_prompt="You are a helpful assistant for the user.",
)

# Invoke the agent
response = agent.invoke(
    {"messages": [{"role": "user", "content": "What is the weather in New York?"}]}
)

print(response["messages"])