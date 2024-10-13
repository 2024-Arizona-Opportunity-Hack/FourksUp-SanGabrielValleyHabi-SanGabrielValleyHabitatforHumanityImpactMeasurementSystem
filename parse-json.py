import json

# Load the JSON data from the Azure response
with open("output.json", "r") as f:
    data = json.load(f)

# Initialize a list to hold lines
lines = []

# Assuming the structure has a 'analyzeResult' key with 'readResults'
for page in data.get("analyzeResult", {}).get("readResults", []):
    for line in page.get("lines", []):
        # Extract the text and add it to the list
        lines.append(line["text"])

# Combine the words into a single string
combined_text = " ".join(lines)

# Print the combined text (for debugging)
print(combined_text)
