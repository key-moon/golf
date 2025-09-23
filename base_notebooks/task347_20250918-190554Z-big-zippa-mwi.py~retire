def p(j,A=range(3)):
	for B in A:
		for C in A:
			j[B][C]+=j[B][C+3]
			if j[B][C]>0:j[B][C]=6
	return[A[:3]for A in j]