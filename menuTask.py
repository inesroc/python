from auxTarefas import readFunc, writeFunc, consultFunc, removeFunc, addTarefa, closeTarefa, estadoTarefa, editTarefa, searchTarefa, sortTarefa

def printMenu():
    print("1. Adicionar uma tarefa ")
    print("2. Editar uma tarefa ")
    print("3. Consultar tarefas ")
    print("4. Filtrar tarefas por estado ")
    print("5. Marcar uma tarefa como fechada ")
    print("6. Remover uma tarefa ")
    print("7. Procurar tarefas por nome ")
    print("8. Ordenação da lista de tarefas ")
    print("9. Sair ")

def main():
    list = readFunc()
    printMenu()
    op= int(input("O que deseja selecionar:"))

    while op != 9:
        if op == 1:
            print("1. Adicionar uma tarefa ")
            list = addTarefa(list)

        if op == 2:
            print("2. Editar uma tarefa ")
            editTarefa(list)

        if op == 3:
            print("3. Consultar tarefas ")
            consultFunc(list,"main")

        if op == 4:
            print("4. Filtrar tarefas por estado ")
            estadoTarefa(list)

        if op == 5:
            print("5. Marcar uma tarefa como fechada ")
            closeTarefa(list)

        if op == 6:
            print("6. Remover uma tarefa ")
            list = removeFunc(list)

        if op == 7:
            print("7. Procurar tarefas por nome ")
            searchTarefa(list)

        if op == 8:
            print("8. Ordenação da lista de tarefas  ")
            sortTarefa(list)

        if op == 9:
            print("9. Sair ")

        print("Carregue no 0 para retroceder")
        input()
        printMenu()
        op = int(input("O que deseja selecionar:"))

    writeFunc(list)
main()
