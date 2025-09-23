R=range
L=len
def p(g):
	for D in R(4):
		g=list(map(list,zip(*g[::-1])))
		for A in R(L(g)):
			if len(set(g[A]))>2:B=[A for A in g[A]if A>0];C=g[A].index(B[0])%L(B);g[A]=B[-C:]+B*20;g[A]=g[A][:L(g[0])]
	return g