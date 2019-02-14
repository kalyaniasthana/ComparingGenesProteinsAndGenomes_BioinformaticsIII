# -*- coding: utf-8 -*-
#from __future__ import print_function
import copy


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

def TopologicalSorting(d_with_weights, start):
	d_without_weights = {}
	for key in d_with_weights:
		if key not in d_without_weights:
			d_without_weights[int(key)] = []

	for key in d_with_weights:
		for item in d_with_weights[key]:
			l = item.split(':')
			d_without_weights[int(key)].append(int(l[0]))

	distance_dict = {}
	for key in d_with_weights:
		if key not in distance_dict:
			distance_dict[int(key)] = []
	for key in d_with_weights:
		for item in d_with_weights[key]:
			l = item.split(':')
			distance_dict[int(key)].append(int(l[1]))	


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


	for key in indegree_dict:
		if indegree_dict[key] == 0 and key not in stack and key!=start:
			stack.append(key)

	if start not in stack:
		stack.append(int(start))

	#print(stack)

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


	return topological_order,d_without_weights, distance_dict

def ReverseGraph(d_without_weights, distance_dict):
	#keys are nodes and values are incoming edges
	d_rev = {}
	d_rev_weights = {}
	d = d_without_weights
	d_ = distance_dict
	for node in d:
		if node not in d_rev:
			d_rev[node] = []
		for edge in d[node]:
			if edge not in d_rev:
				d_rev[edge] = []

	for node in d_rev:
		for node_ in d:
			if node in d[node_]:
				d_rev[node].append(node_)

	for node in d_rev:
		if node not in d_rev_weights:
			d_rev_weights[node] = []

	for node in d_rev:
		for node_ in d:
			if node in d[node_]:
				node_index = d[node_].index(node)
				d_rev_weights[node].append(distance_dict[node_][node_index])


	return d_rev, d_rev_weights


def LongestPathDAG(d_rev, d_rev_weights, d_without_weights, distance_dict, topological_order, start, end):
	source = int(start)
	sink = int(end)
	if source not in topological_order or sink not in topological_order:
		return None

	#a = len(topological_order) - topological_order[::-1].index(source) - 1
	a = topological_order.index(source)
	b = topological_order.index(sink)

	if a>=b:
		return None
	order = topological_order[a:b+1]
	#print(order)

	s = {source: 0}
	backtrack = {source: None}

	#longest path value
	for node in order:
		lmax = float('-Inf')
		if len(d_rev[node]) == 0:
			s[node] = 0
			#print(node, '**')
		else:
			for incoming_edge in d_rev[node]:
				if incoming_edge in backtrack:
					v = d_rev[node].index(incoming_edge)
					#print(incoming_edge,'ie')
					#print(s[v],'!!!!')
					#print(d_rev_weights[node][v],'####')
					l = s[incoming_edge] + d_rev_weights[node][v]
					if l > lmax:
						lmax = l
						s[node] = l
						backtrack[node] = incoming_edge

	longest_path_weight = s[sink]
	path = []
	node = sink
	while (not node is None):
		path.append(str(node))
		node = backtrack[node]
	path.reverse()
	m = '->'.join(path)
	print(backtrack)
	print(order)

	return longest_path_weight, m


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

#start = 'a'
#end = '19'
#d = {}
#file = '../Downloads/dataset_245_7.txt'
#with open(file) as f:
#	for line in f:
#		if line[len(line) - 1] == '\n':
#			line = line[:-1]
#		l = line.split('->')
#		if l[0] not in d:
#			d[l[0]] = []
#		d[l[0]].append(l[1])

#d = {'a': ['b', 'c', 'd', 'e', 'f'], 'b': ['c', 'f'], 'c': ['d'], 'e': ['d', 'f']}
#topological_order, d_without_weights, distance_dict = TopologicalSorting(d, start)
#print(topological_order)
#print(d_without_weights)
#print('********')
#print(distance_dict)
#print('********')
#d_rev, d_rev_weights = ReverseGraph(d_without_weights, distance_dict)
#print(d_rev)
#print('***')
#print(d_rev_weights)
#print(LongestPathDAG(d_rev, d_rev_weights, d_without_weights, distance_dict, topological_order, start, end))