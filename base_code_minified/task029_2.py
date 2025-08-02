def p(g):
	D=[]
	for(G,C)in enumerate(g):
		B=0;E=0;A=1
		for F in range(1,len(C)):
			if C[F]==C[F-1]:A+=1
			else:
				if A>B:B,E=A,F-A
				A=1
		if A>B:B,E=A,len(C)-A
		if B>1:D.append((G,E,B))
	H=max(A[2]for A in D);I,J=[A for A in D if A[2]==H];K,L,M=I;N,O,M=J;return[A[L+1:O]for A in g[K+1:N]]