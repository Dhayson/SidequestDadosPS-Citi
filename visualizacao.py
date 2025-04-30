import pandas
import matplotlib.pyplot as plt

def visualizar_aprovacao(base: pandas.DataFrame):
    valores = base["aprovado"].value_counts()
    valor_total = valores.sum()
    valor_nao = valores["Não"]
    valor_sim = valores["Sim"]
    # Converter em portentagem
    frac_nao = valor_nao / valor_total
    frac_sim = valor_sim / valor_total
    # Gerar gráfico de pizza
    fig, ax = plt.subplots(figsize=(6, 6))
    wedges, texts, autotexts = ax.pie(
        [valor_nao, valor_sim],
        labels=[f"Não {valor_nao}", f"Sim {valor_sim}"],
        autopct=lambda pct: f"{pct:.1f}%" if pct%1 else f"{pct:.0f}%",
        textprops=dict(color="white", weight="bold", fontsize=12),
        startangle=90
    )
    plt.title('Distribuição dos Valores')
    plt.axis('equal')  # Deixa o gráfico redondo
    
    # Estilo das labels (fora das fatias)
    for text in texts:
        text.set_color('black')
        text.set_fontsize(14)
        text.set_weight('normal')

    # Título e layout
    ax.set_title(
        'Aprovados e Desaprovados',
        fontsize = 16,
        )
    ax.axis('equal')
    
    plt.savefig("./visualização/Distribuição_de_Aprovação.png")
    

def visualizar_distribuicao_sexo(base: pandas.DataFrame):
    valores = base["sexo"].value_counts()
    valor_total = valores.sum()
    valor_masculino = valores["Masculino"]
    valor_feminino = valores["Feminino"]
    # Converter em portentagem
    frac_masculino = valor_masculino / valor_total
    frac_feminino = valor_feminino / valor_total
    # Gerar gráfico de pizza
    fig, ax = plt.subplots(figsize=(8, 6))
    wedges, texts, autotexts = ax.pie(
        [valor_masculino, valor_feminino],
        labels=[f"Masculino {valor_masculino}", f"Feminino {valor_feminino}"],
        autopct=lambda pct: f"{pct:.1f}%" if pct%1 else f"{pct:.0f}%",
        textprops=dict(color="white", weight="bold", fontsize=12),
        startangle=90
    )
    plt.title('Distribuição dos Valores')
    plt.axis('equal')  # Deixa o gráfico redondo
    
    # Estilo das labels (fora das fatias)
    for text in texts:
        text.set_color('black')
        text.set_fontsize(14)
        text.set_weight('normal')

    # Título e layout
    ax.set_title(
        'Distribuição por Sexo',
        fontsize = 16,
        )
    ax.axis('equal')
    
    plt.savefig("./visualização/Distribuição_por_Sexo.png")

def visualizar_melhores_medias(base: pandas.DataFrame):
    base_medias = base.sort_values(by=["media"], ascending=False).head(5)
    
    # Converter para float
    base_medias['media'] = base_medias['media'].astype(str).str.replace(',', '.').astype(float)
    
    # Gráfico de barras
    plt.figure(figsize=(8, 5))
    plt.bar(base_medias['nome'], base_medias['media'])
    plt.ylabel('Média')
    plt.title('Ranking das Melhores Médias')
    plt.ylim(0, 10)
    plt.xticks(rotation=45, ha='right')

    # Mostrar os valores nas barras
    for i, valor in enumerate(base_medias['media']):
        plt.text(i, valor + 0.1, f'{valor:.2f}', ha='center', fontsize=10)

    plt.tight_layout()
    plt.savefig("./visualização/Ranking_das_Melhores_Médias.png")
    

def visualizar_rank_frequencia(base: pandas.DataFrame):
    base_freq = base.sort_values(by=["frequencia"], ascending=False).head(5)
    
    # Converter para float
    base_freq['frequencia'] = base_freq['frequencia'].astype(str).str.replace(',', '.').astype(float)
    
    # Gráfico de barras
    plt.figure(figsize=(8, 5))
    plt.bar(base_freq['nome'], base_freq['frequencia'])
    plt.ylabel('Média')
    plt.title('Ranking de Frequência')
    plt.ylim(0, 110)
    plt.xticks(rotation=45, ha='right')

    # Mostrar os valores nas barras
    for i, valor in enumerate(base_freq['frequencia']):
        plt.text(i, valor + 1, f'{valor:.2f}', ha='center', fontsize=10)

    plt.tight_layout()
    plt.savefig("./visualização/Ranking_de_Frequência.png")
    

def main():
    base = pandas.read_csv("./base_de_dados/Base_padronizada.csv")
    visualizar_aprovacao(base)
    visualizar_distribuicao_sexo(base)
    visualizar_melhores_medias(base)
    visualizar_rank_frequencia(base)

if __name__ == "__main__":
    main()