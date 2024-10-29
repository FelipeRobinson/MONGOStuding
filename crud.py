class Aluno:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

class Disciplina:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

class CRUDAluno:
    def __init__(self):
        self.alunos = []

    def adicionar_aluno(self, id, nome):
        self.alunos.append(Aluno(id, nome))
        print("Aluno adicionado com sucesso!")

    def listar_alunos(self):
        print("\nLista de Alunos:")
        for aluno in self.alunos:
            print(f"ID: {aluno.id}, Nome: {aluno.nome}")

    def atualizar_aluno(self, id, novo_nome):
        for aluno in self.alunos:
            if aluno.id == id:
                aluno.nome = novo_nome
                print("Aluno atualizado com sucesso!")
                return
        print("Aluno não encontrado!")

    def deletar_aluno(self, id):
        self.alunos = [aluno for aluno in self.alunos if aluno.id != id]
        print("Aluno deletado com sucesso!")

class CRUDDisciplina:
    def __init__(self):
        self.disciplinas = []

    def adicionar_disciplina(self, id, nome):
        self.disciplinas.append(Disciplina(id, nome))
        print("Disciplina adicionada com sucesso!")

    def listar_disciplinas(self):
        print("\nLista de Disciplinas:")
        for disciplina in self.disciplinas:
            print(f"ID: {disciplina.id}, Nome: {disciplina.nome}")

    def atualizar_disciplina(self, id, novo_nome):
        for disciplina in self.disciplinas:
            if disciplina.id == id:
                disciplina.nome = novo_nome
                print("Disciplina atualizada com sucesso!")
                return
        print("Disciplina não encontrada!")

    def deletar_disciplina(self, id):
        self.disciplinas = [disciplina for disciplina in self.disciplinas if disciplina.id != id]
        print("Disciplina deletada com sucesso!")
