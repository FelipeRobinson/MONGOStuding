import matplotlib.pyplot as plt
from pymongo import MongoClient

def gerar_relatorio_vendas():
    # Conexão ao banco de dados
    cliente = MongoClient("mongodb://localhost:27017/")
    db = cliente["lanchonete"]
    vendas = db["vendas"]

    # Pipeline para gerar o relatório
    pipeline = [
        {"$lookup": {
            "from": "produtos",
            "localField": "produto_nome",
            "foreignField": "nome",
            "as": "produto_info"}},
        {"$unwind": "$produto_info"},
        {"$group": {
            "_id": "$produto_info.categoria",
            "total_vendido": {"$sum": {"$multiply": ["$quantidade", "$produto_info.preco"]}}}},
        {"$sort": {"total_vendido": -1}}
    ]

    relatorio = list(vendas.aggregate(pipeline))

    # Preparando os dados para o gráfico
    categorias = [item['_id'] for item in relatorio]
    total_vendido = [item['total_vendido'] for item in relatorio]

    # Criando o gráfico
    plt.figure(figsize=(10, 6))
    plt.bar(categorias, total_vendido, color='red')
    plt.xlabel('Categorias')
    plt.ylabel('Total Vendido (R$)')
    plt.title('Total de Vendas por Categoria')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Exibindo o gráfico
    plt.show()

if __name__ == "__main__":
    gerar_relatorio_vendas()