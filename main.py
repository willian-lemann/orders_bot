from fastapi import FastAPI
from bot_main import execute

app = FastAPI()

@app.post("/")
def order_bot():
   execute()
      
    
