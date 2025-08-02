from collections import deque
def p(g):
	F,C=len(g),len(g[0])
	for a in g:
		for V in a:
			if V:O=V;break
		else:continue
		break
	W=[]
	for A in range(F):
		for B in range(C):
			if g[A][B]==O and(A in(0,F-1)or B in(0,C-1)):W.append((A,B))
	P,Q=W;G=deque([P]);R={P:None}
	while G:
		L,M=G.popleft()
		if(L,M)==Q:break
		for(S,T)in((1,0),(-1,0),(0,1),(0,-1)):
			D,E=L+S,M+T
			if 0<=D<F and 0<=E<C and(D,E)not in R and g[D][E]==O:R[D,E]=L,M;G.append((D,E))
	X=set();N=Q
	while N:X.add(N);N=R[N]
	H=[(0,A)for A in range(C)]+[(A,C-1)for A in range(1,F)]+[(F-1,A)for A in range(C-2,-1,-1)]+[(A,0)for A in range(F-2,0,-1)];I,J=H.index(P),H.index(Q);Y=H[I:J+1]if I<=J else H[I:]+H[:J+1];Z=H[J:I+1]if J<=I else H[J:]+H[:I+1];b=set(Y if len(Y)<len(Z)else Z);U=X|b;K=[[0]*C for A in g];G=deque()
	for A in range(F):
		for B in(0,C-1):
			if(A,B)not in U:K[A][B]=1;G.append((A,B))
	for B in range(C):
		for A in(0,F-1):
			if(A,B)not in U and not K[A][B]:K[A][B]=1;G.append((A,B))
	while G:
		L,M=G.popleft()
		for(S,T)in((1,0),(-1,0),(0,1),(0,-1)):
			D,E=L+S,M+T
			if 0<=D<F and 0<=E<C and not K[D][E]and(D,E)not in U:K[D][E]=1;G.append((D,E))
	for A in range(F):
		for B in range(C):g[A][B]=5 if K[A][B]else O
	return g