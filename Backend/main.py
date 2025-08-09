from fastapi import FastAPI
from pydantic import BaseModel
import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

from openai import OpenAI
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()

class SubtopicRequest(BaseModel):
    text: str
    subtopic: str
    word_count: int

class IntroRequest(BaseModel):
    main_topic: str
    word_count: int

def generate_text(prompt: str, max_words: int) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful writing assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=max_words * 2
    )
    return response.choices[0].message.content.strip()

@app.post("/generate_subtopic_paragraph")
def generate_subtopic_paragraph(req: SubtopicRequest):
    prompt = (
        f"Given the following text:\n\n{req.text}\n\n"
        f"Write a paragraph of about {req.word_count} words "
        f"about the subtopic '{req.subtopic}', making sure it is cohesive with the given text."
    )
    return {"paragraph": generate_text(prompt, req.word_count)}

@app.post("/generate_intro")
def generate_intro(req: IntroRequest):
    prompt = (
        f"Write an engaging introduction of about {req.word_count} words "
        f"for a text whose main topic is '{req.main_topic}'."
    )
    return {"introduction": generate_text(prompt, req.word_count)}
