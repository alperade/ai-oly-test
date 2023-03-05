import openai
import keys

openai.api_key =keys.OPENAI_API_KEY

def summary(input_from_slither):
    messages = []

    message = input_from_slither + "summarize the results from slither"
    messages.append({"role": "system", "content": message})
    response_category = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    reply = response_category["choices"][0]["message"]["content"]
    messages.append({"role": "system", "content": reply})
    return reply
