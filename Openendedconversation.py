import os
import openai
# Use your own OpenAI API key here
openai.api_key = os.getenv("OPENAI_API_KEY")


def chat_with_gpt3(prompt):
    completions = openai.Completion.create(
        engine="davinci-instruct-beta",
        prompt=prompt,

        n=1,
        stop=None,
        temperature=0.5,
        max_tokens=60,
        top_p=1,
        frequency_penalty=0.5,
        presence_penalty=0.6,
    )

    message = completions.choices[0].text
    return message


while True:
    user_input = input("You: ")
    if user_input == "exit":
        break
    response = chat_with_gpt3(user_input)
    print(f"ChatGPT: {response}")
