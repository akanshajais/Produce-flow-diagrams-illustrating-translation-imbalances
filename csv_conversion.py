import requests
import csv
import pandas as pd

# JSON link
json_url = 'https://en.wikipedia.org/w/api.php?action=query&list=contenttranslationstats&format=json'

# Get JSON data
response = requests.get(json_url)
json_data = response.json()

# Define output CSV file name
output_file = 'data.csv'

# Define CSV header
csv_header = json_data['query']['contenttranslationstats']['pages']

# Define empty list to store data rows
data_rows = []

# Parse JSON data and append rows to data_rows list
for item in csv_header:
    data_rows.append({

        'Source_language': item['sourceLanguage'],
        'target_language': item['targetLanguage'],
        'article_count': item['count'],
        'translators': item['translators']
    })

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(data_rows)

df.to_csv('data.csv', index=False)

 
