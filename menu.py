from crud import CRUDAluno, CRUDDisciplina

def menu():
    crud_aluno = CRUDAluno()
    crud_disciplina = CRUDDisciplina()

    while True:
        print("\nMenu Principal:")
        print("1. CRUD Alunos")
        print("2. CRUD Disciplinas")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            menu_alunos(crud_aluno)
        elif opcao == '2':
            menu_disciplinas(crud_disciplina)
        elif opcao == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

def menu_alunos(crud_aluno):
    while True:
        print("\nMenu Alunos:")
        print("1. Adicionar Aluno")
        print("2. Listar Alunos")
        print("3. Atualizar Aluno")
        print("4. Deletar Aluno")
        print("5. Voltar ao Menu Principal")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            id = input("Digite o ID do aluno: ")
            nome = input("Digite o nome do aluno: ")
            crud_aluno.adicionar_aluno(id, nome)
        elif opcao == '2':
            crud_aluno.listar_alunos()
        elif opcao == '3':
            id = input("Digite o ID do aluno a ser atualizado: ")
            novo_nome = input("Digite o novo nome: ")
            crud_aluno.atualizar_aluno(id, novo_nome)
        elif opcao == '4':
            id = input("Digite o ID do aluno a ser deletado: ")
            crud_aluno.deletar_aluno(id)
        elif opcao == '5':
            break
        else:
            print("Opção inválida!")

def menu_disciplinas(crud_disciplina):
    while True:
        print("\nMenu Disciplinas:")
        print("1. Adicionar Disciplina")
        print("2. Listar Disciplinas")
        print("3. Atualizar Disciplina")
        print("4. Deletar Disciplina")
        print("5. Voltar ao Menu Principal")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            id = input("Digite o ID da disciplina: ")
            nome = input("Digite o nome da disciplina: ")
            crud_disciplina.adicionar_disciplina(id, nome)
        elif opcao == '2':
            crud_disciplina.listar_disciplinas()
        elif opcao == '3':
            id = input("Digite o ID da disciplina a ser atualizada: ")
            novo_nome = input("Digite o novo nome: ")
            crud_disciplina.atualizar_disciplina(id, novo_nome)
        elif opcao == '4':
            id = input("Digite o ID da disciplina a ser deletada: ")
            crud_disciplina.deletar_disciplina(id)
        elif opcao == '5':
            break
        else:
            print("Opção inválida!")
