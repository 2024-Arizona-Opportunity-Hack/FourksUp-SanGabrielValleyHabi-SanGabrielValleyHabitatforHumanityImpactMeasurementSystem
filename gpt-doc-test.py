import time
import json
import requests


filename = "HomePreservationProgram.pdf"

with open("credentials.json") as f:
    config = json.load(f)

# Define your endpoint and API key
endpoint = config["document-ai"]["endpoint"]
api_key = config["document-ai"]["api-key"]

# Define the URL for document analysis
url = f"{endpoint}/formrecognizer/v2.1/layout/analyze"

# Set the headers
headers = {
    "Ocp-Apim-Subscription-Key": api_key,
    "Content-Type": "application/pdf",  # Or "application/json" if using JSON
}

# Open and send the document (PDF or image)
with open(filename, "rb") as f:
    data = f.read()

# Make the request
response = requests.post(url, headers=headers, data=data)

# Check if the request was accepted
if response.status_code == 202:
    print("Request accepted, processing...")
    # Get the operation URL from the response headers or JSON response
    operation_url = response.headers["Operation-Location"]  # Example of how it's returned

    # Poll the operation URL to check the status
    status = ""
    while status != "succeeded":
        response = requests.get(operation_url, headers={"Ocp-Apim-Subscription-Key": api_key})
        result = response.json()
        status = result["status"]
        
        # Wait for a few seconds before polling again
        time.sleep(5)
        print(f"Current status: {status}")

    # Once the status is "succeeded", you can get the results
    print("Processing complete!")
    with open("output.json", "w") as f:
        json.dump(result, f, indent=2)

else:
    print(f"Error: {response.status_code}, {response.text}")
