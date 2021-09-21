import csv
import itertools

list_actions = []
list_invest = []
list_benef = []

list_profit = []
list_lenght = []
result = []
best_invest = []

# addition des sommes investis dans une liste
def how_much_invest(a_list):
    somme = 0
    for i in a_list:
        somme = somme + i
    #print(somme)
    return somme

# ouvrir le fichier algoinvest.txt et récupérer les données
with open('algoinvest.txt',newline='') as f:
    liste_action = []
    liste_invessment = []
    liste_benefit = []
    liste_tuples = []
    max_expense = 500
    read = csv.reader(f)
    for line in read:
        if line[1].lstrip("\t").isdigit() and int(line[1].lstrip("\t")) <= max_expense:
            liste_action.append(line[0])
            liste_invessment.append(int(line[1].lstrip("\t")))
            liste_benefit.append(int(line[2].rstrip("%").lstrip("\t")))
    print(liste_tuples)

# former toutes les combinaisons possibles jusqu'à 15 nombres pour toutes les colonnes
for i in range(1, 16):

    list_actions.append(list(itertools.combinations(liste_action, i)))
    list_invest.append(list(itertools.combinations(liste_invessment, i)))
    list_benef.append(list(itertools.combinations(liste_benefit, i)))

# calcul de la longeur de liste de chaque liste dans la liste de liste
for i in range(15):
    list_lenght.append(len(list_invest[i]))

# filtrage des résultats pour les investissements de moins de 500€
def filter_results(best_result = 999):
    for x in range(15):
        for y in range(list_lenght[x]):
            if how_much_invest(list_invest[x][y]) < 500:
                # prix de l'action * pourcentage / 100
                for invest, benef in zip(list_invest[x][y], list_benef[x][y]):
                    result.append(invest * benef / 100)
                list_profit.append(how_much_invest(result))
                if how_much_invest(result) >= int(best_result):
                    print("liste des actions ", list_invest[x][y], "liste des pourcentages ", list_benef[x][y], "le résultat ", best_result)
                result.clear()

filter_results()
# récupération du max du bénef
filter_results(max(list_profit))
