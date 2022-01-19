import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('WHO-COVID-19-global-table-data.csv')
data.shape
data.head(10)
data.columns
data.info()
data.describe()
data.dtypes
plt.figure(figsize=(20,10))
plt.xlabel('Name of the country')
plt.ylabel('Total Cumulative Deaths per 100000 Population')
plt.plot(data.Name, data.DeathsCumulativeTotalPer100000Population, 'y.-', label='cumulative')
plt.xticks(data.Name[::50])
plt.legend()
plt.show()