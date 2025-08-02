def p(g):
	I,G=len(g),len(g[0]);from collections import Counter as a,deque;b=a(B for A in g for B in A);J=b.most_common(1)[0][0];H=[[0]*G for A in g];K=[]
	for A in range(I):
		for B in range(G):
			if g[A][B]!=J and not H[A][B]:
				C=g[A][B];L=deque([(A,B)]);H[A][B]=1;M,N=[],[]
				while L:
					W,X=L.popleft();M.append(W);N.append(X)
					for(O,P)in((1,0),(-1,0),(0,1),(0,-1)):
						E,F=W+O,X+P
						if 0<=E<I and 0<=F<G and not H[E][F]and g[E][F]==C:H[E][F]=1;L.append((E,F))
				Q,R=min(M),max(M);S,T=min(N),max(N);K.append((C,Q,R,S,T))
	c=I/2;d=G/2;K.sort(key=lambda x:(x[1]+x[2]<2*c,x[3]+x[4]<2*d));U=[]
	for(C,Q,R,S,T)in K:V=[A[S+1:T]for A in g[Q+1:R]];U.append((C,V))
	D=len(U[0][1]);Y=[[J]*(2*D+1)for A in range(2*D+1)]
	for(Z,(C,V))in enumerate(U):
		O=Z//2*(D+1);P=Z%2*(D+1)
		for A in range(D):
			for B in range(D):
				if V[A][B]!=J:Y[O+1+A][P+1+B]=C
	return Y