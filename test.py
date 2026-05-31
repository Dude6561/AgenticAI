from dotenv import load_dotenv
from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.messages import SystemMessage, HumanMessage, AIMessage, ToolMessage

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash")

# for chunk in model.stream("what is your name? give me in 200 words"):
#     print(chunk.text, end="|", flush=True)

#batch inputs
# @tool
# def get_weather(location:str) -> str:
#     """Get the current weather for a given location."""
#     return f"The weather in {location} is sunny and its 40degrees celsius"

# model_with_tool = model.bind_tools([get_weather])
# response = model_with_tool.invoke("What is the weather in New York?")
# print(response)


# message types
# system message = tells model how to bechave
# user message = input from user
# ai message = response from model
# tool message =  ai message can contail tool call

messages = [
    SystemMessage("You are poetry expert"),
    HumanMessage("Write a pomen about the sea."),
]

response = model.invoke (messages)
print(response.text)