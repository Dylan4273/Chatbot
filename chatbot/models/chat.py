from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    message: str = Field(description="The message request")
    user:str = Field(description="Requesting user")