def knapsack(n, W, val, wt):
	print('\nKnapsack weigth: ' + str(W) + ', number of items: ' + str(n))

	K = [[0 for w in range(W + 1)] 
			for i in range(n + 1)]

	# Build table K[][] in bottom up manner 
	for i in range(n + 1): 
		for w in range(W + 1): 
			if i == 0 or w == 0: 
				K[i][w] = 0

			elif wt[i - 1] <= w:   # if item i -1 will fit within weight j
				# add item i - 1 if value is better than without item i
				K[i][w] = max(K[i - 1][w], val[i - 1] + K[i - 1][w - wt[i - 1]]) 

			else:   # otherwise, don't add item
				K[i][w] = K[i - 1][w]

	"""print('\n> Final Table:')
				print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in K]))"""

	# stores the result of Knapsack
	res = K[n][W] 
	print('\n> Result: ', res) 
	print()

	w = W 
	for i in range(n, 0, -1): 
		if res <= 0: 
			break

		if res == K[i - 1][w]:   # item not included
			continue

		else:   # item included
			print('> Item with value ' + str(val[i - 1]) + ' and weith ' + str( wt[i - 1]) + ' included') 
			res = res - val[i - 1]   # decrease value
			w = w - wt[i - 1]   # decrease knapsack weigth

