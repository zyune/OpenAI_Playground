import werobot
robot = werobot.WeRoBot(token='yinzheng1998')
import openai
# 这个api_key首先需要有一个openai账号，然后在个人账户下生成的。
# 具体参考：https://blog.csdn.net/ysvae/article/details/128203722
openai.api_key="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"
def generate_response(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    message = response.choices[0].text
    return message.strip()

@robot.handler
def hello (messages):
    print(messages.content)
    return generate_response(messages.content)

robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.run()