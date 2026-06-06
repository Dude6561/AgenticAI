from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain.agents.middleware import SummarizationMiddleware
from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq
from langgraph.checkpoint.memory import InMemorySaver

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
model = ChatGoogleGenerativeAI(model="gemini-3.5-flash")
summarization_model = ChatGroq(model="llama-3.1-8b-instant")
checkpointer = InMemorySaver()

agent = create_agent(
    model=summarization_model,
    tools=[],
    checkpointer=checkpointer,
    middleware=[
        SummarizationMiddleware(
            model=summarization_model,
            trigger=("messages", 4),
            keep=("messages", 2),
        )
    ],
)

config = {
    "configurable": {
        "thread_id": "user-1"
    }
}


questions = [
    "What is the capital of France?",
    "What is the capital of Germany?",
    "What is the capital of Italy?",
    "What is the capital of Spain?",
    "What is the capital of Portugal?",
    
]
for question in questions:
    response = agent.invoke(
        {
            "messages": [
                HumanMessage(content=question)
            ]
        },
        config,
    )

    last_message = response["messages"][-1]
    content = last_message.content
    print(content[0]["text"] if isinstance(content, list) else content)