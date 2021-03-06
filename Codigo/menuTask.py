from auxTarefas import readFunc, writeFunc, consultFunc, removeFunc, addTarefa, closeTarefa, estadoTarefa, editTarefa, searchTarefa, sortTarefa, readNomeListas, getListas, atualiza, mudarNomeLista, mudarLista, criarList, writeNomeListas
import os

def printMenu():
    print("1. Adicionar uma tarefa ")
    print("2. Editar uma tarefa ")
    print("3. Consultar tarefas ")
    print("4. Filtrar tarefas por estado ")
    print("5. Marcar uma tarefa como fechada ")
    print("6. Remover uma tarefa ")
    print("7. Procurar tarefas por nome ")
    print("8. Ordenação da lista de tarefas ")
    print("9. Mudar lista atual")
    print("10 Mudar nome da lista atual")
    print("11. Criar nova lista")
    print("12. Sair ")

def main():
    tarefas = readFunc()
    nomesListas = readNomeListas()
    allLists = getListas(tarefas, nomesListas)
    i = 0
    for x in allLists:
        print(i," - ",x.nome, x.num, x.lista)
        i = i + 1
    lista = allLists[0]
    print(lista.nome, lista.num, lista.lista)
    print(len(allLists))
    printMenu()
    op= int(input("O que deseja selecionar:"))

    while op != 12:
        if op == 1:
            print("1. Adicionar uma tarefa ")
            print(lista.nome, lista.num, lista.lista)
            lista = addTarefa(lista)
            print(lista.nome, lista.num, lista.lista)
            #atualiza(allLists, lista)

        if op == 2:
            print("2. Editar uma tarefa ")
            lista = editTarefa(lista)
            atualiza(allLists, lista)

        if op == 3:
            print("3. Consultar tarefas ")
            consultFunc(lista,"main")

        if op == 4:
            print("4. Filtrar tarefas por estado ")
            estadoTarefa(lista)

        if op == 5:
           print("5. Marcar uma tarefa como fechada ")
           lista = closeTarefa(lista)
           atualiza(allLists, lista)

        if op == 6:
            print("6. Remover uma tarefa ")
            lista = removeFunc(lista)
            atualiza(allLists, lista)

        if op == 7:
            print("7. Procurar tarefas por nome ")
            searchTarefa(lista)

        if op == 8:
            print("8. Ordenação da lista de tarefas  ")
            sortTarefa(lista)

        if op == 9:
            print("9. Mudar lista atual")
            lista = mudarLista(allLists)
            atualiza(allLists, lista)

        if op == 10:
            print("10. Mudar nome lista atual")
            lista = mudarNomeLista(lista)
            atualiza(allLists, lista)

        if op == 11:
            print("11. Criar nova lista")
            allLists = criarList(allLists)


        if op == 12:
            print("12. Sair ")

        print("Carregue no 0 para retroceder")
        input()
        printMenu()
        op = int(input("O que deseja selecionar:"))

    writeFunc(allLists)
    writeNomeListas(allLists)
main()
