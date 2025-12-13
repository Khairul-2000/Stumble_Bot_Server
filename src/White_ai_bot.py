from persona_config import WHITE_SYSTEM_PROMPT
from model_config import model






def white(user_input):

    try:
        response = model.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": WHITE_SYSTEM_PROMPT},
                {"role": "user", "content": user_input}
            ]
        )


        print(response.choices[0].message.content)
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error: {e}")
        return "Sorry, something went wrong."

