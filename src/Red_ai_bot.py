from config import model, RED_SYSTEM_PROMPT





def red(user_input):

    try:
        response = model.invoke([
            {"role": "system", "content": RED_SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ])


        print(response)
        return response
    except Exception as e:
        print(f"Error: {e}")
        return "Sorry, something went wrong."

