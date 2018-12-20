import csv
import datetime
import os

class myLists():
    def __init__(self, nome, num, lista):
        self.nome = nome
        self.num = num
        self.lista = lista

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

def readFunc():
    lista=[]
    dir = openTxt(r"\tarefas.txt")
    myFile = open(os.path.join(dir),"r")
    reader = csv.reader(myFile, delimiter=";", quotechar='"')

    for row in reader:
        if row:
            lista = lista + [row]
    myFile.close()
    return(lista)


def writeFunc(allLists):
    dir = openTxt(r"\tarefas.txt")
    myFile = open(os.path.join(dir), "w")
    writer = csv.writer(myFile, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)

    for row in allLists:
        print("*",row.lista)
        for elem in row.lista:
            print("+",elem)
            writer.writerow(elem)
    myFile.close()

def readNomeListas():
    lista = []
    dir = openTxt(r"\listaTarefas.txt")
    myFile = open(os.path.join(dir), "r")
    reader = csv.reader(myFile, delimiter=";", quotechar='"')

    for row in reader:
        if row:
            lista = lista + [row]
    myFile.close()
    return (lista)


def writeNomeListas(alllists):
    dir = openTxt(r"\listaTarefas.txt")
    myFile = open(os.path.join(dir), "w")
    writer = csv.writer(myFile, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)

    for row in alllists:
        s = [row.nome, row.num]
        print (s)
        writer.writerow(s)
    myFile.close()


def getListas(tarefas, nomeListas):
    allLists = []
    x = 0
    for row in nomeListas:
        y = x + int(row[1])
        allLists = allLists + [myLists(row[0], row[1], tarefas[x:y])]
        x = x + int(row[1])
    return allLists


def consultFunc(lista,funcao):
    # funcao pode ser main ou sort

    for row in lista.lista:
        if (row[3] == "Fechada" and funcao == "sort") or funcao == "main":
            print(row[0])
            print("Data de Criação:",row[1])
            if row[3] == "Fechada":
                print("Estado:", row[3], "-> Data de concretização", row[2])
            else:
                print("Estado:", row[3])
            print("Observações:", row[4])
            print("------------------------------------------------------")


def removeFunc(lista):
    sel = 1
    for row in lista.lista:
        print(sel,")",row[0])
        sel = sel + 1
    print("Selecione a tarefa que pretende remover:")

    op = int(input())
    op =  op - 1

    lista.lista.remove(lista.lista[op])
    lista.num = str(int(lista.num) - 1)

    return(lista)

def addTarefa(lista):
    temp = []
    print("Nome que pretende:")
    nome = input()
    temp = temp + [nome]
    data = datetime.datetime.now()
    temp = temp + [data]
    temp = temp + [""]
    temp = temp + ["Aberta"]
    print("Deseja deixar observações?:")
    obs = input()
    if obs == "sim":
        print("Escreva as observações")
        obs2 = input()
    else:
        obs2 = ""
    temp = temp + [obs2]

    lista.lista = lista.lista + [temp]
    lista.num = str(int(lista.num) + 1)
    return lista

def closeTarefa(lista):  #mudar lista para lista.lista
    temp = []
    sel = 1

    for i in range(0,len(lista.lista)):
        if lista.lista[i][3] == "Aberta":
            print(sel,")",lista.lista[i][0])
            temp = temp + [i]
            sel = sel + 1
    if sel == 1:
        print("Todas as tarefas estao fechadas!")
    else:
        print("Escolhe a tarefa que quer fechar:")
        sel = int(input()) - 1
        lista.lista[temp[sel]][2] = datetime.datetime.now()
        lista.lista[temp[sel]][3] = "Fechada"
    return(lista)

def estadoTarefa(lista):  #mudar lista para lista.lista
    print("Deseja ver as tarefas:")
    print("1. Abertas")
    print("2. Fechadas")
    op = int(input())

    for row in lista.lista:
        if (op == 1) and (row[3]== "Aberta"):
            print(row[0])
            print("Data de Criação:", row[1])
            print("Estado:", row[3])
            print("Observações:", row[4])
            print("------------------------------------------------------")
        if op == 2 and row[3] == "Fechada":
            print(row[0])
            print("Data de Criação:", row[1])
            print("Estado:", row[3], "-> Data de concretização", row[2])
            print("Observações:", row[4])
            print("------------------------------------------------------")

def editTarefa(lista): #mudar lista para lista.lista
    sel = 1

    print("Selecione a lista que pretende editar:")
    for row in lista.lista:
        print(sel, ")", row[0] )
        sel = sel + 1

    sel = int(input()) -1
    if lista.lista[sel][3] == "Fechada":
        print("A tarefa esta fechada tem a certeza que deseja modificar-la? \n 1) sim, \n 2) nao")
        resp = input()
        if resp == "2":
            return lista
    print("Pretende mudar o nome ou as obeservações?")
    print("1. Nome")
    print("2. Observações")
    op = int(input())
    if op == 1:
        print("Escreva o novo nome!")
        lista.lista[sel][0] = input()
    if op == 2:
        print("Escreva a nova observação!")
        lista[sel][4] = input()
    return lista

def searchTarefa(lista): #mudar lista para lista.lista
    print("Digite:")

    x = input()

    sel = 1

    temp = []

    for i in range(0, len(lista.lista)):
        d = lista.lista[i][0].find(x)
        if d != -1:
            print(sel, ")", lista.lista[i][0])
            temp = temp + [i]
            sel = sel + 1

    if sel != 1:
        print("Que tarefa deseja selecionar?")
        op = int(input()) -1
        print(lista.lista[temp[op]][0])
        print("Data de Criação:", lista.lista[temp[op]][1])
        if lista.lista[temp[op]][3] == "Fechada":
            print("Estado:", lista.lista[temp[op]][3], "-> Data de concretização", lista.lista[temp[op]][2])
        else:
            print("Estado:", lista.lista[temp[op]][3])
        print("Observações:", lista.lista[temp[op]][4])
        print("------------------------------------------------------")

def sortTarefa(lista): #mudar lista para lista.lista
    campo = 0
    print("Quer organizar por: \n 1) nome, \n 2) data de criação \n 3) data de concretisação")
    op = int(input())

    if op == 1:
        campo = 0
    elif op == 2:
        campo = 1
    elif op == 3:
        campo = 2

    while(True):
        i = 0
        changed = False

        while i < len(lista.lista)-1:
            if (lista.lista[i+1][campo] < lista.lista[i][campo]):
                aux = lista.lista[i]
                lista.lista[i] = lista.lista[i+1]
                lista.lista[i+1] = aux
                changed = True

            i = i+1

        if (changed == False):
            break;

    consultFunc(lista,"sort")

def atualiza(allLists, lista):
    for i in range(0,len(allLists)):
        if allLists[i].nome == lista.nome:
            allLists[i] = lista
    return allLists

def mudarLista(allLists):
    sel = 1
    leng = len(allLists)
    print("len",leng)
    for lista in allLists:
        print(sel, ')', lista.nome)
        sel = sel + 1
    op=int(input("Qual e que deseja mudar:"))
    op = op - 1
    lista = allLists[op]
    return lista

def mudarNomeLista(lista): #lista.nome
    nome = input("Novo nome da lista:")
    lista.nome = nome
    return lista

def criarList(allLists):
    nome = input("Qual o nome da lista:")
    allLists.append(myLists(nome,"0",[]))
    return allLists