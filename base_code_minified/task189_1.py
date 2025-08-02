def p(g):
	for(A,D)in enumerate(g):
		if D.count(8)==len(D):break
	for(B,E)in enumerate(zip(*g)):
		if E.count(8)==len(E):break
	F=[[A[:B]for A in g[:A]],[A[B+1:]for A in g[:A]],[A[:B]for A in g[A+1:]],[A[B+1:]for A in g[A+1:]]];I=next(A for A in F if len(A)==2 and len(A[0])==2);C=next(A for A in F if len(A)>2 and len(A[0])>2);G,H=len(C),len(C[0]);J,K=G//2,H//2;return[[C[A][B]//3*I[A//J][B//K]for B in range(H)]for A in range(G)]