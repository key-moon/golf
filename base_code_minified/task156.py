def p(A):
	K,L=len(A),len(A[0]);F=set();M=[]
	for G in range(K):
		for H in range(L):
			if A[G][H]==4 and(G,H)not in F:
				B=[(G,H)];F.add((G,H));C=0
				while C<len(B):
					I,J=B[C];C+=1
					for(D,E)in((I+1,J),(I-1,J),(I,J+1),(I,J-1)):
						if 0<=D<K and 0<=E<L and A[D][E]==4 and(D,E)not in F:F.add((D,E));B.append((D,E))
				N=min(A[0]for A in B);O=max(A[0]for A in B);P=min(A[1]for A in B);Q=max(A[1]for A in B);M.append([(A,B)for A in range(N+1,O)for B in range(P+1,Q)])
	for(C,R)in enumerate(sorted(M,key=len)):
		for(S,T)in R:A[S][T]=C+1
	return A