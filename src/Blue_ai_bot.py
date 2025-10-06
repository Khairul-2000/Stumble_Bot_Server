from config import model, BLUE_SYSTEM_PROMPT



def blue(user_input):

    try:
        response = model.invoke([
            {"role": "system", "content": BLUE_SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ])


        print(response)
        return response
    except Exception as e:
        print(f"Error: {e}")
        return "Sorry, something went wrong."





