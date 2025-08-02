def p(val_g):
	A=val_g;D=0
	if len({A for A in A[0]if A})>1:A=[list(A)for A in zip(*A)];D=1
	E,F=len(A),len(A[0]);B=0
	while B<E:
		G=next(A for A in A[B]if A);C=B
		while C<E and set(A[C])-{0}=={G}:C+=1
		H={B for C in range(B,C)for B in range(F)if A[C][B]==0}
		for I in range(B,C):
			for J in H:A[I][J]=0
		B=C
	if D:A=[list(A)for A in zip(*A)]
	return A