def p(g):
	C=len(g);D,E=min((A,B)for A in range(C)for B in range(C)if g[A][B]==1);F,G=min((A,B)for A in range(C)for B in range(C)if g[A][B]==2);A,B=D,E
	while A and B:A-=1;B-=1;g[A][B]=1
	A,B=F+1,G+1
	while A<C-1 and B<C-1:A+=1;B+=1;g[A][B]=2
	return g