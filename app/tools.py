import os
import requests
from app.prompts import(TREND_IDEA_PROMPT,REEL_SCRIPT_PROMPT,HASHTAG_PROMPT,CONTENT_REVIEW_PROMPT)

OLLAMA_URL="http://localhost:11434/api/generate"
MODEL_NAME="gemma3:4b"

def call_ollama(prompt:str)->str:
    payload={
        "model":MODEL_NAME,
        "prompt":prompt,
        "stream":False
    }
    try:
        response=requests.post(OLLAMA_URL,json=payload,timeout=300)
        response.raise_for_status()
        return response.json().get("response","No response generated")
    except Exception as e:
        return f"Error communication with ollama: {str(e)}"


def generate_trend_ideas(topic:str,tone:str)->str:
    prompt=TREND_IDEA_PROMPT.format(topic=topic,tone=tone)
    return call_ollama(prompt)


def generate_reel_script(concept:str,tone:str)->str:
    prompt=REEL_SCRIPT_PROMPT.format(concept=concept,tone=tone)
    return call_ollama(prompt)


def generate_hashtags(topic:str)->str:
    prompt=HASHTAG_PROMPT.format(topic=topic)
    return call_ollama(prompt)

def review_content(content:str)->str:
    prompt=CONTENT_REVIEW_PROMPT.format(content=content)
    return call_ollama(prompt)

def save_to_file(topic:str,content:str,output_type:str="script")->str:
    sanitized_topic=topic.lower().replace(' ','-')

    if output_type=="post":
        dir_path="outputs/generated_posts"
        filename=f"{dir_path}/{sanitized_topic}_post.md"
    elif output_type=="script":
        dir_path="outputs/generated_scripts"
        filename=f"{dir_path}/{sanitized_topic}_script.md"
    else:
        dir_path="outputs/saved_results"
        filename=f"{dir_path}/{sanitized_topic}_result.md"

    os.makedirs(dir_path,exist_ok=True)
    with open(filename,"w",encoding="utf-8") as f:
        f.write(content)

    return filename                