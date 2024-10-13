import json
import requests

with open("credentials.json") as f:
    config = json.load(f)

# Define your endpoint and API key
endpoint = config["open-ai-llm"]["endpoint"]
api_key = config["open-ai-llm"]["api-key"]

# Define the function to query the LLM
def query_llm(text, question):
    headers = {
        "Content-Type": "application/json",
        "api-key": api_key
    }
    
    data = {
        "messages": [
            {"role": "user", "content": f"{text}\n\n{question}"}
        ]
    }
    
    response = requests.post(endpoint, headers=headers, json=data)
    return response.json()["choices"][0]["message"]["content"]

# Example usage
combined_text = "..."  # Your combined text from the JSON response
question = "What is the user's answer to the question 'What is your date of birth?'"
answer = query_llm(combined_text, question)

print("Extracted Answer:", answer)
