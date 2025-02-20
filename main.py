from typing import Union
from fastapi import FastAPI

# model_().py를 가져옴
import model_and
import model_or
import model_xor
import model_not

# model_().py 안에 있는 ()Model 클래스를 생성
model_and = model_and.AndModel()
model_or = model_or.OrModel()
model_xor = model_xor.XorModel()
model_not = model_not.NotModel()

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
    # return ["Hello", "World"]

# /items/{item_id} 경로
# item_id : 경로 매개변수(파라메터)
@app.get("/items/{item_id}") # 엔드포인트(End Point)
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# and
@app.get("/predict_and/left/{left}/right/{right}") 
def predict_and(left: int, right: int):
    result = model_and.predict([left, right])
    return {"result": result}

# or
@app.get("/predict_or/left/{left}/right/{right}") 
def predict_or(left: int, right: int):
    result = model_or.predict([left, right])
    return {"result": result}

# xor
@app.get("/predict_xor/left/{left}/right/{right}") 
def predict_xor(left: int, right: int):
    result = model_xor.predict([left, right])
    return {"result": result}

# not
@app.get("/predict_not/value/{value}") 
def predict_not(value: int):
    result = model_not.predict([value])
    return {"result": result}

@app.get("/train")
def train():
    model_and.train()
    model_or.train()
    model_xor.train()
    model_not.train()
    return {"result = OK"}

