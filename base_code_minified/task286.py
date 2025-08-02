def p(A):
	K,I=len(A),len(A[0]);D=[[-1]*I for A in A]
	for G in range(K):
		for H in range(I):
			if A[G][H]!=8 and D[G][H]<0:
				L={};J=[(G,H)];D[G][H]=0
				for(B,C)in J:
					M=D[B][C]
					if A[B][C]:L[M]=A[B][C]
					for(E,F)in((B+1,C),(B-1,C),(B,C+1),(B,C-1)):
						if 0<=E<K and 0<=F<I and A[E][F]!=8 and D[E][F]<0:D[E][F]=1-M;J.append((E,F))
				for(B,C)in J:A[B][C]=L[D[B][C]]
	return A