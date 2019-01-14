from __future__ import print_function, division
import copy

pam250 = {'A': {'A': 2, 'C': -2, 'E': 0, 'D': 0, 'G': 1, 'F': -3, 'I': -1, 'H': -1, 'K': -1, 'M': -1, 'L': -2, 'N': 0, 'Q': 0, 'P': 1, 'S': 1, 'R': -2, 'T': 1, 'W': -6, 'V': 0, 'Y': -3}, 'C': {'A': -2, 'C': 12, 'E': -5, 'D': -5, 'G': -3, 'F': -4, 'I': -2, 'H': -3, 'K': -5, 'M': -5, 'L': -6, 'N': -4, 'Q': -5, 'P': -3, 'S': 0, 'R': -4, 'T': -2, 'W': -8, 'V': -2, 'Y': 0}, 'E': {'A': 0, 'C': -5, 'E': 4, 'D': 3, 'G': 0, 'F': -5, 'I': -2, 'H': 1, 'K': 0, 'M': -2, 'L': -3, 'N': 1, 'Q': 2, 'P': -1, 'S': 0, 'R': -1, 'T': 0, 'W': -7, 'V': -2, 'Y': -4}, 'D': {'A': 0, 'C': -5, 'E': 3, 'D': 4, 'G': 1, 'F': -6, 'I': -2, 'H': 1, 'K': 0, 'M': -3, 'L': -4, 'N': 2, 'Q': 2, 'P': -1, 'S': 0, 'R': -1, 'T': 0, 'W': -7, 'V': -2, 'Y': -4}, 'G': {'A': 1, 'C': -3, 'E': 0, 'D': 1, 'G': 5, 'F': -5, 'I': -3, 'H': -2, 'K': -2, 'M': -3, 'L': -4, 'N': 0, 'Q': -1, 'P': 0, 'S': 1, 'R': -3, 'T': 0, 'W': -7, 'V': -1, 'Y': -5}, 'F': {'A': -3, 'C': -4, 'E': -5, 'D': -6, 'G': -5, 'F': 9, 'I': 1, 'H': -2, 'K': -5, 'M': 0, 'L': 2, 'N': -3, 'Q': -5, 'P': -5, 'S': -3, 'R': -4, 'T': -3, 'W': 0, 'V': -1, 'Y': 7}, 'I': {'A': -1, 'C': -2, 'E': -2, 'D': -2, 'G': -3, 'F': 1, 'I': 5, 'H': -2, 'K': -2, 'M': 2, 'L': 2, 'N': -2, 'Q': -2, 'P': -2, 'S': -1, 'R': -2, 'T': 0, 'W': -5, 'V': 4, 'Y': -1}, 'H': {'A': -1, 'C': -3, 'E': 1, 'D': 1, 'G': -2, 'F': -2, 'I': -2, 'H': 6, 'K': 0, 'M': -2, 'L': -2, 'N': 2, 'Q': 3, 'P': 0, 'S': -1, 'R': 2, 'T': -1, 'W': -3, 'V': -2, 'Y': 0}, 'K': {'A': -1, 'C': -5, 'E': 0, 'D': 0, 'G': -2, 'F': -5, 'I': -2, 'H': 0, 'K': 5, 'M': 0, 'L': -3, 'N': 1, 'Q': 1, 'P': -1, 'S': 0, 'R': 3, 'T': 0, 'W': -3, 'V': -2, 'Y': -4}, 'M': {'A': -1, 'C': -5, 'E': -2, 'D': -3, 'G': -3, 'F': 0, 'I': 2, 'H': -2, 'K': 0, 'M': 6, 'L': 4, 'N': -2, 'Q': -1, 'P': -2, 'S': -2, 'R': 0, 'T': -1, 'W': -4, 'V': 2, 'Y': -2}, 'L': {'A': -2, 'C': -6, 'E': -3, 'D': -4, 'G': -4, 'F': 2, 'I': 2, 'H': -2, 'K': -3, 'M': 4, 'L': 6, 'N': -3, 'Q': -2, 'P': -3, 'S': -3, 'R': -3, 'T': -2, 'W': -2, 'V': 2, 'Y': -1}, 'N': {'A': 0, 'C': -4, 'E': 1, 'D': 2, 'G': 0, 'F': -3, 'I': -2, 'H': 2, 'K': 1, 'M': -2, 'L': -3, 'N': 2, 'Q': 1, 'P': 0, 'S': 1, 'R': 0, 'T': 0, 'W': -4, 'V': -2, 'Y': -2}, 'Q': {'A': 0, 'C': -5, 'E': 2, 'D': 2, 'G': -1, 'F': -5, 'I': -2, 'H': 3, 'K': 1, 'M': -1, 'L': -2, 'N': 1, 'Q': 4, 'P': 0, 'S': -1, 'R': 1, 'T': -1, 'W': -5, 'V': -2, 'Y': -4}, 'P': {'A': 1, 'C': -3, 'E': -1, 'D': -1, 'G': 0, 'F': -5, 'I': -2, 'H': 0, 'K': -1, 'M': -2, 'L': -3, 'N': 0, 'Q': 0, 'P': 6, 'S': 1, 'R': 0, 'T': 0, 'W': -6, 'V': -1, 'Y': -5}, 'S': {'A': 1, 'C': 0, 'E': 0, 'D': 0, 'G': 1, 'F': -3, 'I': -1, 'H': -1, 'K': 0, 'M': -2, 'L': -3, 'N': 1, 'Q': -1, 'P': 1, 'S': 2, 'R': 0, 'T': 1, 'W': -2, 'V': -1, 'Y': -3}, 'R': {'A': -2, 'C': -4, 'E': -1, 'D': -1, 'G': -3, 'F': -4, 'I': -2, 'H': 2, 'K': 3, 'M': 0, 'L': -3, 'N': 0, 'Q': 1, 'P': 0, 'S': 0, 'R': 6, 'T': -1, 'W': 2, 'V': -2, 'Y': -4}, 'T': {'A': 1, 'C': -2, 'E': 0, 'D': 0, 'G': 0, 'F': -3, 'I': 0, 'H': -1, 'K': 0, 'M': -1, 'L': -2, 'N': 0, 'Q': -1, 'P': 0, 'S': 1, 'R': -1, 'T': 3, 'W': -5, 'V': 0, 'Y': -3}, 'W': {'A': -6, 'C': -8, 'E': -7, 'D': -7, 'G': -7, 'F': 0, 'I': -5, 'H': -3, 'K': -3, 'M': -4, 'L': -2, 'N': -4, 'Q': -5, 'P': -6, 'S': -2, 'R': 2, 'T': -5, 'W': 17, 'V': -6, 'Y': 0}, 'V': {'A': 0, 'C': -2, 'E': -2, 'D': -2, 'G': -1, 'F': -1, 'I': 4, 'H': -2, 'K': -2, 'M': 2, 'L': 2, 'N': -2, 'Q': -2, 'P': -1, 'S': -1, 'R': -2, 'T': 0, 'W': -6, 'V': 4, 'Y': -2}, 'Y': {'A': -3, 'C': 0, 'E': -4, 'D': -4, 'G': -5, 'F': 7, 'I': -1, 'H': 0, 'K': -4, 'M': -2, 'L': -1, 'N': -2, 'Q': -4, 'P': -5, 'S': -3, 'R': -4, 'T': -3, 'W': 0, 'V': -2, 'Y': 10}}
blosum62 = {'A': {'A': 4, 'C': 0, 'E': -1, 'D': -2, 'G': 0, 'F': -2, 'I': -1, 'H': -2, 'K': -1, 'M': -1, 'L': -1, 'N': -2, 'Q': -1, 'P': -1, 'S': 1, 'R': -1, 'T': 0, 'W': -3, 'V': 0, 'Y': -2}, 'C': {'A': 0, 'C': 9, 'E': -4, 'D': -3, 'G': -3, 'F': -2, 'I': -1, 'H': -3, 'K': -3, 'M': -1, 'L': -1, 'N': -3, 'Q': -3, 'P': -3, 'S': -1, 'R': -3, 'T': -1, 'W': -2, 'V': -1, 'Y': -2}, 'E': {'A': -1, 'C': -4, 'E': 5, 'D': 2, 'G': -2, 'F': -3, 'I': -3, 'H': 0, 'K': 1, 'M': -2, 'L': -3, 'N': 0, 'Q': 2, 'P': -1, 'S': 0, 'R': 0, 'T': -1, 'W': -3, 'V': -2, 'Y': -2}, 'D': {'A': -2, 'C': -3, 'E': 2, 'D': 6, 'G': -1, 'F': -3, 'I': -3, 'H': -1, 'K': -1, 'M': -3, 'L': -4, 'N': 1, 'Q': 0, 'P': -1, 'S': 0, 'R': -2, 'T': -1, 'W': -4, 'V': -3, 'Y': -3}, 'G': {'A': 0, 'C': -3, 'E': -2, 'D': -1, 'G': 6, 'F': -3, 'I': -4, 'H': -2, 'K': -2, 'M': -3, 'L': -4, 'N': 0, 'Q': -2, 'P': -2, 'S': 0, 'R': -2, 'T': -2, 'W': -2, 'V': -3, 'Y': -3}, 'F': {'A': -2, 'C': -2, 'E': -3, 'D': -3, 'G': -3, 'F': 6, 'I': 0, 'H': -1, 'K': -3, 'M': 0, 'L': 0, 'N': -3, 'Q': -3, 'P': -4, 'S': -2, 'R': -3, 'T': -2, 'W': 1, 'V': -1, 'Y': 3}, 'I': {'A': -1, 'C': -1, 'E': -3, 'D': -3, 'G': -4, 'F': 0, 'I': 4, 'H': -3, 'K': -3, 'M': 1, 'L': 2, 'N': -3, 'Q': -3, 'P': -3, 'S': -2, 'R': -3, 'T': -1, 'W': -3, 'V': 3, 'Y': -1}, 'H': {'A': -2, 'C': -3, 'E': 0, 'D': -1, 'G': -2, 'F': -1, 'I': -3, 'H': 8, 'K': -1, 'M': -2, 'L': -3, 'N': 1, 'Q': 0, 'P': -2, 'S': -1, 'R': 0, 'T': -2, 'W': -2, 'V': -3, 'Y': 2}, 'K': {'A': -1, 'C': -3, 'E': 1, 'D': -1, 'G': -2, 'F': -3, 'I': -3, 'H': -1, 'K': 5, 'M': -1, 'L': -2, 'N': 0, 'Q': 1, 'P': -1, 'S': 0, 'R': 2, 'T': -1, 'W': -3, 'V': -2, 'Y': -2}, 'M': {'A': -1, 'C': -1, 'E': -2, 'D': -3, 'G': -3, 'F': 0, 'I': 1, 'H': -2, 'K': -1, 'M': 5, 'L': 2, 'N': -2, 'Q': 0, 'P': -2, 'S': -1, 'R': -1, 'T': -1, 'W': -1, 'V': 1, 'Y': -1}, 'L': {'A': -1, 'C': -1, 'E': -3, 'D': -4, 'G': -4, 'F': 0, 'I': 2, 'H': -3, 'K': -2, 'M': 2, 'L': 4, 'N': -3, 'Q': -2, 'P': -3, 'S': -2, 'R': -2, 'T': -1, 'W': -2, 'V': 1, 'Y': -1}, 'N': {'A': -2, 'C': -3, 'E': 0, 'D': 1, 'G': 0, 'F': -3, 'I': -3, 'H': 1, 'K': 0, 'M': -2, 'L': -3, 'N': 6, 'Q': 0, 'P': -2, 'S': 1, 'R': 0, 'T': 0, 'W': -4, 'V': -3, 'Y': -2}, 'Q': {'A': -1, 'C': -3, 'E': 2, 'D': 0, 'G': -2, 'F': -3, 'I': -3, 'H': 0, 'K': 1, 'M': 0, 'L': -2, 'N': 0, 'Q': 5, 'P': -1, 'S': 0, 'R': 1, 'T': -1, 'W': -2, 'V': -2, 'Y': -1}, 'P': {'A': -1, 'C': -3, 'E': -1, 'D': -1, 'G': -2, 'F': -4, 'I': -3, 'H': -2, 'K': -1, 'M': -2, 'L': -3, 'N': -2, 'Q': -1, 'P': 7, 'S': -1, 'R': -2, 'T': -1, 'W': -4, 'V': -2, 'Y': -3}, 'S': {'A': 1, 'C': -1, 'E': 0, 'D': 0, 'G': 0, 'F': -2, 'I': -2, 'H': -1, 'K': 0, 'M': -1, 'L': -2, 'N': 1, 'Q': 0, 'P': -1, 'S': 4, 'R': -1, 'T': 1, 'W': -3, 'V': -2, 'Y': -2}, 'R': {'A': -1, 'C': -3, 'E': 0, 'D': -2, 'G': -2, 'F': -3, 'I': -3, 'H': 0, 'K': 2, 'M': -1, 'L': -2, 'N': 0, 'Q': 1, 'P': -2, 'S': -1, 'R': 5, 'T': -1, 'W': -3, 'V': -3, 'Y': -2}, 'T': {'A': 0, 'C': -1, 'E': -1, 'D': -1, 'G': -2, 'F': -2, 'I': -1, 'H': -2, 'K': -1, 'M': -1, 'L': -1, 'N': 0, 'Q': -1, 'P': -1, 'S': 1, 'R': -1, 'T': 5, 'W': -2, 'V': 0, 'Y': -2}, 'W': {'A': -3, 'C': -2, 'E': -3, 'D': -4, 'G': -2, 'F': 1, 'I': -3, 'H': -2, 'K': -3, 'M': -1, 'L': -2, 'N': -4, 'Q': -2, 'P': -4, 'S': -3, 'R': -3, 'T': -2, 'W': 11, 'V': -3, 'Y': 2}, 'V': {'A': 0, 'C': -1, 'E': -2, 'D': -3, 'G': -3, 'F': -1, 'I': 3, 'H': -3, 'K': -2, 'M': 1, 'L': 1, 'N': -3, 'Q': -2, 'P': -2, 'S': -2, 'R': -3, 'T': 0, 'W': -3, 'V': 4, 'Y': -1}, 'Y': {'A': -2, 'C': -2, 'E': -2, 'D': -3, 'G': -3, 'F': 3, 'I': -1, 'H': 2, 'K': -2, 'M': -1, 'L': -1, 'N': -2, 'Q': -1, 'P': -3, 'S': -2, 'R': -2, 'T': -2, 'W': 2, 'V': -1, 'Y': 7}}

sigma = -11
epsilon = -1
indel_penalty = -5

def AffineGapPenalties(v, w):
	lower = []
	middle = []
	upper = []
	p = len(v)
	q = len(w)
	lower, middle, upper = [[0 for x in xrange(q+1)] for x in xrange(p+1)], [[0 for x in xrange(q+1)] for x in xrange(p+1)], [[0 for x in xrange(q+1)] for x in xrange(p+1)]  
	for i in range(1, p+1):
		lower[i][0] = sigma + (i-1)*epsilon
		middle[i][0] = sigma + (i-1)*epsilon
		upper[i][0] = float('-inf')
	for j in range(1, q+1):
		upper[0][j] = sigma + (j-1)*epsilon
		middle[0][j] = sigma + (j-1)*epsilon
		lower[0][j] = float('-inf')

	for i in range(1, p+1):
	    for j in range(1, q+1):
	        lower[i][j] = max(lower[i-1][j] + epsilon, middle[i-1][j] + sigma)
	        upper[i][j] = max(upper[i][j-1] + epsilon, middle[i][j-1] + sigma)
	        middle[i][j] = max(lower[i][j], middle[i-1][j-1] + blosum62[v[i-1]][w[j-1]], upper[i][j])
				
	k = []
	l = []
	i = len(v)
	j = len(w)
	score = max(lower[i][j], middle[i][j], upper[i][j])
	current = []
	if score == lower[i][j]:
		current = lower
	elif score == middle[i][j]:
		current = middle
	else:
		current = upper
	#return lower, middle, upper

	while i > 0 and j > 0:
		if current == lower:
			#print('L', i, j)
			#print(k[::-1], l[::-1])
			if lower[i][j] == lower[i-1][j] + epsilon:
				k.append(v[i-1])
				l.append('-')
				i -= 1
				current = lower
			elif lower[i][j] == middle[i-1][j] + sigma:
				k.append(v[i-1])
				l.append('-')
				i -= 1
				current = middle
		elif current == middle:
			#print('M', i, j)
			#print(k[::-1], l[::-1])
			if middle[i][j] == lower[i][j]:
				current = lower
			elif middle[i][j] == middle[i-1][j-1] + blosum62[v[i-1]][w[j-1]]:
				k.append(v[i-1])
				l.append(w[j-1])
				i -= 1
				j -= 1
				current = middle
			elif middle[i][j] == upper[i][j]:
				current = upper
		elif current == upper:
			#print('U', i, j)
			#print(k[::-1], l[::-1])
			if upper[i][j] == upper[i][j-1] + epsilon:
				k.append('-')
				l.append(w[j-1])
				j -= 1
				current = upper
			elif upper[i][j] == middle[i][j-1] + sigma:
				k.append('-')
				l.append(w[j-1])
				j -= 1
				current = middle

	while i > 0:
		k.append(v[i-1])
		l.append('-')
		i -= 1
	while j > 0:
		k.append('-')
		l.append(w[j-1])
		j -= 1

	k = ''.join(k[::-1])
	l = ''.join(l[::-1])

	return score, k , l

def MiddlePath(v, w):
	s = []
	p = len(v)
	q = len(w)
	s = [[0 for x in xrange(q+1)] for x in xrange(p+1)] 

	for i in range(1, p+1):
		s[i][0] = i*indel_penalty
	for j in range(1, q+1):
		s[0][j] = j*indel_penalty

	for i in range(1, p+1):
	    for j in range(1, q+1):
	    	s[i][j] = max(s[i-1][j-1] + blosum62[v[i-1]][w[j-1]], s[i-1][j] + indel_penalty, s[i][j-1] + indel_penalty)

	i = p
	j = q
	#print(s)
	if j%2 == 0:
		res = []
		m1 = i//2
		m2 = i//2 -1 
		#print(m1, m2)
		while i > 0 and j > 0:
			if s[i][j] == s[i-1][j-1] + blosum62[v[i-1]][w[j-1]]: 
				if j == m1 and (j - 1) == m2:
					res.append((i-1, m2))
					res.append((i, m1))
					return 'diagonal', m2
				i -= 1
				j -= 1
			elif s[i][j] == s[i-1][j] + indel_penalty:
				if j == m1:
					res.append((i, m1))
					res.append((i-1, m1))
					return 'up', m1
				i -= 1
			elif s[i][j] == s[i][j-1] + indel_penalty:
				if j == m1:
					res.append((i, m1))
					res.append((i, m2))
					return 'side', m2
				j -= 1
		return res
	else:
		res = []
		m = j//2
		#print(m)
		while i > 0 and j > 0:
			if s[i][j] == s[i-1][j-1] + blosum62[v[i-1]][w[j-1]]: 
				if j == m+1:
					res.append((i-1, j-1))
					res.append((i, j))
					return 'diagonal', j-1
				i -= 1
				j -= 1
			elif s[i][j] == s[i-1][j] + indel_penalty:
				if j == m:
					res.append((i-1, j))
					res.append((i, j))
					return 'up', j
				i -= 1
			elif s[i][j] == s[i][j-1] + indel_penalty:
				if j == m+1:
					res.append((i, j-1))
					res.append((i, j))
					return 'side', j-1
				j -= 1

def MultipleSequenceAlignment(v, w, x):
	score = 0
	s = []
	p = len(v)
	q = len(w)
	r = len(x)
	for i in range(0, p+1):
		s.append([])
		for j in range(0, q+1):
			s[i].append([])
			for k in range(0, r+1):
				s[i][j].append(0)

	for i in range(1, p+1):
	    for j in range(1, q+1):
	    	for k in range(1, r+1):
	    		if v[i-1] == w[j-1] == x[k-1]:
	    			score = 1
	    		else:
	    			score = 0
	    		s[i][j][k] = max(s[i-1][j][k], s[i][j-1][k], s[i][j][k-1], s[i-1][j-1][k], s[i-1][j][k-1], s[i][j-1][k-1], s[i-1][j-1][k-1] + score)
				
	a = []
	b = []
	c =[]
	i = len(v)
	j = len(w)
	k = len(x)
	#return s
	while i > 0 and j > 0 and k > 0:
		if v[i-1] == w[j-1] == x[k-1]:
			score = 1
		else:
			score = 0
		if s[i][j][k] == s[i-1][j-1][k-1] + score: 
			a.append(v[i-1])
			b.append(w[j-1])
			c.append(x[k-1])
			i -= 1
			j -= 1
			k -= 1
		elif s[i][j][k] == s[i][j-1][k-1]:
			a.append('-')
			b.append(w[j-1])
			c.append(x[k-1])
			j -= 1
			k -= 1
		elif s[i][j][k] == s[i-1][j][k-1]:
			a.append(v[i-1])
			b.append('-')
			c.append(x[k-1])
			i -= 1
			k -= 1
		elif s[i][j][k] == s[i-1][j-1][k]:
			a.append(v[i-1])
			b.append(w[j-1])
			c.append('-')
			i -= 1
			j -= 1
		elif s[i][j][k] == s[i][j][k-1]:
			a.append('-')
			b.append('-')
			c.append(x[k-1])
			k -= 1
		elif s[i][j][k] == s[i][j-1][k]:
			a.append('-')
			b.append(w[j-1])
			c.append('-')
			j -= 1
		elif s[i][j][k] == s[i-1][j][k]:
			a.append(v[i-1])
			b.append('-')
			c.append('-')
			i -= 1
		

	while i > 0:
		a.append(v[i-1])
		b.append('-')
		c.append('-')
		i -= 1
	while j > 0:
		a.append('-')
		b.append(w[j-1])
		c.append('-')
		j -= 1
	while k > 0:
		a.append('-')
		b.append('-')
		c.append(x[k-1])
		k -= 1


	a = ''.join(a[::-1])
	b = ''.join(b[::-1])
	c = ''.join(c[::-1])

	return s[p][q][r], a, b, c

v = 'GGATATGG'
w = 'GGCACCTCCA'
x = 'GTGCAATTTT'
score, a, b, c = MultipleSequenceAlignment(v, w, x)
print(score)
print(a)
print(b)
print(c)