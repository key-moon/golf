def p(A):
	J,K=len(A),len(A[0]);E=[(B,C)for B in range(J)for C in range(K)if A[B][C]==5];F,G=min(A for(A,B)in E),max(A for(A,B)in E);H,I=min(A for(B,A)in E),max(A for(B,A)in E);D=[[0]*K for A in range(J)]
	for B in range(F,G+1):
		for C in range(H,I+1):D[B][C]=5
	M=G-F>I-H
	for B in range(J):
		for C in range(K):
			L=A[B][C]
			if L and L!=5:
				if M:
					if B<F:D[F-1][C]=5
					if B>G:D[G+1][C]=5
				else:
					if C<H:D[B][H-1]=5
					if C>I:D[B][I+1]=5
	return D