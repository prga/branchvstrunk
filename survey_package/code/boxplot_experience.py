import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dados = pd.read_csv('survey.csv')
plt.figure(figsize=(8, 6))
#plt.title("Developers' Years of Experience")
plt.ylabel('Years of Experience')
plt.grid(True)

mdn1 = np.median(dados['YearsProgramming'])
m1 = dados['YearsProgramming'].mean(axis=0)
st1 = dados['YearsProgramming'].std(axis=0)

fig, ax = plt.subplots()
bp = ax.boxplot(dados['YearsProgramming'])
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
    
plt.savefig('boxplot_experience.png')
