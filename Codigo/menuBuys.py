from auxCompras import read, write, readCate, writeCate, writeInventario, readInventario, writeCateItem, readCateItem, addCompras, editarElem, remove, searchElem, visualizar, editarCate, closeElem, atualiza, writeNomeListas, getListas, readNomeListas, mudarLista, mudarNomeLista, criarList

def printMenu():
    print("1. Adicionar um elemento à lista ")
    print("2. Editar um elemento da lista ")
    print("3. Marcar um elemento como fechado ")
    print("4. Remover um elemento da lista ")
    print("5. Visualizar a lista  ")
    print("6. Procurar elementos por nome")
    print("7. Ordenação da lista ")
    print("8. Adicionar uma categoria ")
    print("9. Editar uma categoria existente ")
    print("10. Consultar categorias ")
    print("11. Consultar todos os items associados a uma categoria")
    print("12. Mudar lista atual")
    print("13. Mudar nome da lista atual")
    print("14. Criar nova lista")
    print("15. Sair ")

def main():
    lista = read() #list de conmpras
    inventario = readInventario() # inventario
    listaCate = readCate() # categorias
    cateItem = readCateItem() #categorias item
    listaCompras = readNomeListas()
    allLists = getListas(lista, listaCompras)
    i=0
    for x in allLists:
        print(i," - ",x.nome, x.num, x.lista)
        i = i + 1
    lista = allLists[0]
    print(lista.nome, lista.num, lista.lista)
    print(len(allLists))

    printMenu()
    op=int(input("O que deseja selecionar:"))

    while op !=15:
        if op == 1:
            print("1. Adicionar um elemento à lista ")
            lista = addCompras(lista, inventario)
            atualiza(allLists, lista)
            print(lista)

        if op == 2:
            print("2. Editar um elemento da lista")
            lista = editarElem(lista)
            atualiza(allLists, lista)

        if op == 3:
            print("3. Marcar um elemento como fechado")
            lista = closeElem(lista)
            atualiza(allLists, lista)

        if op == 4:
            print("4. Remover um elemento da lista  ")
            lista = remove(lista)
            print("before",lista.nome, lista.num, lista.lista)
            atualiza(allLists, lista)
            print("after",lista.nome, lista.num, lista.lista)


        if op == 5:
            print("5. Visualizar a lista ")
            visualizar(lista,"main")

        if op == 6:
            print("6. Procurar elementos por nome")
            searchElem(lista)

        if op == 7:
            print("7. Ordenação da lista ")

        if op == 8:
            print("8. Adicionar uma categoria ")

        if op == 9:
            print("9. Editar uma categoria existente ")
            listaCate = editarCate(listaCate)
            atualiza(allLists, lista)

        if op == 10:
            print("10. Consultar categorias ")

        if op == 11:
            print("11. Consultar todos os items associados a uma categoria ")

        if op == 12:
            print("9. Mudar lista atual")
            lista = mudarLista(allLists)
            atualiza(allLists, lista)

        if op == 13:
            print("10. Mudar nome lista atual")
            lista = mudarNomeLista(lista)
            atualiza(allLists, lista)

        if op == 14:
            print("11. Criar nova lista")
            allLists = criarList(allLists)
            atualiza(allLists, lista)

        if op == 15:
            print("12. Sair")

        print("Carregue no 0 para retroceder")
        input()
        printMenu()
        op = int(input("O que deseja selecionar:"))

    writeCateItem(cateItem)
    writeInventario(inventario)
    writeCate(listaCate)
    write(allLists)
    writeNomeListas(allLists)
main()
