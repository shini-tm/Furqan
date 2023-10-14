import requests
import json

url = "https://api.quran.com/api/v4/resources/translations?language=english"

payload={"language": "english"}
headers = {
  'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

json_data = json.loads(response.text)
formatted_json = json.dumps(json_data, indent=4, sort_keys=True)

# Filter and keep only the objects with "language_name": "english" at the top
filtered_data = [translation for translation in json_data["translations"] if translation["language_name"] == "english"]

# Extract and save the "id," "name," and "author_name" fields into a file
output_data = []
for translation in filtered_data:
    output_data.append({
        "id": translation["id"],
        "name": translation["name"],
        "author_name": translation["author_name"]
    })

# Save the data to a JSON file
with open("translation_authors.json", "w") as file:
    json.dump(output_data, file, indent=4)

print("Data saved to 'translation_authors.json'")