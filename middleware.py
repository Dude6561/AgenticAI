from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain.agents.middleware import SummarizationMiddleware
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import InMemorySaver

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

checkpointer = InMemorySaver()

agent = create_agent(
    model=model,
    tools=[],
    checkpointer=checkpointer,
    middleware=[
        SummarizationMiddleware(
            model=model,
            trigger=("messages", 10),
            keep=("messages", 3),
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
    "What is the capital of Greece?",
    "What is the capital of Netherlands?",
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

    print(response["messages"][-1].content)