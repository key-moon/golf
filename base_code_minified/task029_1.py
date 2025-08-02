def p(g):
	D={};E=0
	for(G,C)in enumerate(g):
		A=0
		while A<len(C):
			B=A+1
			while B<len(C)and C[B]==C[A]:B+=1
			if B-A>1:D.setdefault((A,B),[]).append(G)
			A=B
	for((A,B),F)in D.items():
		if len(F)==2 and B-A>E:E,H,I,J,K=B-A,B,A,*sorted(F)
	return[A[I+1:H-1]for A in g[J+1:K]]