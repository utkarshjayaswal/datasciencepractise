import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('covid_19_india.csv')
plt.figure(figsize=(10, 5))
plt.xlabel('State/UnionTerritory')
plt.ylabel('Cured')
plt.plot(data.StateUnionTerritory, data.Cured, 'y.-', label='cumulative')
plt.xticks(data.StateUnionTerritory[::150])
plt.legend()
plt.show()
