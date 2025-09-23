def p(j,A=range(9),c=range(3)):
	D,C=__import__('collections').Counter(j[0]+j[1]+j[2]).most_common(1)[0][0],[[0 for A in A]for B in A]
	for(E,F)in[(B,A)for A in c for B in c if j[B][A]==D]:
		for B in A:C[3*E+B%3][3*F+B//3]=j[B%3][B//3]
	return C