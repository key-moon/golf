def p(j):
	for A in range(4):
		for B in range(3):
			j[A][B]+=j[A][B+4]
			if j[A][B]>0:j[A][B]=0
			else:j[A][B]=3
	return[A[:3]for A in j]