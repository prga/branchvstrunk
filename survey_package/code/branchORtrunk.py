import csv
import matplotlib.pyplot as plt

def ler_csv(nome_arquivo):
    dados = []
    with open(nome_arquivo, 'r', newline='') as arquivo_csv:
        leitor = csv.reader(arquivo_csv)
        for linha in leitor:
            dados.append(linha)
    return dados

def plotar_grafico_barras(respostas, labels):
    contagem_a = respostas.count('branch')
    contagem_b = respostas.count('trunk')
    contagem_c = respostas.count('unidentified')


    valores = [contagem_a, contagem_b, contagem_c]
    x = range(len(valores))
    colors=['blue','red','orange']
    largura_barra = 0.35  # Largura das barras
    
    fig, ax = plt.subplots()  # Cria uma figura e um conjunto de eixos
    barras = ax.bar(x, valores, largura_barra, label=labels, color=colors)  # Barras para os valores

    for i, value in enumerate(valores):
        plt.annotate(str(abs(value)), (i, max(0, value)), ha='center', va='bottom')


    ax.set_ylabel('Quantity')  # Nome do eixo y
    #ax.set_title('Branch-based vs. Trunk-based')  # Título do gráfico
    ax.set_xticks(x)  # Posições do eixo x
    ax.set_xticklabels(labels)  # Rótulos do eixo 
    ax.grid(True)
    ax.legend()  # Adiciona a legenda


    plt.savefig('branch_vs_trunk.png')  # Mostra o gráfico

sheet = 'survey.csv'
answers = ler_csv(sheet)

branchORtrunk = []
for linha in answers:
    branchORtrunk.append(linha[4])

# Exemplo de uso:
respostas = branchORtrunk
labels = ['Branch-based', 'Trunk-based', 'Unidentified']
plotar_grafico_barras(respostas, labels)
