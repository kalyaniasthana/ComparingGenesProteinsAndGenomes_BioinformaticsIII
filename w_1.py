# -*- coding: utf-8 -*-
from __future__ import print_function


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

def LCSBackTrack(v,w):
	s = []
	backtrack = []
	p = len(v)
	q = len(w)
	s = [[0 for x in xrange(q+1)] for x in xrange(p+1)] 
	for i in range(0, p + 1):
		for j in range(0, q + 1):
			if i == 0 or j == 0: 
				s[i][j] = 0
			elif v[i-1] == w[j-1]: 
				s[i][j] = s[i-1][j-1] + 1
			else: 
				s[i][j] = max(s[i-1][j], s[i][j-1])

	LCS = []
	i = len(v)
	j = len(w)
	while i > 0 and j > 0:
		if v[i-1] == w[j-1]: 
			LCS.append(v[i-1]) 
			i-=1
			j-=1
		elif s[i-1][j] > s[i][j-1]: 
			i-=1
		else: 
			j-=1
	LCS = ''.join(LCS[::-1])
	return LCS

def TopologicalSorting(d_with_weights, start, end):
	d_without_weights = {}
	for key in d_with_weights:
		if key not in d_without_weights:
			d_without_weights[key] = []

	for key in d_with_weights:
		for item in d_with_weights[key]:
			l = item.split(':')
			d_without_weights[key].append(l[0])

	stack = []
	#calculating indegrees
	indegree_dict = {}
	for key in d_without_weights:
		if key not in indegree_dict:
			indegree_dict[key] = 0
		l = d_without_weights[key]
		for node in l:
			if node not in indegree_dict:
				indegree_dict[node] = 0

	for key in indegree_dict:
		count_in_key = 0
		for key_ in d_without_weights:
			l = d_without_weights[key_]
			if key in l:
				count_in_key += 1
		indegree_dict[key] = count_in_key


	if start not in stack:
		stack.append(start)

	for key in indegree_dict:
		if indegree_dict[key] == 0 and key not in stack:
			stack.append(key)

	topological_order = []

	while len(stack) > 0:
		u = stack.pop()
		topological_order.append(u)
		#print(topological_order)
		if u in d_without_weights:
			for node in d_without_weights[u]:
				indegree_dict[node] -= 1
				if indegree_dict[node] == 0:
					stack.append(node)

	return topological_order


#money = 21
#coins = [2,3]
#print(DPchange(money, coins))

#n = 4
#m = 4
#down = [[1, 0, 2, 4, 3], [4, 6, 5, 2, 1], [4, 4, 5, 2, 1] ,[5, 6, 8, 5, 3]]
#right = [[3, 2, 4, 0], [3, 2, 4, 2], [0, 7, 3, 3] ,[3, 3, 0, 2], [1, 3, 2, 2]]

#file = '../Downloads/dataset_261_10.txt'
#n, m, down, right =  ManhattanTouristInput(file)
#print ManhattanTourist(n, m, down, right)

#v = 'AACC'
#w = 'ACAC'
#backtrack = LCSBackTrack(v,w)
#for l in backtrack:
#	for element in l:
#		print(element, end = ' ')
#	print('\n')


#v = 'AACCTTGG'
#w = 'ACACTGTGA'
#backtrack = LCSBackTrack(v,w)
#i = len(v)
#j = len(w)
#print(OutputLCS(backtrack, v, i, j))

#X='AACCTTGG'
#Y='ACACTGTGA'
#print(LCSBackTrack(X, Y))

start = 'a'
end = 'f'
d = {'a': ['b:7', 'c:4'], 'b': ['e:2'], 'c': ['d:1', 'e:4'], 'd': ['f:3'], 'e': ['f:2']}
print(TopologicalSorting(d, start, end))

  
