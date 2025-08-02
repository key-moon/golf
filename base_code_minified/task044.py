def p(A):
	J,K=len(A),len(A[0]);T=[];P=set()
	for E in range(J):
		for F in range(K):
			if A[E][F]==0 and(E,F)not in P:
				G=[(E,F)];D=[];U=True
				while G:
					B,C=G.pop()
					if(B,C)in P or not(0<=B<J and 0<=C<K)or A[B][C]!=0:continue
					P.add((B,C));D.append((B,C))
					if B in(0,J-1)or C in(0,K-1):U=False
					for(L,M)in((1,0),(-1,0),(0,1),(0,-1)):G.append((B+L,C+M))
				if U:T.append(D)
	N=[];Q=set()
	for E in range(J):
		for F in range(K):
			V=A[E][F]
			if V not in(0,5)and(E,F)not in Q:
				G=[(E,F)];D=[];H=V
				while G:
					B,C=G.pop()
					if(B,C)in Q or not(0<=B<J and 0<=C<K)or A[B][C]!=H:continue
					Q.add((B,C));D.append((B,C))
					for(L,M)in((1,0),(-1,0),(0,1),(0,-1)):G.append((B+L,C+M))
				N.append((H,D))
	def W(A):B=min(A for(A,B)in A);C=min(A for(B,A)in A);return set((A-B,D-C)for(A,D)in A),(B,C)
	X=[];Y=[]
	for a in T:R,I=W(a);X.append(R);Y.append(I)
	b=[];S=[];c=[]
	for(H,D)in N:R,I=W(D);S.append(R);c.append(I);b.append(H)
	Z=[None]*len(N)
	for(O,d)in enumerate(S):
		for(e,f)in enumerate(X):
			if d==f:Z[O]=e;break
	for(h,D)in N:
		for(B,C)in D:A[B][C]=0
	for(O,(H,D))in enumerate(N):
		g=1-Z[O];I=Y[g]
		for(L,M)in S[O]:A[I[0]+L][I[1]+M]=H
	return A