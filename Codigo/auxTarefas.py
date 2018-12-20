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
    list=[]
    dir = openTxt(r"\tarefas.txt")
    myFile = open(os.path.join(dir),"r")
    reader = csv.reader(myFile, delimiter=";", quotechar='"')

    for row in reader:
        if row:
            list = list + [row]
    myFile.close()
    return(list)


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
    list = []
    dir = openTxt(r"\listaTarefas.txt")
    myFile = open(os.path.join(dir), "r")
    reader = csv.reader(myFile, delimiter=";", quotechar='"')

    for row in reader:
        if row:
            list = list + [row]
    myFile.close()
    return (list)


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


def consultFunc(list,funcao):
    # funcao pode ser main ou sort

    for row in list.lista:
        if (row[3] == "Fechada" and funcao == "sort") or funcao == "main":
            print(row[0])
            print("Data de Criação:",row[1])
            if row[3] == "Fechada":
                print("Estado:", row[3], "-> Data de concretização", row[2])
            else:
                print("Estado:", row[3])
            print("Observações:", row[4])
            print("------------------------------------------------------")


def removeFunc(list):
    sel = 1
    for row in list.lista:
        print(sel,")",row[0])
        sel = sel + 1
    print("Selecione a tarefa que pretende remover:")

    op = int(input())
    op =  op - 1

    list.lista.remove(list.lista[op])
    list.num = str(int(list.num) - 1)

    return(list)

def addTarefa(list):
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

    list.lista = list.lista + [temp]
    list.num = str(int(list.num) + 1)
    return list

def closeTarefa(list):  #mudar list para list.lista
    temp = []
    sel = 1

    for i in range(0,len(list.lista)):
        if list.lista[i][3] == "Aberta":
            print(sel,")",list.lista[i][0])
            temp = temp + [i]
            sel = sel + 1
    if sel == 1:
        print("Todas as tarefas estao fechadas!")
    else:
        print("Escolhe a tarefa que quer fechar:")
        sel = int(input()) - 1
        list.lista[temp[sel]][2] = datetime.datetime.now()
        list.lista[temp[sel]][3] = "Fechada"
    return(list)

def estadoTarefa(list):  #mudar list para list.lista
    print("Deseja ver as tarefas:")
    print("1. Abertas")
    print("2. Fechadas")
    op = int(input())

    for row in list.lista:
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

def editTarefa(list): #mudar list para list.lista
    sel = 1

    print("Selecione a lista que pretende editar:")
    for row in list.lista:
        print(sel, ")", row[0] )
        sel = sel + 1

    sel = int(input()) -1
    if list.lista[sel][3] == "Fechada":
        print("A tarefa esta fechada tem a certeza que deseja modificar-la? \n 1) sim, \n 2) nao")
        resp = input()
        if resp == "2":
            return list
    print("Pretende mudar o nome ou as obeservações?")
    print("1. Nome")
    print("2. Observações")
    op = int(input())
    if op == 1:
        print("Escreva o novo nome!")
        list.lista[sel][0] = input()
    if op == 2:
        print("Escreva a nova observação!")
        list[sel][4] = input()
    return list

def searchTarefa(list): #mudar list para list.lista
    print("Digite:")

    x = input()

    sel = 1

    temp = []

    for i in range(0, len(list.lista)):
        d = list.lista[i][0].find(x)
        if d != -1:
            print(sel, ")", list.lista[i][0])
            temp = temp + [i]
            sel = sel + 1

    if sel != 1:
        print("Que tarefa deseja selecionar?")
        op = int(input()) -1
        print(list.lista[temp[op]][0])
        print("Data de Criação:", list.lista[temp[op]][1])
        if list.lista[temp[op]][3] == "Fechada":
            print("Estado:", list.lista[temp[op]][3], "-> Data de concretização", list.lista[temp[op]][2])
        else:
            print("Estado:", list.lista[temp[op]][3])
        print("Observações:", list.lista[temp[op]][4])
        print("------------------------------------------------------")

def sortTarefa(list): #mudar list para list.lista
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

        while i < len(list.lista)-1:
            if (list.lista[i+1][campo] < list.lista[i][campo]):
                aux = list.lista[i]
                list.lista[i] = list.lista[i+1]
                list.lista[i+1] = aux
                changed = True

            i = i+1

        if (changed == False):
            break;

    consultFunc(list,"sort")

def atualiza(allLists, lista):
    for i in range(0,len(allLists)):
        if allLists[i].nome == lista.nome:
            allLists[i] = lista
    return allLists

def mudarLista(allLists):
    sel = 1
    leng = len(allLists)
    print("len",leng)
    for list in allLists:
        print(sel, ')', list.nome)
        sel = sel + 1
    op=int(input("Qual e que deseja mudar:"))
    op = op - 1
    list = allLists[op]
    return list

def mudarNomeLista(list): #list.nome
    nome = input("Novo nome da lista:")
    list.nome = nome
    return list

def criarList(allLists):
    nome = input("Qual o nome da lista:")
    allLists.append(myLists(nome,"0",[]))
    return allLists