from collections import deque
def p(A):
	G,D=len(A),len(A[0])
	for b in A:
		for W in b:
			if W:P=W;break
		else:continue
		break
	X=[]
	for B in range(G):
		for C in range(D):
			if A[B][C]==P and(B in(0,G-1)or C in(0,D-1)):X.append((B,C))
	Q,R=X;H=deque([Q]);S={Q:None}
	while H:
		M,N=H.popleft()
		if(M,N)==R:break
		for(T,U)in((1,0),(-1,0),(0,1),(0,-1)):
			E,F=M+T,N+U
			if 0<=E<G and 0<=F<D and(E,F)not in S and A[E][F]==P:S[E,F]=M,N;H.append((E,F))
	Y=set();O=R
	while O:Y.add(O);O=S[O]
	I=[(0,A)for A in range(D)]+[(A,D-1)for A in range(1,G)]+[(G-1,A)for A in range(D-2,-1,-1)]+[(A,0)for A in range(G-2,0,-1)];J,K=I.index(Q),I.index(R);Z=I[J:K+1]if J<=K else I[J:]+I[:K+1];a=I[K:J+1]if K<=J else I[K:]+I[:J+1];c=set(Z if len(Z)<len(a)else a);V=Y|c;L=[[0]*D for A in A];H=deque()
	for B in range(G):
		for C in(0,D-1):
			if(B,C)not in V:L[B][C]=1;H.append((B,C))
	for C in range(D):
		for B in(0,G-1):
			if(B,C)not in V and not L[B][C]:L[B][C]=1;H.append((B,C))
	while H:
		M,N=H.popleft()
		for(T,U)in((1,0),(-1,0),(0,1),(0,-1)):
			E,F=M+T,N+U
			if 0<=E<G and 0<=F<D and not L[E][F]and(E,F)not in V:L[E][F]=1;H.append((E,F))
	for B in range(G):
		for C in range(D):A[B][C]=5 if L[B][C]else P
	return A