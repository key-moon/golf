def p(g):
	G=sum(g,[]);H=next(A for A in G if G.count(A)<2);A,B=len(g),len(g[0]);D,E=next((A,C)for(A,B)in enumerate(g)for(C,D)in enumerate(B)if D==H);I=max((0,1),(0,-1),(1,0),(-1,0),key=lambda t:sum(0<=D+t[0]*C<A and 0<=E+t[1]*C<B and g[D+t[0]*C][E+t[1]*C]==0 for C in range(1,A+B)))
	for J in range(1,A+B):
		C,F=D+I[0]*J,E+I[1]*J
		if 0<=C<A and 0<=F<B and g[C][F]==0:g[C][F]=H
	return g