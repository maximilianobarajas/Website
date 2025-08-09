import os
import json
from openai import OpenAI
from templates.prompts import get_subtopic_prompt

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def get_subtopics(main_topic:str="", num:int=0):
    if main_topic=='' or num == 0:
        return {"msg":"Not a valid request"}
    
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": "You are a helpful writing assistant."},
            {"role": "user", "content": get_subtopic_prompt(main_topic=main_topic, num=num)}
        ]        
    )
    json_response = json.loads(response.choices[0].message.content)

    return json_response.get("subtopics", [])

