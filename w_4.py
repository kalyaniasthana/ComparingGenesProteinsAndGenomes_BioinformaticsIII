#from __future__ import print_function, division

def Format(l):
	temp = []
	for num in l:
		if num > 0:
			temp.append('+' + str(num))
		else:
			temp.append(str(num))
	line = ' '.join(temp)
	line = '(' + line + ')' 
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

def Breakpoints(l):
	num_of_breakpoints = 0
	for i in range(0, len(l) - 1):
		if l[i+1] - l[i] != 1:
			num_of_breakpoints += 1
	return num_of_breakpoints

'''
x = '+6 -12 -9 +17 +18 -4 +5 -3 +11 +19 +20 +10 +8 +15 -14 -13 +2 +7 -16 -1'
x = x.split(' ')
l = []
l.append(0)
for num in x:
	if num[0] == '-':
		num = -1*int(num[1:])
		l.append(num)
	else:
		num = int(num[1:])
		l.append(num)
l.append(len(l))
print(Breakpoints(l))
'''