import csv
import itertools

# ouvrir le fichier algoinvest.txt et récupérer les données
with open('algoinvest.txt', newline='') as f:
	read = csv.reader(f)
	liste_action = []
	liste_invessment = []
	liste_benefit = []

	for line in read:
		if line[1].lstrip("\t").isdigit() and line[2].rstrip("%").lstrip("\t").isdigit():
			liste_action.append(line[0])
			liste_invessment.append(int(line[1].lstrip("\t")))
			liste_benefit.append(int(line[2].rstrip("%").lstrip("\t")))

	sorted_liste_benefit = sorted(liste_benefit, reverse = True)
	expense = 0
	max_expense = 500
	liste_bought_actions = []
	total_profit = 0

	def optimise_it(sorted_liste_benefit, max_expense, expense, liste_invessment, liste_bought_actions, total_profit, liste_benefit):
		for i in sorted_liste_benefit:
			if max_expense - expense >= liste_invessment[i]:
				#del sorted_liste_benefit[i]
				expense += liste_invessment[i]
				liste_bought_actions.append(liste_action[i])
				total_profit += liste_invessment[i] * liste_benefit[i] / 100
				print("expense", expense, "total_profit", total_profit)

	while expense < max_expense:
		index = liste_benefit.index(sorted_liste_benefit.pop(0))
		if expense + liste_invessment[index] <= max_expense:
			expense += liste_invessment[index]
			liste_bought_actions.append(liste_action[index])
			total_profit += liste_invessment[index] * liste_benefit[index] / 100
			print("expense", expense, "total_profit", total_profit)
		else:
			print("expense", expense, "total_profit", total_profit)
			optimise_it(sorted_liste_benefit, max_expense, expense, liste_invessment, liste_bought_actions, total_profit, liste_benefit)
			break





















"""
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

# while min prix action <= max_expense - expense fonction optimise
for i, b in zip(list_i, list_b):
	if i <= (max_expense - expense):
		benef = i * b / 100
		optimised_benefit.append(benef)
		if benef == max(optimised_benefit):
			print("i", i)
			new_expense = i
			new_expense_percent = b
expense += new_expense
profit += max(optimised_benefit)
print("investi ", new_expense, "pourcent ", new_expense_percent, "gain ", max(optimised_benefit))

optimised_benefit.clear()


# optimised_list_i.append(i)
# optimised_list_b.append(b)
# index = list_b.index(max(list_b))
# list_invest.append(list_i.pop(index))
# expense = how_much_invest(list_invest)
# list_benef.append(list_b.pop(index))
# profit = how_much_invest(list_benef)
print("list_invest ", list_invest, "list_benef ", list_benef, "expense ", expense, "profit ", profit)
"""