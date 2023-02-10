import openai
content_to_classify = "输入你想说的话"

response = openai.Completion.create(
    model="content-filter-alpha",
    prompt="<|endoftext|>"+content_to_classify+"\n--\nLabel:",
    temperature=0,
    max_tokens=1,
    top_p=0,
    logprobs=10
)
print(response)
