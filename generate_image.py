import os
import openai
import requests
import io
from PIL import Image
openai.organization = "org-ib1ZWJAduDkTLlWWceXwAUes"
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Image.create(
    prompt="a brilliant and handsome talent computer science master student name Yune who",
    n=1,
    size="1024x1024"
)
image_url = response['data'][0]['url']
response = requests.get(image_url)
img = Image.open(io.BytesIO(response.content))
# img = Image.open(image_url)
img.save("img/yune.jpg")
