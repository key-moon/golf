R=range
L=len
def p(g):
	C=sum(g,[]).count(5);D=[A for A in R(L(g))if g[A].count(0)==0][0];E=g[D][0];F=g[0].index(E)
	for A in R(L(g)):
		for B in R(L(g[0])):
			if A==D+C or B==F-C:g[A][B]=E
			else:g[A][B]=0
	return g