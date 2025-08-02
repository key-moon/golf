def p(g):
	F,G=len(g),len(g[0]);A={(A,B)for A in range(F)for B in range(G)if g[A][B]==2};L=A;J={(A,B)for A in range(F)for B in range(G)if g[A][B]==8};B,C=zip(*A);M,N=min(B),max(B);O,P=min(C),max(C);B,C=zip(*J);Q,R=min(B),max(B);S,T=min(C),max(C);D=Q+R-M-N;E=S+T-O-P
	if abs(D)>abs(E):E=0;D=D>0 and 1 or-1
	else:D=0;E=E>0 and 1 or-1
	while 1:
		K={(A+D,B+E)for(A,B)in A}
		if any(A<0 or A>=F or B<0 or B>=G or(A,B)in J for(A,B)in K):break
		A=K
	for(H,I)in L:g[H][I]=0
	for(H,I)in A:g[H][I]=2
	return g