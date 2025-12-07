from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import os
from dotenv import load_dotenv
from prompt_builder import build_prompt
from bot_personas_config import BOT_PERSONAS

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
app = FastAPI()


class BotEventRequest(BaseModel):
    bot_name: str
    event_type: str
    event_data: dict
    timestamp: str | None = None


@app.get("/")
async def root():
    return {"message": "Stumble Bot Server is running."}





@app.post("/api/v1/bot-event")
async def handle_bot_event(req: BotEventRequest):

    # Validate bot name
    if req.bot_name.lower() not in BOT_PERSONAS:
        return {"success": False, "error": "Invalid bot_name"}

    # Build prompt
    prompt = build_prompt(
        bot_persona=req.bot_name,
        event_type=req.event_type,
        event_data=req.event_data
    )

    completion = client.chat.completions.create(
    model="gpt-5",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
    )
    message = completion.choices[0].message.content
    print(message)

    # Length validation
    if len(message) > 280:
        message = message[:280]

    return {
        "success": True,
        "response": message
    }
