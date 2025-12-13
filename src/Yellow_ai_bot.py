from persona_config import YELLOW_SYSTEM_PROMPT
from model_config import model



def yellow(user_input):

    try:
        response = model.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": YELLOW_SYSTEM_PROMPT},
                {"role": "user", "content": user_input}
            ]
        )


        print(response.choices[0].message.content)
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error: {e}")
        return "Sorry, something went wrong."

