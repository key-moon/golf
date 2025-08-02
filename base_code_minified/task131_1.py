def p(A):
	E,F=len(A),len(A[0]);C=[(B,C)for B in range(E)for C in range(F)if A[B][C]==2];H=[(B,C)for B in range(E)for C in range(F)if A[B][C]==3];B=0 if all(A==C[0][0]for(A,B)in C)else 1;M=min(A[B]for A in C);P=max(A[B]for A in C);N=min(A[B]for A in H);I=max(A[B]for A in H)
	if I<M:D=M-1-I;J=N+D-1
	else:D=P+1-N;J=I+D+1
	G=[[0]*F for A in range(E)]
	for(K,L)in C:G[K][L]=2
	for(K,L)in H:G[K+(1-B)*D][L+B*D]=3
	for O in range(E if B else F):G[O if B else J][J if B else O]=8
	return G