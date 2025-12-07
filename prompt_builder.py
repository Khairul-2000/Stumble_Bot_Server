


def build_prompt(bot_persona: str, event_type: str, event_data: dict, context: dict):
    username = event_data.get("username", "@User")

    # EVENT-SPECIFIC INSTRUCTIONS
    EVENT_GUIDELINES = {
        "NEW_USER_JOINED": "Welcome them warmly and make them feel safe.",
        "SAD_POST_DETECTED": "Be gentle, validating, and emotionally supportive.",
        "USER_RELAPSE_MENTIONED": "Acknowledge the setback without shame. Keep it supportive.",
        "USER_TAGGED_BOT": "Answer their question or acknowledge the tag.",
        "CHAT_SILENT": "Restart the conversation gently.",
        "DAILY_CHECK_IN": "Give a warm, short check-in message.",
        "TRIBE_MOOD_LOW": "Support the whole group with empathy.",
        "BADGE_UNLOCKED": "Celebrate the achievement clearly and warmly.",
        "MOOD_CHECKIN_COMPLETED": "Acknowledge their emotional honesty.",
        "STREAK_MILESTONE": "Celebrate their consistency.",
        "POINTS_MILESTONE": "Recognize their progress enthusiastically.",
        "PROGRESS_MILESTONE_COMPLETED": "Celebrate growth without exaggeration."
    }

    EVENT_RULE = EVENT_GUIDELINES.get(event_type, "Respond appropriately to the event.")

    # GLOBAL STRICT RULES (Fixes all the issues)
    STRICT_RULES = f"""
STRICT NON-NEGOTIABLE RULES:
- Response MUST be 1–2 sentences only. Never more.
- MUST be under 280 characters.
- MUST mention {username}.
- Use max 1 emoji.
- NO lists, no bullets, no long explanations.
- Do NOT give instructions or steps unless you are Joe AND the event is streak/progress related.
- Sara and Blue NEVER give steps, advice, or actions.
- Yellow NEVER gives steps.
- Responses must match the bot’s personality AND the event type tone.
- If event is emotional (SAD_POST_DETECTED, TRIBE_MOOD_LOW, RELAPSE), soften tone even for Joe/Yellow.
"""

    # FINAL PROMPT SENT TO THE LLM
    prompt = f"""
You are {bot_persona}.

EVENT TYPE: {event_type}
EVENT GOAL: {EVENT_RULE}

USERNAME: {username}

CONTEXT:
Recent Messages: {context.get("recent_messages", [])}
Current User Info: {context.get("current_user", {})}
Tribe Mood: {context.get("tribe_mood", {})}

{STRICT_RULES}

Now write a response that:
- Fits the personality
- Matches the event type
- Is short, warm, and human
- Follows ALL rules above

Final Output:
"""

    return prompt
