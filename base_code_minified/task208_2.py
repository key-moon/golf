def p(g):
	F=sum(g,[]);H=max(set(F),key=F.count)
	for G in set(F)-{H}:
		A=[(A,C)for(A,B)in enumerate(g)for(C,D)in enumerate(B)if D==G]
		if(B:=max(A for(A,B)in A)-min(A for(A,B)in A)+1)*(C:=max(A for(B,A)in A)-min(A for(B,A)in A)+1)>len(A):J,K=min(A for(A,B)in A),min(A for(B,A)in A);break
	I=[(A,D)for A in range(B)for D in range(C)if A*(A-B+1)*D*(D-C+1)==0]
	for D in range(len(g)-B+1):
		for E in range(len(g[0])-C+1):
			if D==J and E==K:continue
			if all(g[D+A][E+B]==H for A in range(1,B-1)for B in range(1,C-1))and all(g[D+A][E+B]!=G for(A,B)in I):
				for(L,M)in I:g[D+L][E+M]=G
				return g
	return g