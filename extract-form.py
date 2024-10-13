import requests
import json
import time
from requests.exceptions import RequestException

# Load credentials
with open("credentials.json") as f:
    config = json.load(f)

# Define your endpoint and API key
endpoint = config["open-ai-llm"]["endpoint"]
api_key = config["open-ai-llm"]["api-key"]

# Define the headers, including the API key for authentication
headers = {
    "Content-Type": "application/json",
    "api-key": api_key
}

# Define the payload (prompt, model, etc.)
data = {
    "model": "gpt-3.5-turbo",  # or 'gpt-3.5-turbo' depending on your model
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ],
    "temperature": 0.7,  # Control randomness: 0 = deterministic, 1 = more creative
    "max_tokens": 100    # Limit the response length
}

# Function to send the request and check for the response in a loop
def send_request_with_check():
    response_received = False
    attempt_count = 0

    while not response_received:
        try:
            print(f"Attempt {attempt_count + 1}: Sending request...")
            response = requests.post(
                f"{endpoint}", 
                headers=headers, json=data
            )
            
            if response.status_code == 200:
                response_data = response.json()
                print("Response:", response_data["choices"][0]["message"]["content"])
                response_received = True  # Break the loop when response is successfully received
            else:
                print(f"Error: {response.status_code}")
                print(f"Message: {response.text}")
            
            # Increment attempt counter
            attempt_count += 1
            # Wait before trying again (to avoid overwhelming the server)
            time.sleep(2)

        except RequestException as e:
            print(f"An error occurred: {e}")
            time.sleep(2)  # Wait before retrying

# Run the function
send_request_with_check()
