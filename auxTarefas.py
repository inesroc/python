import csv
import datetime

def readFunc():
    list=[]
    myFile = open("tarefas.txt", "r")
    reader = csv.reader(myFile, delimiter=";", quotechar='"')

    for row in reader:
        if row:
            list = list + [row]
    myFile.close()
    return(list)


def writeFunc(list):

    myFile = open("tarefas.txt", "w")
    writer = csv.writer(myFile, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)

    for row in list:
        writer.writerow(row)
    myFile.close()


def cansultFunc(list):

    for row in list:
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
    for row in list:
        print(sel,")",row[0])
        sel = sel + 1
    print("Selecione a tarefa que pretende remover:")

    op = int(input())
    op =  op - 1

    list.remove(list[op])

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

    list = list + [temp]
    return list

def closeTarefa(list):
    temp = []
    sel = 1

    for i in range(0,len(list)):
        if list[i][3] == "Aberta":
            print(sel,")",list[i][0])
            temp = temp + [i]
            sel = sel + 1
    if sel == 1:
        print("Todas as tarefas estao fechadas!")
    else:
        print("Escolhe a tarefa que quer fechar:")
        sel = int(input()) - 1
        list[temp[sel]][2] = datetime.datetime.now()
        list[temp[sel]][3] = "Fechada"

    return(list)

def estadoTarefa(list):
    temp = []

    print("Deseja ver as tarefas:")
    print("1. Abertas")
    print("2. Fechadas")
    op = int(input())

    for row in list:
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

def editTarefa(list):
    sel = 1

    print("Selecione a lista que pretende editar:")
    for row in list:
        print(sel, ")", row[0] )
        sel = sel + 1
    if list[sel][3] == "Fechada":
        print("A tarefa esta fechada tem a certeza que deseja modificar-la?")
        op = input()
        if op == "nao":
            return
    print("Pretende mudar o nome ou as obeservações?")
    print("1. Nome")
    print("2. Observações")
    op = int(input())
    if op == 1:
        print("Escreva o novo nome!")
        list[sel][0] = input()
    if op == 2:
        print("Escreva a nova descrição!")
        list[sel][4] = input()

def searchTarefa(list):
    print("Digite:")

    x = input()

    sel = 1

    temp = []

    for elem in list:
        d = elem[0].find(x)
        if d != -1:
            print(sel,")", elem[0])
            sel = sel + 1
    print("Que tarefa deseja selecionar?")
        for i in range(0, len(list)):

def sortTarefa(list):
    while(True):
        i = 0
        changed = False

        while i < len(list)-1:
            if (list[i+1] < list[i]):
                aux = list[i]
                list[i] = list[i+1]
                list[i+1] = aux
                changed = True

            i = i+1

        if (changed == False):
            return list

    return list

list = [54,26,93,1,2,5,174,25]
list = sortTarefa(list)
print (list)
