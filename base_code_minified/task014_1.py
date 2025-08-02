def p(A):
	B,C=len(A),len(A[0]);E=[A for(A,B)in enumerate(A)if B.count(0)==C];J,D=E[0],E[-1];F=[C for C in range(C)if all(A[B][C]==0 for B in range(B))];G,K=F[0],F[-1];L={B for C in range(J)for B in A[C]if B};M={B for C in range(D+1,B)for B in A[C]if B};N=(M-L).pop()
	if any(A[B][C]==N for B in range(D+1,B)for C in range(G)):H,I=0,G
	else:H,I=K+1,C
	return[A[H:I]for A in A[D+1:B]]