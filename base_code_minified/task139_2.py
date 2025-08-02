def p(A):
	D=set();I=len(A);J=len(A[0]);K=(1,0),(-1,0),(0,1),(0,-1)
	for E in range(I):
		for F in range(J):
			if A[E][F]==4 and(E,F)not in D:
				C=[(E,F)];D.add((E,F))
				for(G,H)in C:
					for(L,M)in K:
						B=G+L,H+M
						if B not in D and 0<=B[0]<I and 0<=B[1]<J and A[B[0]][B[1]]==4:D.add(B);C.append(B)
				N=min(A[0]for A in C);O=max(A[0]for A in C);P=min(A[1]for A in C);Q=max(A[1]for A in C)
				for G in range(N,O+1):
					for H in range(P,Q+1):
						if A[G][H]==0:A[G][H]=7
	return A