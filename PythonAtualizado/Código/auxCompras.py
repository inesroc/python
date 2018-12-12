import csv
import datetime

def pathFile():
def read():
    lista = []
    file = open('compras.txt', 'r')
    reader = csv.reader(file, delimiter =';', quotechar ='"')

    for row in reader:
        if row:
            lista += [row]
    file.close()
    return (lista)

def write(lista):

    file = open("Compras.txt", "w")
    writer = csv.writer(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)

    for row in lista:
        writer.writerow(row)
    file.close()

def readCate():
    listaCate = []
    file = open('categorias.txt', 'r')
    reader = csv.reader(file, delimiter =';', quotechar ='"')

    for row in reader:
        if row:
            listaCate += [row]
    file.close()
    return (listaCate)

def writeCate(listaCate):

    file = open("categorias.txt", "w")
    writer = csv.writer(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)

    for row in listaCate:
        writer.writerow(row)
    file.close()

def readCompra():
    listaCompra = []
    file = open('inventario.txt', 'r')
    reader = csv.reader(file, delimiter =';', quotechar ='"')

    for row in reader:
        if row:
            listaCompra += [row]
    file.close()
    return (listaCompra)

def writeCompra(listaCompra):

    file = open("inventario.txt", "w")
    writer = csv.writer(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)

    for row in listaCompra:
        writer.writerow(row)
    file.close()


def addCompras(lista): # nao funciona a 100% falta preço
    
    temporaria = []
    nome = input('Lista de compras: ')
    temporaria += [nome]
    quantidade = input("Quantidade:") #preco = ("->Preco: ")
    temporaria += [quantidade] #+ [preco]
    actual = datetime.datetime.now()
    temporaria += [actual]
    temporaria += [""]
    temporaria += ["Aberta"]
    observacoes = input('Deseja colocar observações? \n 1)Sim \n 2)Nao')
    if observacoes == '1':
        obs = input('Escreva as observacões: ')
    else:
        obs = ' '
    temporaria += [obs]

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
