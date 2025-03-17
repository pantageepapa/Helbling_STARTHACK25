import requests

API_KEY = "sk-Czp5WvFa8zWm8LL1CgC74YZEa5bLNDCs2PT2KXjQzaT3BlbkFJ3RjItB0TigG3MJ0VHvwq6twg_qvzTFlXWnMnxkxqoA"
URL = "https://api.openai.com/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

data = {
    "model": "gpt-4o",
    "messages": [{"role": "user", "content": "Hello, how are you?"}]
}

response = requests.post(URL, headers=headers, json=data)

print(response.json())
