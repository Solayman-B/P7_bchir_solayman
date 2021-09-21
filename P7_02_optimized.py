import csv

# the best ROI strategy
def find_best_investment(remainig_money, data):
	# fill with 0s when there's no invest
	matrix = [[0 for i in range(remainig_money + 1)] for i in range(len(data) + 1)]

	# scrolling down the number of the share
	for x in range(1, len(data) + 1):
		# scrolling down the invested money
		for y in range(1, remainig_money + 1):
			# if we can invest in this share (the share price <= remaining money)
			if data[x-1][1] <= y:
				# we get the max of the 2 invests (the best one)
				matrix[x][y] = max(data[x-1][2] + matrix[x-1][y-data[x-1][1]], matrix[x-1][y])
			else:
				# otherwise we keep the previous one
				matrix[x][y] = matrix[x-1][y]

	# identify elements based on the sum
	n = len(data)
	data_selection = []

	while remainig_money >= 0 and n >= 0:
		# we get the last element of the list
		e = data[n-1]
		if matrix[n][remainig_money] == matrix[n-1][remainig_money-e[1]] + e[2]:
			data_selection.append(e)
			remainig_money -= e[1]
		n -= 1

	return matrix[-1][-1], data_selection


# open the file algoinvest.txt and get the data
with open('algoinvest.txt', newline='') as f:
	read = csv.reader(f)
	remainig_money = 500
	data = []

	# delete the headers and clean the data
	for line in read:
		x = line[1].lstrip("\t")
		y = line[2].rstrip("%").lstrip("\t")
		if x.isdigit() and 0 < int(x) <= remainig_money:
			data.append((line[0], int(x), (int(x) * int(y) / 100)))	# name of the share, invest amount €, achievable benefit €

print(find_best_investment(remainig_money, data))