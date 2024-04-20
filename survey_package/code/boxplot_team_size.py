import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dados = pd.read_csv('survey.csv')
plt.figure(figsize=(8, 6))
#plt.title("Developers' Team Size")
plt.ylabel('Number of Developers')
plt.grid(True)

mdn1 = np.median(dados['howManyDevs'])
m1 = dados['howManyDevs'].mean(axis=0)
st1 = dados['howManyDevs'].std(axis=0)

fig, ax = plt.subplots()
bp = ax.boxplot(dados['howManyDevs'])
plt.tick_params(
    axis='x',
    which='both',
    bottom=False,
    top=False,
    labelbottom=False)

for i, line in enumerate(bp['medians']):
    x, y = line.get_xydata()[1]
    text = ' Mdn={:.2f}\n M={:.2f}\n SD={:.2f}'.format(mdn1, m1, st1)
    ax.annotate(text, xy=(x, y))

plt.savefig('boxplot_team_size.png')
