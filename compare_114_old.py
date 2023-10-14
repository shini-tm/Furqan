import requests
import json

url = "https://api.quran.com/api/v4/quran/translations/131?chapter_number=114"
#url = "https://api.quran.com/api/v4/verses/by_chapter/1?words=true&translations=217"
# 131 : Dr. Mustafa Khattab, the Clear Quran

payload={
  "verse_key": "1:1"
}
headers = {
  'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

json_response = json.loads(response.text)
formatted_json = json.dumps(json_response, indent=4, sort_keys=True)
print(formatted_json)
