import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('survey.csv')
plt.figure(figsize=(8, 6))
plt.ylabel('Frequency', fontsize=14) 
plt.xlabel('Years of Experience', fontsize=14) 
plt.grid(True)

plt.hist(dados['YearsProgramming'], bins=20, color='skyblue', edgecolor='black')

plt.tick_params(axis='x', labelsize=12)
plt.tick_params(axis='y', labelsize=12)

plt.savefig('frequency_years_experience.png')
