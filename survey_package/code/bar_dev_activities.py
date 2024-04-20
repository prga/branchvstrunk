import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('survey.csv')
data = dados['softwareDevActivities']

data_split = data.str.split(';', expand=True)
data_split = data_split.stack()
counts = data_split.str.strip().value_counts()

sorted_counts = counts.sort_values(ascending=True)

num_bars = len(sorted_counts)
fig_width = max(13, num_bars * 0.8)
fig_height = max(6, num_bars * 0.6)

plt.figure(figsize=(fig_width, fig_height))

sorted_counts.plot(kind='barh', width=0.5)  # Use 'barh' for horizontal bars

plt.xlabel('Frequency')
plt.ylabel('Activities')
#plt.title('Frequency of Software Development Activities')
plt.grid(True)

for i, count in enumerate(sorted_counts):
    plt.text(count, i, " " + str(count), ha='left', va='center', fontsize=10)

plt.savefig('bar_dev_activities.png')