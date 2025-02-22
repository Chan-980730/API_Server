from fastapi import FastAPI, Query
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles

import app_model

app = FastAPI() # 서버 생성

model = app_model.AppModel()

@app.get("/say") # say라고 했을 때 밑에 함수 불러오기
def say_app(text: str = Query()):
    response = model.get_response(text)
    return {"content" : response.content}

@app.get("/translate")
def translate(text: str = Query(), language: str = Query()):
    response = model.get_prompt_response(language, text)
    return response.content