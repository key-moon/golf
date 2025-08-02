def p(g):
	D,E=len(g),len(g[0]);B=[(A,B)for A in range(D)for B in range(E)if g[A][B]==2];G=[(A,B)for A in range(D)for B in range(E)if g[A][B]==3];A=0 if all(A==B[0][0]for(A,C)in B)else 1;L=min(B[A]for B in B);O=max(B[A]for B in B);M=min(B[A]for B in G);H=max(B[A]for B in G)
	if H<L:C=L-1-H;I=M+C-1
	else:C=O+1-M;I=H+C+1
	F=[[0]*E for A in range(D)]
	for(J,K)in B:F[J][K]=2
	for(J,K)in G:F[J+(1-A)*C][K+A*C]=3
	for N in range(D if A else E):F[N if A else I][I if A else N]=8
	return F