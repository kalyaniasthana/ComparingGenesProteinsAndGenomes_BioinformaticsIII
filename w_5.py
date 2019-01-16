from __future__ import print_function, division
from w_4 import *

def ChromosomeToCycle(l):
	nodes = []
	for i in range(0, len(l)):
		start = l[i]
		if start > 0:
			nodes.append(2*start - 1)
			nodes.append(2*start)
		else:
			nodes.append(-2*start)
			nodes.append(-2*start - 1)
	return nodes

def CycleToChromosome(nodes):
	l = []
	i = 0
	while i < len(nodes):
		if nodes[i] < nodes[i+1]:
			l.append(nodes[i+1]//2)
		else:
			l.append(-nodes[i+1]//2)
		i += 2
	return l




'''
x = '+1 -2 -3 +4'
x = x.split(' ')
l = []
for num in x:
	if num[0] == '-':
		num = -1*int(num[1:])
		l.append(num)
	else:
		num = int(num[1:])
		l.append(num)
		
nodes = ChromosomeToCycle(l)
nodes = [str(i) for i in nodes]
nodes = '(' + ' '.join(nodes) + ')'
print(nodes)
'''
x = '2 1 3 4 6 5 8 7 9 10 12 11 13 14 15 16 18 17 19 20 22 21 23 24 25 26 28 27 29 30 31 32 34 33 36 35 38 37 39 40 42 41 44 43 46 45 47 48 49 50 52 51 53 54 56 55 57 58 60 59 61 62 64 63 66 65 68 67 69 70 72 71 73 74 75 76 77 78 80 79 81 82 84 83 86 85 88 87 89 90 92 91 93 94 96 95 97 98 99 100 101 102 104 103 105 106 108 107 110 109 112 111 114 113 115 116 118 117 119 120 122 121'
x = x.split(' ')
nodes = [int(i) for i in x]
print(Format(CycleToChromosome(nodes)))
