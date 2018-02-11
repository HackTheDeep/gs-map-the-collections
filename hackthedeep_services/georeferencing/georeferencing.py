import pandas as pd

print("Hello World")

file = 'data/DirtyData.xlsx'

df = pd.read_excel(file)

data = df[['Tracking Number', 'Continent', 'Country', 'Department / Province / State', 'County', 'City/Town/Hamlet', 'Specific Locale', 'decimal latitude', 'decimal latitude']]
#data.set_index('Tracking Number')

data.to_csv('data/testDirtyData.csv', index=False)