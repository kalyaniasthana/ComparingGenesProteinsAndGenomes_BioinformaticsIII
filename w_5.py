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

def ColoredEdges(P):
	edges = []
	for chromosome in P:
		nodes = ChromosomeToCycle(chromosome)
		i = 1
		while i < len(nodes) - 2:
			edges.append((nodes[i], nodes[i+1]))
			i += 2
		edges.append((nodes[len(nodes) - 1], nodes[0]))

	return edges


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
'''
x = '2 1 3 4 6 5 8 7 9 10 12 11 13 14 15 16 18 17 19 20 22 21 23 24 25 26 28 27 29 30 31 32 34 33 36 35 38 37 39 40 42 41 44 43 46 45 47 48 49 50 52 51 53 54 56 55 57 58 60 59 61 62 64 63 66 65 68 67 69 70 72 71 73 74 75 76 77 78 80 79 81 82 84 83 86 85 88 87 89 90 92 91 93 94 96 95 97 98 99 100 101 102 104 103 105 106 108 107 110 109 112 111 114 113 115 116 118 117 119 120 122 121'
x = x.split(' ')
nodes = [int(i) for i in x]
print(Format(CycleToChromosome(nodes)))
''' 
x = '-1 -2 +3 +4 +5 +6 +7 +8 -9 -10 +11 -12 +13 +14 -15 +16 +17 -18 +19 +20 +21 -22 +23 +24 +25 -26 -27 -28 +29 +30)(-31 -32 -33 -34 -35 +36 +37 +38 -39 -40 -41 -42 +43 +44 +45 +46 -47 +48 -49 -50 +51 +52 +53 +54 -55 -56 -57 +58 +59 +60 -61)(+62 -63 +64 -65 +66 +67 -68 +69 +70 +71 +72 -73 -74 +75 +76 +77 -78 +79 +80 -81 -82 +83 +84 -85 +86)(-87 -88 +89 +90 -91 -92 -93 +94 -95 +96 +97 +98 +99 +100 +101 +102 +103 +104 +105 +106 -107 -108 -109 -110 +111)(-112 -113 -114 +115 -116 +117 -118 -119 -120 -121 -122 -123 +124 +125 +126 +127 -128 -129 -130 -131 -132 +133 -134 +135)(+136 -137 +138 +139 +140 +141 +142 -143 -144 +145 -146 -147 +148 +149 +150 +151 -152 -153 -154 +155 -156 -157 +158 +159 +160 +161 +162 +163 -164)(-165 -166 -167 +168 -169 -170 +171 -172 -173 +174 -175 -176 -177 +178 +179 -180 -181 +182 +183 -184 +185 +186 +187 -188 +189 -190)(-191 -192 -193 +194 -195 -196 -197 +198 -199 +200 +201 +202 +203 +204 -205 +206 +207 +208 +209 +210 +211 -212 -213 -214'
x = x.split(')(')
for i in range(0, len(x)):
	l = []
	item = x[i].split(' ')
	for num in item:
		if num[0] == '-':
			num = -1*int(num[1:])
			l.append(num)
		else:
			num = int(num[1:])
			l.append(num)
	x[i] = l
print(ColoredEdges(x))

