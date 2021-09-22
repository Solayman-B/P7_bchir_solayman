import csv
import itertools

list_actions = []
list_invest = []
list_benef = []

list_profit = []
list_lenght = []
result = []
best_invest = []

# addition of the amounts invested in a list
def how_much_invest(a_list):
    somme = 0
    for i in a_list:
        somme = somme + i
    return somme

# open the file and get the data
with open(input("nom du fichier a ouvrir\n>>> "),newline='') as f:
    liste_action = []
    liste_investment = []
    liste_benefit = []
    liste_tuples = []
    max_expense = 500
    read = list(csv.reader(f))
    for line in read[1:]:
        if len(line) == 1:
            line = line[0].split(";")
        x = line[1].lstrip("\t")
        if x.replace(".","",1).isdigit() and 0 < float(x) <= max_expense:
            liste_action.append(line[0])
            liste_investment.append(float(x))
            liste_benefit.append(float(line[2].rstrip("%").lstrip("\t")))

# form all possible combinations
for i in range(len(liste_investment)):
    list_actions.append(list(itertools.combinations(liste_action, i)))
    list_invest.append(list(itertools.combinations(liste_investment, i)))
    list_benef.append(list(itertools.combinations(liste_benefit, i)))

# calculation of the length of each list in the list of list
for i in range(len(liste_investment)):
    list_lenght.append(len(list_invest[i]))

# filtering of results for investments above the limit
def filter_results(best_result = 999):
    for x in range(len(liste_investment)):
        for y in range(list_lenght[x]):
            if how_much_invest(list_invest[x][y]) < max_expense:
                # prix de l'action * pourcentage / 100
                for invest, benef in zip(list_invest[x][y], list_benef[x][y]):
                    result.append(invest * benef / 100)
                list_profit.append(how_much_invest(result))
                if how_much_invest(result) >= int(best_result):
                    print("Solayman bought:\n", list_actions[x][y], "\nTotal cost: ", how_much_invest(list_invest[x][y]), "€\nProfit: ", round(best_result, 2), "€")
                result.clear()

filter_results()
# maximum profit recovery
filter_results(max(list_profit))