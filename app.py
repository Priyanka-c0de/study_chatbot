import datetime
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from pymongo import MongoClient
from datetime import datetime, timezone
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
mongo_uri = os.getenv("MONGO_URI")

client = MongoClient(mongo_uri)
db = client["chat"]
collection = db["users"]

app = FastAPI()

class ChatRequest(BaseModel):
    user_id: str
    question: str

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a specialized AI Study Assistant."" Your primary goal is to help students understand academic concepts, solve learning-related problems, and organize their study materials.Only answer for academic related qestions and remember about the user .""Use bullet points and bold text for clarity."),
        ("placeholder", "{history}"),
        ("user", "{question}")
    ]
)

llm = ChatGroq(api_key = groq_api_key, model="openai/gpt-oss-20b")
chain = prompt | llm

def get_history(user_id):
    chats = collection.find({"user_id": user_id}).sort("timestamp", 1)
    history = []

    for chat in chats:
        history.append((chat["role"], chat["message"]))
    return history

@app.get("/") 
def home():
    return {"message": "Hello! I am your AI Study Assistant. How can I help you excel in your studies today?"}

@app.post("/chat")
def chat(request: ChatRequest):
    history = get_history(request.user_id)
    response = chain.invoke({"history": history, "question": request.question})

    collection.insert_one({
        "user_id": request.user_id,
        "role": "user",
        "message": request.question,
        "timestamp": datetime.now(timezone.utc)
    })

    collection.insert_one({
        "user_id": request.user_id,
        "role": "assistant",
        "message": response.content,
        "timestamp": datetime.now(timezone.utc)
    })

    return {"response" : response.content}