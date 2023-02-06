# Import necessary packages
import os
import openai
import requests
import io
from PIL import Image
# Set the API key for the OpenAI API
openai.organization = "org-ib1ZWJAduDkTLlWWceXwAUes"
openai.api_key = os.getenv("OPENAI_API_KEY")
# Use OpenAI API to create an image based on the given prompt
response = openai.Image.create(
    prompt="a fat and talent Chinese male computer science   student named Jerry ",
    n=1,
    size="1024x1024"
)
# Get the URL of the generated image
image_url = response['data'][0]['url']
# Use requests to retrieve the image content from the URL
response = requests.get(image_url)
# Use the Image package from PIL to open the image content
img = Image.open(io.BytesIO(response.content))
# Save the image to a file named "yune.jpg" in the "img" folder
img.save("img/leren.jpg")
