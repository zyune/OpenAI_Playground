import requests


import requests


def generate_text(prompt):
    api_key = "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"
    model = "text-davinci-002"
    completions_endpoint = f"https://api.openai.com/v1/engines/{model}/completions"

    prompt = (f"{prompt}"
              f"\n\n context: \n"
              )
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "prompt": prompt,
        "max_tokens": 100,
        "n": 1,
        "stop": None,
        "temperature": 0.5,
    }
    response = requests.post(completions_endpoint,
                             headers=headers, json=data).json()
    message = response["choices"][0]["text"]
    return message


while True:
    prompt = input("You: ")
    response = generate_text(prompt)
    print("AI: " + response)


