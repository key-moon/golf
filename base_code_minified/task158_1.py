def p(g):
	F,G=len(g),len(g[0]);M=[B for A in g for B in A];N=max(set(M),key=M.count);H=[[0]*G for A in range(F)];O=[]
	for B in range(F):
		for C in range(G):
			if g[B][C]!=N and not H[B][C]:
				I=[(B,C)];H[B][C]=1;D=[]
				while I:
					P,Q=I.pop();D.append((P,Q))
					for(U,V)in((1,0),(-1,0),(0,1),(0,-1)):
						E,A=P+U,Q+V
						if 0<=E<F and 0<=A<G and not H[E][A]and g[E][A]!=N:H[E][A]=1;I.append((E,A))
				O.append(D)
	for D in O:
		W={g[A][B]for(A,B)in D}
		if len(W)>1:break
	X=[A for(A,B)in D];Y=[A for(B,A)in D];R,S=min(X),min(Y);J=[(A-R,B-S,g[A][B])for(A,B)in D];T={}
	for(K,L,A)in J:T.setdefault(A,[]).append((K,L))
	for(A,Z)in T.items():
		a=min(Z);b,c=a
		for B in range(F):
			for C in range(G):
				if g[B][C]==A and(B-R,C-S,A)not in J:
					d,e=B-b,C-c
					for(K,L,f)in J:g[d+K][e+L]=f
	return g