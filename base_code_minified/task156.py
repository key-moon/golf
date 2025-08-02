def p(g):
	J,K=len(g),len(g[0]);E=set();L=[]
	for F in range(J):
		for G in range(K):
			if g[F][G]==4 and(F,G)not in E:
				A=[(F,G)];E.add((F,G));B=0
				while B<len(A):
					H,I=A[B];B+=1
					for(C,D)in((H+1,I),(H-1,I),(H,I+1),(H,I-1)):
						if 0<=C<J and 0<=D<K and g[C][D]==4 and(C,D)not in E:E.add((C,D));A.append((C,D))
				M=min(A[0]for A in A);N=max(A[0]for A in A);O=min(A[1]for A in A);P=max(A[1]for A in A);L.append([(A,B)for A in range(M+1,N)for B in range(O+1,P)])
	for(B,Q)in enumerate(sorted(L,key=len)):
		for(R,S)in Q:g[R][S]=B+1
	return g