def p(A):
	G,H=len(A),len(A[0]);B={(B,C)for B in range(G)for C in range(H)if A[B][C]==2};M=B;K={(B,C)for B in range(G)for C in range(H)if A[B][C]==8};C,D=zip(*B);N,O=min(C),max(C);P,Q=min(D),max(D);C,D=zip(*K);R,S=min(C),max(C);T,U=min(D),max(D);E=R+S-N-O;F=T+U-P-Q
	if abs(E)>abs(F):F=0;E=E>0 and 1 or-1
	else:E=0;F=F>0 and 1 or-1
	while 1:
		L={(A+E,B+F)for(A,B)in B}
		if any(A<0 or A>=G or B<0 or B>=H or(A,B)in K for(A,B)in L):break
		B=L
	for(I,J)in M:A[I][J]=0
	for(I,J)in B:A[I][J]=2
	return A