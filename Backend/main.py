from fastapi import FastAPI
from services.subtopics import get_subtopics

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.post("/generate_subtopics")
def generate_intro(main_topic, num_topics):
    return {"subtopics": get_subtopics(main_topic=main_topic, num=num_topics)}