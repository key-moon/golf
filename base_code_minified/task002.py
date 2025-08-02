def p(A):
	G,F=len(A),len(A[0]);D=[[0]*F for A in A];E=[(B,C)for B in(0,G-1)for C in range(F)if A[B][C]==0]+[(C,B)for B in(0,F-1)for C in range(G)if A[C][B]==0]
	for(B,C)in E:D[B][C]=1
	while E:
		B,C=E.pop()
		if B>0 and not D[B-1][C]and A[B-1][C]==0:D[B-1][C]=1;E.append((B-1,C))
		if B+1<G and not D[B+1][C]and A[B+1][C]==0:D[B+1][C]=1;E.append((B+1,C))
		if C>0 and not D[B][C-1]and A[B][C-1]==0:D[B][C-1]=1;E.append((B,C-1))
		if C+1<F and not D[B][C+1]and A[B][C+1]==0:D[B][C+1]=1;E.append((B,C+1))
	for B in range(G):
		for C in range(F):
			if A[B][C]==0 and not D[B][C]:A[B][C]=4
	return A