from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
from os import environ

# initialize the app
app = FastAPI()

# enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # TODO: Change this to the URL of Nancy app
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# define a root `/` endpoint
@app.get("/")
def root():
    return {"message": "Hello World"}


# Run the FastAPI app with Uvicorn
if __name__ == "__main__":
    port = int(environ.get("PORT", 8000))
    uvicorn.run("main:app", host="127.0.0.1", port=port, reload=True)