import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('WHO-COVID-19-global-table-data.csv')

# Check the column names to ensure they match
print("Columns in the dataset:", data.columns)

# Corrected column names based on the CSV file
plt.figure(figsize=(10, 5))
plt.xlabel('Name')  # Country/Region names
plt.ylabel('CasesCumulativeTotal')  # Total cumulative cases

# Ensure column names match exactly
if 'Name' in data.columns and 'CasesCumulativeTotal' in data.columns:
    plt.plot(data['Name'], data['CasesCumulativeTotal'], 'y.-', label='Cumulative Cases')
    plt.xticks(data['Name'][::10], rotation=90)  # Rotate for better visibility
    plt.legend()
    plt.show()
else:
    print("Error: Column names do not match. Please check the dataset.")