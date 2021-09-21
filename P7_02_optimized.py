import csv
import itertools

# ouvrir le fichier algoinvest.txt et récupérer les données
with open('algoinvest.txt', newline='') as f:
	read = csv.reader(f)
	liste_action = []
	liste_invessment = []
	liste_benefit = []
	max_expense = 500

	# retirer les entetes et nettoyer les données
	for line in read:
		if line[1].lstrip("\t").isdigit() and 0 < int(line[1].lstrip("\t")) <= max_expense:
			liste_action.append(line[0])
			liste_invessment.append(int(line[1].lstrip("\t")))
			liste_benefit.append(int(line[2].rstrip("%").lstrip("\t")))
	duplicated_action = []
	duplicated_invessment = []
	duplicated_benefit = []
	for i in liste_benefit:
		x = liste_benefit.count(i)
		if x > 1:
			index = liste_benefit.index(i)
			duplicated_action.append(liste_action.pop(index))
			duplicated_invessment.append(liste_invessment.pop(index))
			duplicated_benefit.append(liste_benefit.pop(index))

	# trier la liste des % de benef par ordre décroissant
	sorted_liste_benefit = sorted(liste_benefit, reverse = True)
	expense = 0
	liste_bought_actions = []
	liste_total_benef = []

	def optimise_it(expense):
		for i in sorted_liste_benefit:
			index = liste_benefit.index(i)
			if max_expense - expense >= liste_invessment[index]:
				del sorted_liste_benefit[sorted_liste_benefit.index(i)]
				expense = update_it(expense, index)
				if min(sorted_liste_benefit) <= max_expense - expense:
					optimise_it(expense)
				return expense

	def clear_it():
		del duplicated_action[duplicated_index], duplicated_invessment[duplicated_index], duplicated_benefit[duplicated_index], sorted_liste_benefit[0]

	def update_it(expense, i, d = 0):
		if d == 1:
			expense += duplicated_invessment[i]
			liste_bought_actions.append(duplicated_action[i])
			liste_total_benef.append(duplicated_benefit[i])	#expense * duplicated_benefit[i] / 100
		else:
			expense += liste_invessment[i]
			liste_bought_actions.append(liste_action[i])
			liste_total_benef.append(liste_benefit[i])	#expense * liste_benefit[i] / 100
		return expense

	while expense < max_expense:
		index = liste_benefit.index(sorted_liste_benefit[0])
		if sorted_liste_benefit[0] in duplicated_benefit:
			duplicated_index = duplicated_benefit.index(sorted_liste_benefit[0])
			if (expense + duplicated_invessment[duplicated_index] + liste_invessment[index]) <= max_expense:
				expense = update_it(expense, index)
				expense = update_it(expense, duplicated_index, 1)
				clear_it()
			elif liste_invessment[index] >= duplicated_invessment[duplicated_index] and expense + liste_invessment[index]<= max_expense:
				expense = update_it(expense, index)
				clear_it()
			elif duplicated_invessment[duplicated_index] >= liste_invessment[index] and expense + duplicated_invessment[duplicated_index]<= max_expense:
				expense = update_it(expense, duplicated_index, 1)
				clear_it()
			else:
				expense = optimise_it(expense)
				clear_it()
				continue
		elif expense + liste_invessment[index] <= max_expense:
			expense = update_it(expense, index)
			del sorted_liste_benefit[0]
		else:
			expense = optimise_it(expense)
			break
print(expense, liste_bought_actions, liste_total_benef, sorted_liste_benefit)