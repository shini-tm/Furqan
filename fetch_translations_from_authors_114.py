import requests
import json

# Load the translation authors data from "translation_authors.json"
with open("translation_authors.json", "r") as authors_file:
    translation_authors = json.load(authors_file)

# Define the chapter number for which you want to fetch translations
chapter_number = 114

# Create a dictionary to store translations for each verse
verse_translations = {}

# Fetch translations for each verse
for author in translation_authors:
    author_id = author["id"]
    author_name = author["author_name"]

    # Construct the URL for fetching translations
    url = f"https://api.quran.com/api/v4/quran/translations/{author_id}?chapter_number={chapter_number}"

    headers = {
        'Accept': 'application/json'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        json_response = json.loads(response.text)
        translations = json_response["translations"]
        for index, translation in enumerate(translations):
            verse_key = str(index + 1)  # Index + 1
            text = translation["text"]

            # Create or append the translation to the verse_translations dictionary
            if verse_key in verse_translations:
                verse_translations[verse_key].append(text)
            else:
                verse_translations[verse_key] = [text]

# Print translations side by side for each verse
for verse_key, translations in verse_translations.items():
    print(f"Verse {verse_key}: {translations}")

# Optionally, you can save the data to a JSON file for further analysis
with open("chapter_114_translations.json", "w") as output_file:
    json.dump(verse_translations, output_file, indent=4)

print("Translations for chapter 114 have been fetched and printed.")
