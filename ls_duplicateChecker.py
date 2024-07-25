import pandas as pd
import json

df1=pd.read_csv('/path/to/dataset/file.csv')
with open('/path/to/label_studio/backup/port1/Project_1-at-2024-07-25-120008.json', 'r') as file:
    json_data = json.load(file)
    data_list = [entry['data'] for entry in json_data]
df2 = pd.DataFrame(data_list)

print(f'Number of Ori Data in the DataFrame 1: {df1.shape[0]}')
print(f'Number of Annotated Data in the DataFrame 2: {df2.shape[0]}')
# Output
# Number of Ori Data in the DataFrame 1: 1500
# Number of Annotated Data in the DataFrame 2: 500

common_values = df1['id'].isin(df2['id'])
count_common_values = common_values.sum()
print('Duplicate id =', count_common_values) # Duplicate id should have the same number as annotated data
# Output
# Duplicate id = 500

df_cleaned = df1[~common_values]
print(f'Cleaned rows: {df_cleaned.shape[0]}')
removed_rows = df1.shape[0] - df_cleaned.shape[0]
print(f'Removed rows: {removed_rows}')
# Output
# Cleaned rows: 1000
# Removed rows: 500

cleaned_csv_path = '/path/to/label_studio/cleaned_data.csv' # Check path and name
df_cleaned.to_csv(cleaned_csv_path, index=False)

print(f'The cleaned CSV file has been saved to {cleaned_csv_path}')
# Output
# The cleaned CSV file has been saved to /path/to/label_studio/cleaned_data.csv
