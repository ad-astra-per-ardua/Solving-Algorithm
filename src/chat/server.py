from fastapi import *
from pydantic import BaseModel
from typing import List
import json
import os

class Chat(BaseModel):
    user: str
    message: str

app = FastAPI()

chat_list = []

@app.post("/chat")
async def create_chat(chat: Chat):
    chat_list.append(chat.dict())
    with open("chat.json", "w") as write_file:
        json.dump(chat_list, write_file)
    return chat

@app.get("/chat", response_model=List[Chat])
async def read_chats():
    if os.path.exists("chat.json"):
        with open("chat.json", "r") as read_file:
            data = json.load(read_file)
        return data
    else:
        raise HTTPException(status_code=404, detail="File not found")

@app.delete("/chat")
async def delete_chats():
    if os.path.exists("chat.json"):
        os.remove("chat.json")
        return {"message": "All chats have been deleted."}
    else:
        raise HTTPException(status_code=404, detail="File not found")
