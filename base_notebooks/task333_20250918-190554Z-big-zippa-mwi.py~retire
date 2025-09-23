L=len
R=range
def p(g):
	for F in range(4):
		g=list(map(list,zip(*g[::-1])));D,G=L(g),L(g[0])
		for A in R(D):
			if 3 in g[A]:
				C=g[A].index(3);B=max(g[A][:C])
				if B>0:
					for E in R(g[A].index(B),C):g[A][E]=B
	return g