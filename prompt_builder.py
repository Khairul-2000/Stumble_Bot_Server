from persona_config import EVENT_GUIDELINES 



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