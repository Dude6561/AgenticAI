from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash")

# for chunk in model.stream("what is your name? give me in 200 words"):
#     print(chunk.text, end="|", flush=True)

#batch inputs

responses = model.batch(["what is your name? give me in 200 words", "what is your favorite color?"])
for response in responses:
    print(response.text)

