from dotenv import load_dotenv
from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field


load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash")


class Movie(BaseModel):
    title: str = Field(..., description="The title of the movie")
    director: str = Field(..., description="The director of the movie")
    release_year: int = Field(..., description="The release year of the movie")
    director: str = Field(..., description="The director of the movie")
    rating: float = Field(..., description="The rating of the movie")

model_with_structured_output = model.with_structured_output(Movie)
response = model_with_structured_output.invoke("What is the movie Openheimer about?")
print(response)