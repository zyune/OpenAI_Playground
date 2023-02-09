import openai
response = openai.Moderation.create(
    # 输入你想说的话在这，可以试用暴力，sexual的话术。看返回值
    input="输入你想说的话在这，可以试用暴力，sexual的话术。看返回值"
)
output = response["results"]
print(output)
