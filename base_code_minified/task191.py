def p(A):
	C=[(B,C)for B in range(len(A))for C in range(len(A[0]))if A[B][C]];D,M=min(A for(A,B)in C),max(A for(A,B)in C);E,N=min(A for(B,A)in C),max(A for(B,A)in C);B=[A[E:N+1]for A in A[D:M+1]];O=[(A,C)for A in range(len(B))for C in range(len(B[0]))if B[A][C]==4];I,J=O[0];P,Q=len(B),len(B[0])
	for F in range(len(A)):
		for G in range(len(A[0])):
			if A[F][G]==4 and not(D+I==F and E+J==G):
				R,S=F-(D+I),G-(E+J)
				for K in range(P):
					for L in range(Q):
						H=B[K][L]
						if H:A[R+K][S+L]=H if H==4 else 1
	return A