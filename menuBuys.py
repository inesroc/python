from auxCompras import read, write, readCate, writeCate, writeCompra, readCompra, addCompras, editarElem, remove, searchElem, visualizar, editarCate, closeElem

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
    print("12. Sair ")

def main():
    lista = read()
    listaCompra = readCompra()
    listaCate = readCate()
    printMenu()
    op=int(input("O que deseja selecionar:"))

    while op !=12:
        if op == 1:
            print("1. Adicionar um elemento à lista ")
            lista = addCompras(lista)

        if op == 2:
            print("2. Editar um elemento da lista")
            lista = editarElem(lista)

        if op == 3:
            print("3. Marcar um elemento como fechado")
            lista = closeElem(lista)

        if op == 4:
            print("4. Remover um elemento da lista  ")
            lista = remove(lista)

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

        if op == 10:
            print("10. Consultar categorias ")

        if op == 11:
            print("11. Consultar todos os items associados a uma categoria ")

        if op == 12:
            print("12. Sair")

        print("Carregue no 0 para retroceder")
        input()
        printMenu()
        op = int(input("O que deseja selecionar:"))
    writeCompra(listaCompra)
    writeCate(listaCate)
    write(lista)
main()
