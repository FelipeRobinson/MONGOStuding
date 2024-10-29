import tkinter as tk
from tkinter import messagebox
from pymongo import MongoClient
from datetime import datetime

class Produto:
    def __init__(self, nome, preco, categoria):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria

    def to_dict(self):
        return {
            "nome": self.nome,
            "preco": self.preco,
            "categoria": self.categoria
        }

class Venda:
    def __init__(self, produto_nome, quantidade, data_venda=None):
        self.produto_nome = produto_nome
        self.quantidade = quantidade
        self.data_venda = data_venda or datetime.now()

    def to_dict(self):
        return {
            "produto_nome": self.produto_nome,
            "quantidade": self.quantidade,
            "data_venda": self.data_venda
        }

class Lanchonete:
    def __init__(self):
        self.cliente = MongoClient("mongodb://localhost:27017/")
        self.db = self.cliente["lanchonete"]
        self.produtos = self.db["produtos"]
        self.vendas = self.db["vendas"]

    def cadastrar_produto(self, produto):
        self.produtos.insert_one(produto.to_dict())

    def listar_produtos(self):
        return list(self.produtos.find())

    def registrar_venda(self, venda):
        produto = self.produtos.find_one({"nome": venda.produto_nome})
        if produto:
            self.vendas.insert_one(venda.to_dict())
            return True
        return False

    def gerar_relatorio_vendas_por_categoria(self):
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
                "total_vendido": {"$sum": {"$multiply": ["$quantidade", "$produto_info.preco"]}},
                "quantidade_vendida": {"$sum": "$quantidade"},
                "produtos": {"$addToSet": "$produto_info.nome"}}},  # Coleta os produtos vendidos
            {"$sort": {"total_vendido": -1}}
        ]
        return list(self.vendas.aggregate(pipeline))

class LanchoneteGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Lanchonete")
        self.lanchonete = Lanchonete()

        # Configurações de cor para a interface
        self.root.configure(bg="#E8F0FE")

        # Seção de Cadastro de Produto
        self.frame_cadastro = tk.Frame(root, bg="#F0F4C3", padx=10, pady=10)
        self.frame_cadastro.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.label_nome = tk.Label(self.frame_cadastro, text="Nome do Produto", bg="#F0F4C3")
        self.label_nome.grid(row=0, column=0)
        self.entry_nome = tk.Entry(self.frame_cadastro)
        self.entry_nome.grid(row=0, column=1)

        self.label_preco = tk.Label(self.frame_cadastro, text="Preço", bg="#F0F4C3")
        self.label_preco.grid(row=1, column=0)
        self.entry_preco = tk.Entry(self.frame_cadastro)
        self.entry_preco.grid(row=1, column=1)

        self.label_categoria = tk.Label(self.frame_cadastro, text="Categoria", bg="#F0F4C3")
        self.label_categoria.grid(row=2, column=0)
        self.entry_categoria = tk.Entry(self.frame_cadastro)
        self.entry_categoria.grid(row=2, column=1)

        self.button_cadastrar = tk.Button(self.frame_cadastro, text="Cadastrar Produto", command=self.cadastrar_produto, bg="#AED581", fg="white")
        self.button_cadastrar.grid(row=3, column=1)

        # Seção de Listagem de Produtos
        self.frame_listagem = tk.Frame(root, bg="#FFECB3", padx=10, pady=10)
        self.frame_listagem.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.button_listar = tk.Button(self.frame_listagem, text="Listar Produtos", command=self.listar_produtos, bg="#FFB74D", fg="white")
        self.button_listar.grid(row=0, column=0)
        self.text_listagem = tk.Text(self.frame_listagem, height=10, width=50, bg="#FFF8E1")
        self.text_listagem.grid(row=1, column=0, columnspan=2)

        # Seção de Registro de Venda
        self.frame_venda = tk.Frame(root, bg="#C5CAE9", padx=10, pady=10)
        self.frame_venda.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.label_produto_venda = tk.Label(self.frame_venda, text="Produto para Venda", bg="#C5CAE9")
        self.label_produto_venda.grid(row=0, column=0)
        self.entry_produto_venda = tk.Entry(self.frame_venda)
        self.entry_produto_venda.grid(row=0, column=1)

        self.label_quantidade = tk.Label(self.frame_venda, text="Quantidade", bg="#C5CAE9")
        self.label_quantidade.grid(row=1, column=0)
        self.entry_quantidade = tk.Entry(self.frame_venda)
        self.entry_quantidade.grid(row=1, column=1)

        self.button_vender = tk.Button(self.frame_venda, text="Registrar Venda", command=self.registrar_venda, bg="#7986CB", fg="white")
        self.button_vender.grid(row=2, column=1)

        # Seção de Relatório
        self.frame_relatorio = tk.Frame(root, bg="#FFCDD2", padx=10, pady=10)
        self.frame_relatorio.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        self.button_relatorio = tk.Button(self.frame_relatorio, text="Relatório por Categoria", command=self.gerar_relatorio, bg="#E57373", fg="white")
        self.button_relatorio.grid(row=0, column=1)
        self.text_relatorio = tk.Text(self.frame_relatorio, height=10, width=50, bg="#FFEBEE")
        self.text_relatorio.grid(row=1, column=0, columnspan=2)

    def cadastrar_produto(self):
        nome = self.entry_nome.get()
        preco = float(self.entry_preco.get())
        categoria = self.entry_categoria.get()
        produto = Produto(nome, preco, categoria)
        self.lanchonete.cadastrar_produto(produto)
        messagebox.showinfo("Sucesso", f"Produto '{nome}' cadastrado com sucesso.")

    def listar_produtos(self):
        produtos = self.lanchonete.listar_produtos()
        self.text_listagem.delete(1.0, tk.END)
        for produto in produtos:
            self.text_listagem.insert(tk.END, f"{produto['nome']} - R${produto['preco']} - {produto['categoria']}\n")

    def registrar_venda(self):
        produto_nome = self.entry_produto_venda.get()
        quantidade = int(self.entry_quantidade.get())
        venda = Venda(produto_nome, quantidade)
        if self.lanchonete.registrar_venda(venda):
            messagebox.showinfo("Sucesso", f"Venda registrada para '{produto_nome}'.")
        else:
            messagebox.showerror("Erro", "Produto não encontrado!")

    def gerar_relatorio(self):
        relatorio = self.lanchonete.gerar_relatorio_vendas_por_categoria()
        self.text_relatorio.delete(1.0, tk.END)
        for categoria in relatorio:
            self.text_relatorio.insert(
                tk.END,
                f"Categoria: {categoria['_id']}\n"
                f"  Total Vendido: R${categoria['total_vendido']}\n"
                f"  Quantidade Vendida: {categoria['quantidade_vendida']}\n"
                f"  Produtos: {', '.join(categoria['produtos'])}\n\n"
            )

# Inicialização da interface
root = tk.Tk()
app = LanchoneteGUI(root)
root.mainloop()