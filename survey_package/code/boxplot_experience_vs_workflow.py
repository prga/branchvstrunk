import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


dados = pd.read_csv('survey.csv')


dados_branch = dados[dados['branchORtrunk'] == 'branch']['YearsProgramming']
dados_trunk = dados[dados['branchORtrunk'] == 'trunk']['YearsProgramming']


median1 = np.median(dados_branch.values)
median2 = np.median(dados_trunk.values)
mdn1=[median1, median2]
m_branch = dados_branch.values.mean(axis=0)
m_trunk = dados_trunk.values.mean(axis=0)
m1 = [m_branch, m_trunk]
st_branch = dados_branch.values.std(axis=0)
st_trunk = dados_trunk.values.std(axis=0)
st1 = [st_branch, st_trunk]

fig, ax = plt.subplots()
bp = ax.boxplot([dados_branch, dados_trunk], labels=['Branch-based', 'Trunk-based'])
#plt.title('Years of Experience by Workflow')
plt.xlabel('Workflow')
plt.ylabel('Years of Experience')
plt.grid(True)

for i, line in enumerate(bp['medians']):
    x, y = line.get_xydata()[1]
    text = ' Mdn={:.2f}\n M={:.2f}\n SD={:.2f}'.format(mdn1[i], m1[i], st1[i])
    ax.annotate(text, xy=(x, y))

plt.savefig('boxplot_experience_vs_workflow.png')
