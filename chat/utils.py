import openai
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY

def generate_reply(messages):
    print(settings.OPENAI_API_KEY)
    llm_messages = [{"role": m.sender, "content": m.text} for m in messages]
    print("here", llm_messages)
    completion = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=llm_messages
    )
    print("output=",completion)
    return completion.choices[0].message["content"]
