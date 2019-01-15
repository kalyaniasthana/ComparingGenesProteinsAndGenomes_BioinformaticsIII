from __future__ import print_function, division

def Format(l):
	temp = []
	for num in l:
		if num > 0:
			temp.append('+' + str(num))
		else:
			temp.append(str(num))
	line = ' '.join(temp)
	line = '(' + line + ')\n' 
	return line

def GreedySorting(l):
	file = open('GreedySorting.txt', 'w')
	reversal_distance = 0
	m = len(l)
	indentity = [i+1 for i in range(0, m)]
	
	for i in range(0, m):
		start = i
		if l[start] != indentity[start]:
			if indentity[start] in l:
				end = l.index(indentity[start])
			else:
				end = l.index(-1*(indentity[start]))
			sub = l[start: end+1][::-1]
			sub = [-j for j in sub]
			l[start: end+1] = sub
			#print(tuple(l))
			line = Format(l)	
			file.write(line)
			reversal_distance += 1
		if l[start] < 0:
			l[start] *= -1
			reversal_distance += 1
			#print(tuple(l))
			line = Format(l)
			file.write(line)

	return reversal_distance


x = '+63 +91 -6 +74 +41 -79 -111 -104 -50 +77 -37 +119 -22 +4 -20 +109 -12 -65 -25 +16 -82 +31 -49 +67 +116 +43 -123 +53 +40 -100 +117 -14 -59 -56 -88 +29 +99 +103 +70 +17 +98 +19 +128 -83 -114 +13 -102 +84 +113 +55 -36 -93 +96 +97 -72 -9 -21 -81 +46 -39 -24 -23 +130 -38 +124 -125 +90 -64 -95 +2 +60 +66 -73 -75 -106 +51 +11 +42 +68 -52 -107 +92 +127 -126 +89 +108 -48 +69 -8 -120 +45 +30 +105 +129 -5 +1 -7 +44 +58 -94 +35 -47 -54 -115 +57 -112 -101 -15 -62 -32 -76 -10 -86 +121 +118 -34 -110 +71 -3 -33 -87 +27 -61 +26 +80 -78 -28 -122 +85 -18'
x = x.split(' ')
l = []
for num in x:
	if num[0] == '-':
		num = -1*int(num[1:])
		l.append(num)
	else:
		num = int(num[1:])
		l.append(num)

print(GreedySorting(l))