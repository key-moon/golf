def p(j):
	C,D=len(j),len(j[0]);E=lambda k:next((A,B)for A in range(C-1)for B in range(D-1)if j[A][B]==j[A+1][B+1]==k);A,B=E(1)
	while A>=1 and B>=1:A,B=A-1,B-1;j[A][B]=1
	A,B=E(2)
	while A<C-1 and B<D-1:A,B=A+1,B+1;j[A][B]=2
	return j