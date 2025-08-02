def p(g):
	A,D=len(g),len(g[0]);C=lambda r,c:0<=r<A and 0<=c<D and g[r][c]>0
	while 1:
		B=[(A,B)for A in range(A)for B in range(D)if g[A][B]==0 and(C(A-1,B)and C(A,B-1)or C(A-1,B)and C(A,B+1)or C(A+1,B)and C(A,B-1)or C(A+1,B)and C(A,B+1))]
		if not B:break
		for(E,F)in B:g[E][F]=2
	return g