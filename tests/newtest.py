from openai import OpenAI
import requests

api_key = ''#future me put api key here
url = 'https://api.openai.com/v1/engines/davinci/completions'

headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

data = {
    "prompt": "Once upon a time",
    "max_tokens": 50
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    result = response.json()
    print(result)
else:
    print(f"Error: {response.status_code} - {response.text}")