import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
API_KEY = os.getenv("API_KEY")

class LLMResponse:
    def __init__(self):
        self.client = OpenAI(
            base_url = "https://integrate.api.nvidia.com/v1",
            api_key = API_KEY
        )
    
    def get_response(self):
        return self.response


