from config import model, WHITE_SYSTEM_PROMPT





def white(user_input):

    try:
        response = model.invoke([
            {"role": "system", "content": WHITE_SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ])


        print(response)
        return response
    except Exception as e:
        print(f"Error: {e}")
        return "Sorry, something went wrong."

