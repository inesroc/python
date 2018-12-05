import csv
import datetime

def read():
    lista = []
    file = open('Compras.txt', 'r')
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

def addCompras(lista):
    
    temporaria = []
    nome = input('Lista de compras: ')
    
    temporaria += [nome]
    actual = datetime.datetime.now()
    temporaria += [actual]
    temporaria += [""]
    temporaria += ["aberta"]
    observacoes = input('deseja colocar observações? ')
    if observacoes == 'Sim':
        obs = input('esvreva as observacões: ')
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
    seletor = int(input('selecione o que pretende editar: ')) -1
    
    if lista[seletor][3] == 'Fechada':
        resp = input('O elemento esta pago. tem a certeza que quer modica lo: ')
        if resp == 'nN':
            return
        
        print('1. Nome ')
        print('2. observaçoes')
    opcao = input('que pretende modificar?' )
    if opcao == 1:
        nome = input('Novo nome: ')
        lista[seletor][0] = nome
    elif opcao == 2:
        observacoes = input('Nova observação: ')
        lista[seletor][4] = observacoes

def remove(lista):
    
    cont = 1
    for row in lista:
        print(cont,')',row[0])
        cont += 1
    opcao = int(input('Selecione o elemento que pretende retirar.'))
    opcao -= 1
    lista.remove(lista[opcao])
    
    return lista        
