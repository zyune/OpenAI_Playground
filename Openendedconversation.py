import os
import openai
# Use your own OpenAI API key here
openai.api_key = os.getenv("OPENAI_API_KEY")


def chat_with_gpt3(prompt):
    completions = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": prompt}
    ]
)

    message = completions['choices'][0]['message']['content']
    return message


while True:
    user_input = input("You: ")
    if user_input == "exit":
        break
    response = chat_with_gpt3(user_input)
    print(f"ChatGPT: {response}")
