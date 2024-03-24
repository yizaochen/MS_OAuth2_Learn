from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()

"""
POST /myapp/ HTTP/1.1
Host: localhost
Content-Type: application/x-www-form-urlencoded

id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ik1uQ19WWmNB...&state=12345
"""

class Item(BaseModel):
    id_token: str
    state: str
    session_state: str

class Content(BaseModel):
    input: str


@app.post("/sign-in")
async def root(content: Content):
    return content