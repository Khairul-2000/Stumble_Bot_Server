from config import model, JOE_SYSTEM_PROMPT





def joe(user_input):

    try:
        response = model.invoke([
            {"role": "system", "content": JOE_SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ])


        print(response)
        return response
    except Exception as e:
        print(f"Error: {e}")
        return "Sorry, something went wrong."