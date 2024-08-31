from typing import Final
import os
from dotenv import load_dotenv
import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("prompt", help="The prompt to send to the OpenAI API")
parser.add_argument("file_name", help="Name of the file to save the Python script")
args = parser.parse_args()

api_endpoint = "https://api.openai.com/v1/chat/completions"
load_dotenv()
TOKEN: Final[str] = os.getenv('CLIENT_SECRET')

request_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + TOKEN
}

request_data = {
    "model": "gpt-4o-mini",
    "prompt": f"Write a python script to {args.prompt}. Provide only code no text",
    "max_tokens": 500,
    "temperature": 0.5
}

response = requests.post(api_endpoint, headers = request_headers, json=request_data)

if response.status_code == 200:
    print(response.json()["choices"][0]["text"])
else:
    print(f"Request Failed with status code: {str(response.status_code)}")