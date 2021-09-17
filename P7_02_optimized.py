import csv
import itertools

list_a = []
list_i = []
optimised_list_i = []
list_b = []
optimised_list_b = []
list_actions = []
list_invest = []
list_benef = []
max_expense = 500.0
expense = 0.0
index = float
list_profit = []
list_lenght = []
result = []
best_invest = []
list_to_del = []
optimised_benefit = []

# ouvrir le fichier algoinvest.txt et récupérer les données
with open('algoinvest.txt', newline='') as f:
	tableau = []
	lire = csv.reader(f)
	for ligne in lire:
		list_a.append(ligne[0])
		invest = ligne[1].lstrip("\t")
		benef = ligne[2].rstrip("%").lstrip("\t")
		if invest.isdigit():
			invest = int(invest)
			list_i.append(invest)
			benef = int(benef)
			list_b.append(benef)


# addition des sommes investis dans une liste
def how_much_invest(a_list):
	somme = 0
	for i in a_list:
		somme = somme + i
	# print(somme)
	return somme


# récupérer l'action ayant le plus gros pourcentage
while expense < max_expense:
	index = list_b.index(max(list_b))
	if expense + list_i[index] <= 500:
		list_invest.append(list_i[index])
		expense = how_much_invest(list_invest)
		list_benef.append(list_i.pop(index) * list_b.pop(index) / 100)
		profit = how_much_invest(list_benef)
	else:
		break

# tenter d'améliorer le résultat obtenu
for i, b in zip(list_i, list_b):
	if i > (max_expense - expense):
		list_to_del.append(index)

for i in list_to_del:
	del list_i[i]
	del list_b[i]
	optimised_benefit.append(list_i[i] * list_b[i] / 100)

print(max(optimised_benefit))

		#optimised_list_i.append(i)
		#optimised_list_b.append(b)
		#index = list_b.index(max(list_b))
		#list_invest.append(list_i.pop(index))
		#expense = how_much_invest(list_invest)
		#list_benef.append(list_b.pop(index))
		#profit = how_much_invest(list_benef)
print("list_invest ", list_invest, "list_benef ", list_benef, "expense ", expense, "profit ", profit)
