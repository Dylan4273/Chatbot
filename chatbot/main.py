from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from models.chat import ChatRequest
app = FastAPI()

@app.get("/")
async def root():
    return JSONResponse(content={"message": "Hello!"}, status_code=status.HTTP_200_OK)

@app.post("/chat")
async def chat(chat_request: ChatRequest):
    return JSONResponse(content={"message": f"{chat_request.message} from {chat_request.user}"}, status_code=status.HTTP_200_OK)