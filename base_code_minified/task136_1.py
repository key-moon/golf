def p(A):
	D=len(A);E,F=min((B,C)for B in range(D)for C in range(D)if A[B][C]==1);G,H=min((B,C)for B in range(D)for C in range(D)if A[B][C]==2);B,C=E,F
	while B and C:B-=1;C-=1;A[B][C]=1
	B,C=G+1,H+1
	while B<D-1 and C<D-1:B+=1;C+=1;A[B][C]=2
	return A