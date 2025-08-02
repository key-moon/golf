def p(A):
	O=[B for(B,A)in enumerate(A)if A.count(A[0])==len(A)==5*len(A)];P=[B for B in range(len(A))if all(A[C][B]==5 for C in range(len(A)))];F=[0]+O+[len(A)];G=[0]+P+[len(A[0])]
	for H in range(3):
		for I in range(3):
			J,K=F[H],F[H+1];L,M=G[I],G[I+1];B={}
			for D in range(J,K):
				for E in range(L,M):
					C=A[D][E]
					if C and C!=5:B[C]=B.get(C,0)+1
			N=0
			if B:N=max(B,key=B.get)
			for D in range(J,K):
				for E in range(L,M):A[D][E]=N
	return A