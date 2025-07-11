from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
chat_db = []

class Message(BaseModel):
    name: str
    message: str

@app.post("/send_message")
def send_message(msg: Message):
    chat_db.append({"name": msg.name, "message": msg.message})
    return {"message": f"{msg.name} said: {msg.message}"}

@app.get("/get_messages")
def get_messages():
    return {"chat": chat_db}
