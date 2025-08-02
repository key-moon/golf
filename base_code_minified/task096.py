def p(g):
	Q,R=len(g),len(g[0]);M={}
	for c in g:
		for A in c:M[A]=M.get(A,0)+1
	F=max(M,key=M.get);N=[[0]*R for A in range(Q)];G=[]
	for C in range(Q):
		for E in range(R):
			if g[C][E]!=F and not N[C][E]:
				X=g[C][E];S=[(C,E)];N[C][E]=1;Y=[];O,T,P,U=C,C,E,E
				while S:
					B,A=S.pop();Y.append((B,A))
					if B<O:O=B
					if B>T:T=B
					if A<P:P=A
					if A>U:U=A
					for(d,e)in((1,0),(-1,0),(0,1),(0,-1)):
						H,I=B+d,A+e
						if 0<=H<Q and 0<=I<R and not N[H][I]and g[H][I]==X:N[H][I]=1;S.append((H,I))
				J=T-O+1;K=U-P+1;D=J if J>K else K;V=[[F]*K for A in range(J)]
				for(B,A)in Y:V[B-O][A-P]=X
				f=D-J;h=D-K;i=f//2;j=h//2;L=[[F]*D for A in range(D)]
				for B in range(J):
					for A in range(K):
						if V[B][A]!=F:L[i+B][j+A]=V[B][A]
				G.append((D,L))
	G.sort(key=lambda x:x[0]);Z=len(G)-1;W=G[0][0]+2*Z;k=W//2;a=[[F]*W for A in range(W)]
	for(C,(D,L))in enumerate(G):
		l=Z-C;b=k-D//2-l
		for B in range(D):
			for A in range(D):
				if L[B][A]!=F:a[b+B][b+A]=L[B][A]
	return a