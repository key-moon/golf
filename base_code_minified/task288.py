def p(g):
	A=len(g)-1;B=next(B for B in g[A]if B and B not in g[A-1]);D=[A for(A,C)in enumerate(g[A])if C==B];H,I=D[0],D[-1];J=len(g[0])
	for C in range(1,A):
		E=A-C-1;F=H-C
		if F>=0:g[E][F]=B
		G=I+C
		if G<J:g[E][G]=B
	return g