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



x = '-1 +2 +3 -4 +5 -6 -7 +8 +9 +10 -11 -12 +13 -14 +15 +16 +17 +18 -19 -20 -21 -22 +23 -24 -25 +26 +27 +28 -29 -30 +31 -32 +33 +34 -35 -36 +37 +38 +39 -40 -41 -42 -43 -44 -45 -46 +47 -48 -49 +50 +51 -52 -53 -54 +55 -56 +57 -58 +59 +60 -61 -62 +63 -64 -65'
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
