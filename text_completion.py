import openai
import os
# Apply the API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define the prompt
while True:
    prompt = "How does a message queueing system achieve message integrity; validity? How does it make sure that message is delivered at least once."
    
    your_description = input("Enter your question for GPT-3 model: ")
    # Generate the completion
    completion = openai.Completion.create(
        engine="davinci-instruct-beta",
        prompt=your_description,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )
    
    # Get the response
    message = completion.choices[0].text
    print(message)
    