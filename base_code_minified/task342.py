def p(A):
	B,C=sorted((B,C)for B in range(10)for C in range(10)if A[B][C]==8)[0];D=sorted((B,C,G)for B in range(10)for C in range(10)if(G:=A[B][C])%8);E=sorted(D[:2],key=lambda G:G[1]);F=sorted(D[2:],key=lambda G:G[1])
	for H in range(10):A[H]=[0]*10
	A[B][C],A[B][C+1]=E[0][2],E[1][2];A[B+1][C],A[B+1][C+1]=F[0][2],F[1][2];return A