def p(A):
	B={}
	for G in A:
		for(D,C)in enumerate(G):
			if C:B.setdefault(C,[0,D])[0]+=1;B[C][1]=min(B[C][1],D)
	E=max(A[0]for A in B.values());F=[A for(A,B)in B.items()if B[0]==E];F.sort(key=lambda E:B[E][1]);return[F]*E