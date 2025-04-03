from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from models.chat import ChatRequest
from services.chat import llm

app = FastAPI()

@app.get("/")
async def root():
    return JSONResponse(content={"message": "Hello!"}, status_code=status.HTTP_200_OK)

@app.post("/chat")
async def chat(chat_request: ChatRequest):
    prompt=f"""
    you are a friendly chatbot who responds to messages
    the user who has sent you a message is called {chat_request.user}
    the message is {chat_request.message}
    """
    response= await llm.ainvoke(prompt)
    return JSONResponse(content={"message": response}, status_code=status.HTTP_200_OK)