import csv
import datetime
import os

def openTxt(nameFile):
    #print("diretorio atual: ",os.path.abspath(file))
    #print("diretorio sem o ultimo elemento: ",os.path.dirname(os.path.abspath(file)))
    dir = os.path.dirname(os.path.abspath(__file__))   # tira o ultimo elemento que é o nome do programa atual
    #print("dir 1: ",dir)
    dir = os.path.dirname(dir) # tira o ultimo elemento que é o nome da pasta dos códigos
    #print("dir 2: ",dir)

    dir = dir +r"\dados"+nameFile # adicionamos a pasta e o nome do ficheiro que queremos abrir (tem de ter o r atrás porque o python interpreta \f como um caracter esepcial)
    #print("novo diretorio: ",dir)
    return dir

def read():
    lista = []
    dir = openTxt(r"\compras.txt")
    file = open(os.path.join(dir), "r")
    reader = csv.reader(file, delimiter =';', quotechar ='"')

    for row in reader:
        if row:
            lista += [row]
    file.close()
    return (lista)

def write(lista):
    dir = openTxt(r"\compras.txt")
    file = open(os.path.join(dir), "w")
    writer = csv.writer(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)

    for row in lista:
        writer.writerow(row)
    file.close()

def readCate():
    listaCate = []
    dir = openTxt(r"\categorias.txt")
    file = open(os.path.join(dir), "r")
    reader = csv.reader(file, delimiter =';', quotechar ='"')

    for row in reader:
        if row:
            listaCate += [row]
    file.close()
    return (listaCate)

def writeCate(listaCate):
    dir = openTxt(r"\categorias.txt")
    file = open(os.path.join(dir), "w")
    writer = csv.writer(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)

    for row in listaCate:
        writer.writerow(row)
    file.close()

def readInventario():
    inventario = []
    dir = openTxt(r"\inventario.txt")
    file = open(os.path.join(dir), "r")
    reader = csv.reader(file, delimiter =';', quotechar ='"')

    for row in reader:
        if row:
            inventario += [row]
    file.close()
    return (inventario)

def writeInventario(inventario):
    dir = openTxt(r"\inventario.txt")
    file = open(os.path.join(dir), "w")
    writer = csv.writer(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)

    for row in inventario:
        writer.writerow(row)
    file.close()


def readCateItem():
    cateItem = []
    dir = openTxt(r"\cateItem.txt")
    file = open(os.path.join(dir), "r")
    reader = csv.reader(file, delimiter =';', quotechar ='"')

    for row in reader:
        if row:
            cateItem += [row]
    file.close()
    return (cateItem)

def writeCateItem(lista):
    dir = openTxt(r"\cateItem.txt")
    file = open(os.path.join(dir), "w")
    writer = csv.writer(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)

    for row in lista:
        writer.writerow(row)
    file.close()

def addCompras(lista, inventario):
    sel = 1
    print("Produto          | Preço Por unicade      | Quantidade existente ")
    for elem in inventario:
        print(sel, ')',elem[0],    elem[2],        elem[1])
        sel += 1
    sl = (int(input("O que deseja comprar:")))
    sl -= 1
    temporaria = []
    temporaria += [inventario[sl][0]] + [inventario[sl][1]]
    date = datetime.datetime.now()
    print(date)
    temporaria+= [date]
    temporaria += [inventario[sl][2]] + [inventario[sl][3]] + [inventario[sl][4]]
  #temporaria[2] = date
    #print(temporaria)
    lista += [temporaria]

    return lista

def editarElem (lista):
    seletor = 1
    
    for row in lista:
        print(seletor, ')', row[0])
        seletor += 1
    seletor = int(input('Selecione o que pretende editar: ')) -1
    
    if lista[seletor][3] == 'Fechada':
        resp = input('O elemento esta pago. tem a certeza que quer modica lo: \n 1) Sim, \n 2) Nao')
        if resp == '2':
            return
    print('1. Nome ')
    print('2. Observaçoes')
    opcao = int(input('O que pretende modificar?' ))
    if opcao == 1:
        nome = input('Novo nome: ')
        lista[seletor][0] = nome
    elif opcao == 2:
        observacoes = input('Nova observação: ')
        lista[seletor][4] = observacoes
    return(lista)

def remove(lista):
    
    cont = 1
    for row in lista:
        print(cont,')',row[0])
        cont += 1
    opcao = int(input('Selecione o elemento que pretende retirar.'))
    opcao -= 1
    lista.remove(lista[opcao])
    
    return lista

def searchElem(lista):
    print("Digite:")

    x = input()

    sel = 1

    temp = []

    for i in range(0, len(lista)):
        d = lista[i][0].find(x)
        if d != -1:
            print(sel, ")", lista[i][0])
            temp = temp + [i]
            sel = sel + 1

    if sel != 1:
        print("Que elemento deseja selecionar?")
        op = int(input()) -1
        print(lista[temp[op]][0])
        print("Data de Criação:", lista[temp[op]][1])
        if lista[temp[op]][3] == "Fechada":
            print("Estado:", lista[temp[op]][3], "-> Data de concretização", lista[temp[op]][2])
        else:
            print("Estado:", lista[temp[op]][3])
        print("Observações:", lista[temp[op]][4])
        print("------------------------------------------------------")

def visualizar(lista,funcao):
    # funcao pode ser main ou sort

    total = 0

    for row in lista:
        if (row[4] == "Fechada" and funcao == "sort") or funcao == "main":
            print(row[0])
            print("Quantidade:",row[1]," -> Preço:",row[3])
            print("Data de Criação:",row[2])
            if row[4] == "Fechada":
                print("Estado:", row[4], "-> Data de concretização", row[2])
            else:
                print("Estado:", row[4])
            print("Observações:", row[5])
            print("------------------------------------------------------")
            total = total + float(row[1]) + float(row[3])
    print("Total da compra:", total)


def editarCate(lista):
    seletor = 1

    for row in lista:
        print(seletor, ')', row[0])
        seletor += 1
    seletor = int(input('Selecione a categoria que pretende editar: ')) - 1

    if lista[seletor][3] == 'Fechada':
        resp = input('O elemento esta pago. tem a certeza que quer modica lo: \n 1) Sim, \n 2) Nao')
        if resp == '2':
            return
    print('1. Nome ')
    print('2. Categoria Sup.')
    print('3. Observaçoes')
    opcao = int(input('O que pretende modificar?'))
    if opcao == 1:
        nome = input('Novo nome: ')
        lista[seletor][0] = nome
    elif opcao == 2:
        observacoes = input('Nova observação: ')
        lista[seletor][4] = observacoes
    return (lista)

def closeElem(lista):
    temp = []
    sel = 1

    for i in range(0,len(lista)):
        if lista[i][3] == "Aberta":
            print(sel,")",lista[i][0])
            temp = temp + [i]
            sel = sel + 1
    if sel == 1:
        print("Todos os elementos estao pagos!")
    else:
        print("Escolhe o elemento que quer pagar:")
        sel = int(input()) - 1
        lista[temp[sel]][2] = datetime.datetime.now()
        lista[temp[sel]][3] = "Fechada"

    return(lista)
