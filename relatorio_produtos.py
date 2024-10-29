import matplotlib.pyplot as plt
from pymongo import MongoClient

def gerar_relatorio_produtos():
    # Conexão ao banco de dados
    cliente = MongoClient("mongodb://localhost:27017/")
    db = cliente["lanchonete"]
    produtos = db["produtos"]

    # Consultando produtos
    produtos_list = list(produtos.find())
    
    # Preparando os dados para o gráfico
    nomes_produtos = [produto['nome'] for produto in produtos_list]
    precos_produtos = [produto['preco'] for produto in produtos_list]

    # Criando o gráfico
    plt.figure(figsize=(10, 6))
    plt.bar(nomes_produtos, precos_produtos, color='lightgreen')
    plt.xlabel('Produtos')
    plt.ylabel('Preço (R$)')
    plt.title('Preço dos Produtos')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Exibindo o gráfico
    plt.show()

if __name__ == "__main__":
    gerar_relatorio_produtos()