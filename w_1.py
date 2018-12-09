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

money = 19212
coins = [19,13,5,3,1]
print DPchange(money, coins)