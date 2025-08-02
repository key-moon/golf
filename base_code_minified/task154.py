def p(g):
	J,K=len(g),len(g[0]);F=[(A,B)for A in range(J)for B in range(K)if g[A][B]==2];S=min(A for(A,B)in F);T=max(A for(A,B)in F);U=min(A for(B,A)in F);V=max(A for(B,A)in F);L=[(A,B)for A in range(J)for B in range(K)if g[A][B]==5];G=set(L);M=[]
	while G:
		A,B=G.pop();I=[(A,B)];C=[(A,B)]
		while I:
			W,X=I.pop()
			for(D,E)in((1,0),(-1,0),(0,1),(0,-1)):
				H=W+D,X+E
				if H in G:G.remove(H);I.append(H);C.append(H)
		M.append(C)
	for(A,B)in L:g[A][B]=0
	for C in M:
		N=[A for(A,B)in C];O=[A for(B,A)in C];Y,Z=S+1-min(N),T-1-max(N);a,b=U+1-min(O),V-1-max(O);P=10**9
		for D in range(Y,Z+1):
			for E in range(a,b+1):
				Q=1
				for(A,B)in C:
					if g[A+D][B+E]!=0:Q=0;break
				if Q:
					R=abs(D)+abs(E)
					if R<P:P=R;c,d=D,E
		for(A,B)in C:g[A+c][B+d]=5
	return g