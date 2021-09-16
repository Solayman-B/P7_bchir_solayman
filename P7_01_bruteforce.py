import csv
import itertools
liste_a = []
liste_invest = []
liste_actions = []
liste_c =[]
amont_benefice = []
max_expense = 500
amont_invest = 0
new_liste = []



def how_much_invest(liste):
    somme = 0
    for i in liste:
        somme = somme + i
    #print(somme)
    return somme
with open('algoinvest.txt',newline='') as f:
    tableau=[]
    lire=csv.reader(f)
    for ligne in lire:
        a = ligne[1].lstrip("\t")
        b = ligne[2].rstrip("%").lstrip("\t")
        liste_c.append(ligne[0])
        if a.isdigit():
            a = int(a)
            b = int(b)
            amont_benefice = amont_invest + (a*b/100)
            liste_a.append(a)
            amont_invest = amont_invest + a
            #print(amont_invest)
            #print(amont_benefice)
            #print(ligne[0])

for i in range(1, 16):
    liste_invest.append(list(itertools.combinations(liste_a, i)))
    liste_actions.append(list(itertools.combinations(liste_c, i)))

list_lenght = 0

for i in range(15):
    list_lenght = list_lenght + len(liste_invest[i])
    new_liste.append(len(liste_invest[i]))
    print(len(liste_invest[i]))
#print(list_lenght)

#print(liste_invest[9][184755])
#longueur max 16 soit range 17

#print(liste_invest[0][0], "it's me Mario")

#for x, y in zip(range(10), range(new_liste[x])):
 #   if how_much_invest(liste_invest[x][y]) < 500:
  #      print(liste_invest[x][y])


for x in range(15):
    for y in range(new_liste[x]):
        if how_much_invest(liste_invest[x][y]) < 500:
            print(liste_invest[x][y])
            print(how_much_invest(liste_invest[x][y]))