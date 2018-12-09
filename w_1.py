def DPchange(money, coins):
	MinNumCoins = {}
	for m in range(0, money + 1):
		if m not in MinNumCoins:
			MinNumCoins[m] = 99999
	MinNumCoins[0] = 0
	for m in range(1, money + 1):
		MinNumCoins[m] = 99999
		for coin in coins:
			if m >= coin:
				if MinNumCoins[m - coin] + 1 < MinNumCoins[m]:
					MinNumCoins[m] = MinNumCoins[m - coin] + 1
	return MinNumCoins[money]

def ManhattanTourist(n, m, down, right):
	s = []
	for i in range(0, n + 1):
		l = []
		for j in range(0, m + 1):
			l.append(0)
		s.append(l)
	for i in range(1, n+1):
		s[i][0] = s[i-1][0] + down[i - 1][0]
	for i in range(1, m+1):
		s[0][j] = s[0][j-1] + right[0][j - 1]
	for i in range(1, n + 1):
		for j in range(1, m + 1):
			s[i][j] = max(s[i-1][j] + down[i-1][j], s[i][j-1] + right[i][j-1])
	return s[n][m]

def ManhattanTouristInput(file):
	#remove '-' from file, otw this function won't work!!
	n = 0
	m = 0
	down = []
	right = []
	with open(file) as f:
		for line in f:
			if line[len(line) - 1] == '\n':
				line = line[: -1]
			l = line.split(' ')
			l = map(int, l)
			if len(l) == 2:
				n = l[0]
				m = l[1]
			elif len(l) == m + 1:
				down.append(l)
			elif len(l) == m:
				right.append(l)
			else:
				continue

	return (n, m, down, right)




#money = 19212
#coins = [19,13,5,3,1]
#print DPchange(money, coins)

#n = 4
#m = 4
#down = [[1, 0, 2, 4, 3], [4, 6, 5, 2, 1], [4, 4, 5, 2, 1] ,[5, 6, 8, 5, 3]]
#right = [[3, 2, 4, 0], [3, 2, 4, 2], [0, 7, 3, 3] ,[3, 3, 0, 2], [1, 3, 2, 2]]

file = '../Downloads/dataset_261_10.txt'
n, m, down, right =  ManhattanTouristInput(file)
print ManhattanTourist(n, m, down, right)