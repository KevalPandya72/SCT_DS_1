import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("API_SP.POP.TOTL_DS2_en_csv_v2_76034.csv", skiprows=4)

india_data = df[df['Country Name'] == 'India']

year_columns = [col for col in india_data.columns if col.isdigit()]

india_population = india_data[year_columns].T
india_population.columns = ['Population']
india_population.index.name = 'Year'
india_population.reset_index(inplace=True)
india_population['Year'] = india_population['Year'].astype(int)

india_population['Population'] = india_population['Population'] / 1e9

plt.figure(figsize=(16, 6))
plt.bar(india_population['Year'], india_population['Population'], color='skyblue')
plt.title("India's Population by Year (1960–2022)", fontsize=16)
plt.xlabel("Year")
plt.ylabel("Population (in Billions)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
