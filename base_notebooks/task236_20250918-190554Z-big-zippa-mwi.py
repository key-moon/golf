def p(j,A=range(4)):
	for B in A:
		for C in A:
			j[B][C]+=j[B+5][C]
			if j[B][C]==3:j[B][C]=0
			elif j[B][C]>0:j[B][C]=3
	return j[:4]