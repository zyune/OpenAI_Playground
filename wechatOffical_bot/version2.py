import werobot
import openai

robot = werobot.WeRoBot(token='yinzheng1998')

# Set up OpenAI API key
openai.api_key = "sk-XXXX"

# Set up conversation history dictionary
history = {}


def generate_response(prompt):
    # Use conversation history to generate response
    context = history.get(prompt, "")
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=context + prompt,
        temperature=0.5,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    message = response.choices[0].text

    # Update conversation history
    history[prompt] = context + prompt + message

    return message.strip()


@robot.handler
def hello(messages):
    print(messages.content)
    response = generate_response(messages.content)
    return response


robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.run()
