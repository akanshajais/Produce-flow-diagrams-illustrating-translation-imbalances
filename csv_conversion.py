import requests
import csv
import pandas as pd

# wikipedia link to extract data
json_url = 'https://en.wikipedia.org/w/api.php?action=query&list=contenttranslationstats&format=json'

# Get the data
response = requests.get(json_url)
data = response.json()

#output csv file
output_file = 'data_source.csv'
csv_header = data['query']['contenttranslationstats']['pages']

# list to store data
csv_data = []

# Parse JSON data and append rows to data_rows list
for item in csv_header:
    csv_data.append({

        'Source_language': item['sourceLanguage'],
        'target_language': item['targetLanguage'],
        'article_count': item['count'],
        'translators': item['translators']
    })

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(csv_data)

df.to_csv('source_data.csv', index=False)

 
