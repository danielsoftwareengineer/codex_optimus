from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uuid
import random
import string

app = FastAPI()
storage = {}

class GenerateRequest(BaseModel):
    palindrome: bool

class GenerateResponse(BaseModel):
    id: str
    result: str

class ResultResponse(BaseModel):
    id: str
    result: str

def generate_palindrome():
    half = ''.join(random.choices(string.ascii_lowercase, k=3))
    return half + half[::-1]

def generate_non_palindrome():
    while True:
        result = ''.join(random.choices(string.ascii_lowercase, k=6))
        if result != result[::-1]:
            return result

@app.post("/generate", response_model=GenerateResponse)
def generate_string(request: GenerateRequest):
    string_id = str(uuid.uuid4())
    if request.palindrome:
        result = generate_palindrome()
    else:
        result = generate_non_palindrome()
    storage[string_id] = result
    return {"id": string_id, "result": result}

@app.get("/result/{string_id}", response_model=ResultResponse)
def get_result(string_id: str):
    if string_id not in storage:
        raise HTTPException(status_code=404, detail="Result not found")
    return {"id": string_id, "result": storage[string_id]}
