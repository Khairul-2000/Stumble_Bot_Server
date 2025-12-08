from fastapi import FastAPI
from pydantic import BaseModel


from persona_config  import JOE_SYSTEM_PROMPT, YELLOW_SYSTEM_PROMPT, RED_SYSTEM_PROMPT, SARA_SYSTEM_PROMPT, BLUE_SYSTEM_PROMPT, WHITE_SYSTEM_PROMPT, EVENT_GUIDELINES
from model_config import model


# Persona map
BOT_PERSONAS = {
    "sara": SARA_SYSTEM_PROMPT,
    "blue": BLUE_SYSTEM_PROMPT,
    "joe": JOE_SYSTEM_PROMPT,
    "yellow": YELLOW_SYSTEM_PROMPT,
    "red": RED_SYSTEM_PROMPT,
    "white": WHITE_SYSTEM_PROMPT
}





# ---------------------------------------
# 3. STRICT PROMPT BUILDER
# ---------------------------------------

def build_prompt(bot_persona, event_type, event_data, context):
    username = event_data.get("username", "@User")
    event_rule = EVENT_GUIDELINES.get(event_type, "Respond appropriately to the event.")

    STRICT_RULES = f"""
STRICT NON-NEGOTIABLE RULES:
- Response MUST be 1–2 sentences only.
- MUST be under 280 characters.
- MUST mention {username}.
- DO NOT start the response with the username (e.g., do not begin with "{username}," or "@{username}").
- Begin with a normal sentence, then mention {username} later in the sentence.
- Bad example (do NOT do): "{username}, great job today!"
- Good example: "Great job today—proud of you, {username}."
- Use a maximum of 1 emoji.
- No lists, no formatting, no bullets.
- Sara/Blue/Yellow/White MUST NOT give advice or steps.
- Joe may give short steps ONLY for streak/progress/check-in events.
- Red must be direct but never cruel.
- Emotional events override personality (be softer).
"""

    return f"""
{bot_persona}

EVENT TYPE: {event_type}
EVENT GOAL: {event_rule}
USERNAME: {username}

CONTEXT:
Recent Messages: {context.get("recent_messages", [])}
Current User: {context.get("current_user", {})}
Tribe Mood: {context.get("tribe_mood", {})}

{STRICT_RULES}

Write a single short response that follows ALL rules.
"""


# ---------------------------------------
# 4. REQUEST MODEL
# ---------------------------------------

class BotEvent(BaseModel):
    bot_name: str
    event_type: str
    event_data: dict
    context: dict = {}
    timestamp: str | None = None


# ---------------------------------------
# 5. FINAL FASTAPI ENDPOINT
# ---------------------------------------

app = FastAPI()




@app.get("/")
async def root():
    return {"message": "Stumble Bot Server is running."}


@app.post("/api/v1/bot-event")
async def bot_event_handler(payload: BotEvent):

    bot_name = payload.bot_name.lower()

    if bot_name not in BOT_PERSONAS:
        return {"success": False, "error": "Invalid bot_name"}

    persona = BOT_PERSONAS[bot_name]

    prompt = build_prompt(
        bot_persona=persona,
        event_type=payload.event_type,
        event_data=payload.event_data,
        context=payload.context
    )

    # LLM CALL
    completion = model.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
    )


    text = completion.choices[0].message.content

    # Return cleaned response
    return {
        "success": True,
        "response": text
    }
