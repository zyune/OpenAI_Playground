import os
import openai
openai.organization = "org-ib1ZWJAduDkTLlWWceXwAUes"
openai.api_key = os.getenv("OPENAI_API_KEY")

dir(openai)