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


def consultFunc(list,funcao):
    # funcao pode ser main ou sort

    for row in list:
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

    sel = int(input()) -1
    if list[sel][3] == "Fechada":
        print("A tarefa esta fechada tem a certeza que deseja modificar-la?")
        resp = input()
        if resp == "nao":
            return
    print("Pretende mudar o nome ou as obeservações?")
    print("1. Nome")
    print("2. Observações")
    op = int(input())
    if op == 1:
        print("Escreva o novo nome!")
        list[sel][0] = input()
    if op == 2:
        print("Escreva a nova observação!")
        list[sel][4] = input()

def searchTarefa(list):
    print("Digite:")

    x = input()

    sel = 1

    temp = []

    for i in range(0, len(list)):
        d = list[i][0].find(x)
        if d != -1:
            print(sel, ")", list[i][0])
            temp = temp + [i]
            sel = sel + 1

    if sel != 1:
        print("Que tarefa deseja selecionar?")
        op = int(input()) -1
        print(list[temp[op]][0])
        print("Data de Criação:", list[temp[op]][1])
        if list[temp[op]][3] == "Fechada":
            print("Estado:", list[temp[op]][3], "-> Data de concretização", list[temp[op]][2])
        else:
            print("Estado:", list[temp[op]][3])
        print("Observações:", list[temp[op]][4])
        print("------------------------------------------------------")

def sortTarefa(list):
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

        while i < len(list)-1:
            if (list[i+1][campo] < list[i][campo]):
                aux = list[i]
                list[i] = list[i+1]
                list[i+1] = aux
                changed = True

            i = i+1

        if (changed == False):
            break;

    consultFunc(list,"sort")

print (list)