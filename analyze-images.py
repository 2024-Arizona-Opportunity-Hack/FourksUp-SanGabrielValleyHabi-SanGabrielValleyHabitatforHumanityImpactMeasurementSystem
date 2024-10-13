import requests
import time
import json

filename = "HomePreservationProgram.pdf"

# Load credentials
with open("credentials.json") as f:
    config = json.load(f)

# Define your endpoint and API key
endpoint = config["vision-ai"]["endpoint"]
api_key = config["vision-ai"]["api-key"]

# The URL for the OCR Read API
ocr_url = f"{endpoint}/vision/v3.2/read/analyze"


# Set headers for the request
headers = {
    "Ocp-Apim-Subscription-Key": api_key,
    "Content-Type": "application/octet-stream"
}

# Open the PDF and send it in the POST request
with open(filename, "rb") as pdf_file:
    response = requests.post(ocr_url, headers=headers, data=pdf_file)

# Check if the POST request was successful (status code 202 indicates accepted)
if response.status_code != 202:
    print(f"Error: {response.status_code}, {response.text}")
    exit()

# The operation-location header contains the URL to poll for the result
operation_url = response.headers["Operation-Location"]

# Poll the result
polling_interval = 5  # seconds
while True:
    # Get the status of the operation
    result_response = requests.get(operation_url, headers={"Ocp-Apim-Subscription-Key": api_key})
    result = result_response.json()

    # Check if the operation is complete
    if result["status"] == "succeeded":
        break
    elif result["status"] == "failed":
        print("OCR analysis failed.")
        exit()
    else:
        print("Waiting for analysis to complete...")
        time.sleep(polling_interval)

# Extract text from the result
for read_result in result["analyzeResult"]["readResults"]:
    for line in read_result["lines"]:
        print(line["text"])
